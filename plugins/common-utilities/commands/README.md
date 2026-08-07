# Common Utilities — Slash Commands

The `common-utilities` plugin contributes cross-cutting utility commands useful across the marketplace, including broker operating workflows and document/git utilities. Domain-specific analysis commands remain in their respective plugins.

## Commands (6)

All commands are namespaced under the `common-utilities` plugin.

### Broker cockpit

- **`/common-utilities:broker-daily`** — Produce a two-minute daily CRE priority brief: Top 3, waiting-on-others, deadlines/risk, deals to move, and work that can wait.
- **`/common-utilities:deal-intake`** — Convert rough transaction notes into a clean deal snapshot, open-item list, follow-up log, material risks, and next three actions.
- **`/common-utilities:deal-follow-up`** — Decide who should be contacted now, what the specific ask should be, when to wait, and when escalation is justified.

### Utilities

- **`/common-utilities:convert-to-pdf`** — Convert markdown files (typically reports under `Reports/`) to professionally formatted PDF documents.
- **`/common-utilities:git-delete`** — Safely delete a local and/or remote git branch with confirmation prompts.
- **`/common-utilities:git-delete-comments`** — Remove resolved or stale review comments from a pull request.

## Full marketplace command inventory

For the complete cross-plugin slash-command catalogue, see the **Slash Commands** section of the repository root [`CLAUDE.md`](../../../CLAUDE.md).

That document also covers:

- Plugin namespacing conventions (e.g., `/leasing-commercial:abstract-lease`)
- The standard PDF → JSON → Python → Report workflow
- Report file-naming rules (`YYYY-MM-DD_HHMMSS_*.md`, Eastern Time)

## Adding a new utility command

1. Create `[name].md` under `plugins/common-utilities/commands/Utilities/`.
2. Add frontmatter with a clear `description`.
3. Document inputs, workflow, and outputs.
4. Update this README's command list.
