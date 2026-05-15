#!/usr/bin/env python3
"""
Easement Valuation Calculator

Computes ROW easement value using three methods and reconciles them:
  1. Percentage of Fee
  2. Income Capitalization
  3. Before/After (market extraction)

Then adds optional compensation components (temporary construction easement,
injurious affection, severance, disturbance allowance).

USAGE:
    python easement_valuation_calculator.py <input.json> [-o output.json] [--verbose]

INPUT schema (see SKILL.md "Easement Valuation Methods" → "Calculator Integration"):
    corridor_specifications, property, valuation_methods,
    reconciliation_weights (optional), additional_compensation (optional)

OUTPUT: JSON with per-method values, reconciled value, additional compensation,
and a grand total.
"""

import argparse
import json
import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(__file__))

SQ_METERS_PER_ACRE = 4046.8564224

DEFAULT_RECONCILIATION_WEIGHTS = {
    "percentage_of_fee": 0.40,
    "income_capitalization": 0.40,
    "before_after": 0.20,
}


def compute_row_acres(corridor: Dict[str, Any]) -> float:
    """Convert corridor width×length (meters) to acres."""
    width = float(corridor["width_meters"])
    length = float(corridor["length_meters"])
    return (width * length) / SQ_METERS_PER_ACRE


def percentage_of_fee_value(row_acres: float, property_data: Dict[str, Any],
                            method_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Easement Value = ROW Acres × Fee/Acre × Adjusted %"""
    fee_per_acre = float(property_data["fee_simple_value_per_acre"])
    adjusted_pct = float(method_inputs.get(
        "adjusted_percentage",
        method_inputs.get("base_percentage", 0.0),
    ))
    base_pct = float(method_inputs.get("base_percentage", adjusted_pct))
    value = row_acres * fee_per_acre * adjusted_pct
    return {
        "row_acres": row_acres,
        "fee_simple_value_per_acre": fee_per_acre,
        "base_percentage": base_pct,
        "adjusted_percentage": adjusted_pct,
        "value": value,
    }


def income_capitalization_value(row_acres: float, property_data: Dict[str, Any],
                                method_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Easement Value = (Rent/acre × Productivity Loss % × ROW acres) ÷ Cap Rate"""
    annual_rent = float(property_data.get("annual_rent_per_acre", 0.0))
    productivity_loss = float(method_inputs["productivity_loss_percentage"])
    cap_rate = float(method_inputs["cap_rate"])
    if cap_rate <= 0:
        raise ValueError("income_capitalization.cap_rate must be > 0")
    annual_income_loss = annual_rent * productivity_loss * row_acres
    value = annual_income_loss / cap_rate
    return {
        "annual_rent_per_acre": annual_rent,
        "productivity_loss_percentage": productivity_loss,
        "row_acres": row_acres,
        "annual_income_loss": annual_income_loss,
        "cap_rate": cap_rate,
        "value": value,
    }


def before_after_value(row_acres: float, method_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Easement Value = ROW acres × ((value_before − value_after) ÷ easement_acres_comparable)

    Falls back to (value_before − value_after) when comparable acres are not provided
    (i.e., inputs already represent subject-property values).
    """
    value_before = float(method_inputs["value_before"])
    value_after = float(method_inputs["value_after"])
    diminution = value_before - value_after
    comparable_easement_acres = method_inputs.get("comparable_easement_acres")
    if comparable_easement_acres:
        per_acre = diminution / float(comparable_easement_acres)
        value = row_acres * per_acre
        details = {"implied_value_per_row_acre": per_acre}
    else:
        value = diminution
        details = {}
    return {
        "value_before": value_before,
        "value_after": value_after,
        "diminution_in_value": diminution,
        **details,
        "value": value,
    }


def reconcile(method_values: Dict[str, float],
              weights: Dict[str, float]) -> Dict[str, Any]:
    """Weighted reconciliation across available methods; weights are renormalized
    over the methods actually computed."""
    available = {k: w for k, w in weights.items() if k in method_values and w > 0}
    total_weight = sum(available.values())
    if total_weight <= 0:
        raise ValueError("No reconciliation weights apply to the computed methods")
    normalized = {k: w / total_weight for k, w in available.items()}
    reconciled = sum(method_values[k] * normalized[k] for k in normalized)
    return {
        "applied_weights": normalized,
        "reconciled_value": reconciled,
    }


def compute_additional_compensation(add_on: Dict[str, Any]) -> Dict[str, Any]:
    """Sum optional add-on components if provided."""
    if not add_on:
        return {"total": 0.0, "components": {}}

    components: Dict[str, float] = {}

    tce = add_on.get("temporary_construction_easement")
    if tce:
        area_acres = float(tce.get("area_acres", 0.0))
        annual_revenue = float(tce.get("annual_revenue_per_acre", 0.0))
        seasons_lost = float(tce.get("growing_seasons_lost", 0.0))
        restoration = float(tce.get("restoration_costs", 0.0))
        crop_damage = float(tce.get("crop_damage", 0.0))
        fence_repair = float(tce.get("fence_repair", 0.0))
        components["temporary_construction_easement"] = (
            area_acres * annual_revenue * seasons_lost
            + restoration + crop_damage + fence_repair
        )

    severance = add_on.get("severance_damages")
    if severance:
        before_hbu = float(severance["before_hbu_value_per_acre"])
        after_hbu = float(severance["after_hbu_value_per_acre"])
        remainder_acres = float(severance["remainder_acres"])
        components["severance_damages"] = (before_hbu - after_hbu) * remainder_acres

    injurious = add_on.get("injurious_affection")
    if injurious is not None:
        components["injurious_affection"] = float(injurious)

    disturbance = add_on.get("disturbance_allowance")
    if disturbance is not None:
        components["disturbance_allowance"] = float(disturbance)

    return {"total": sum(components.values()), "components": components}


def calculate(input_data: Dict[str, Any], verbose: bool = False) -> Dict[str, Any]:
    corridor = input_data["corridor_specifications"]
    property_data = input_data["property"]
    methods = input_data["valuation_methods"]

    row_acres = compute_row_acres(corridor)
    if verbose:
        print(f"ROW area: {row_acres:.2f} acres")

    method_results: Dict[str, Any] = {}
    method_values: Dict[str, float] = {}

    if "percentage_of_fee" in methods:
        method_results["percentage_of_fee"] = percentage_of_fee_value(
            row_acres, property_data, methods["percentage_of_fee"]
        )
        method_values["percentage_of_fee"] = method_results["percentage_of_fee"]["value"]
        if verbose:
            print(f"  Percentage of Fee:     ${method_values['percentage_of_fee']:>14,.0f}")

    if "income_capitalization" in methods:
        method_results["income_capitalization"] = income_capitalization_value(
            row_acres, property_data, methods["income_capitalization"]
        )
        method_values["income_capitalization"] = method_results["income_capitalization"]["value"]
        if verbose:
            print(f"  Income Capitalization: ${method_values['income_capitalization']:>14,.0f}")

    if "before_after" in methods:
        method_results["before_after"] = before_after_value(
            row_acres, methods["before_after"]
        )
        method_values["before_after"] = method_results["before_after"]["value"]
        if verbose:
            print(f"  Before/After:          ${method_values['before_after']:>14,.0f}")

    if not method_values:
        raise ValueError("No valuation methods provided in input")

    weights = input_data.get("reconciliation_weights", DEFAULT_RECONCILIATION_WEIGHTS)
    reconciliation = reconcile(method_values, weights)
    if verbose:
        print(f"  Reconciled value:      ${reconciliation['reconciled_value']:>14,.0f}")

    additional = compute_additional_compensation(input_data.get("additional_compensation", {}))
    if verbose and additional["components"]:
        for name, val in additional["components"].items():
            print(f"  + {name}: ${val:,.0f}")

    total = reconciliation["reconciled_value"] + additional["total"]
    if verbose:
        print(f"  TOTAL compensation:    ${total:>14,.0f}")

    return {
        "inputs": input_data,
        "row_acres": row_acres,
        "method_results": method_results,
        "reconciliation": reconciliation,
        "additional_compensation": additional,
        "total_compensation": total,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Easement Valuation Calculator — three-method reconciliation"
    )
    parser.add_argument("input_file", help="Path to input JSON file")
    parser.add_argument("-o", "--output", help="Output path for results JSON")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print intermediate values")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"ERROR: Input file not found: {args.input_file}", file=sys.stderr)
        return 1

    try:
        with open(args.input_file, "r") as f:
            input_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}", file=sys.stderr)
        return 1

    try:
        results = calculate(input_data, verbose=args.verbose)
    except (KeyError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    output_path = args.output
    if output_path is None:
        base = os.path.splitext(os.path.basename(args.input_file))[0]
        output_dir = os.path.join(os.path.dirname(__file__), "row_outputs")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{base}_results.json")
    else:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    if args.verbose:
        print(f"\nResults written to: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
