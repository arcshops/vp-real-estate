# Common Utilities — Slash Commands

The `common-utilities` plugin contributes a small set of cross-cutting utility commands that are useful across every other plugin in this marketplace (document conversion, git hygiene). Domain-specific commands live in their respective plugins.

## Commands (3)

All commands are namespaced under the `common-utilities` plugin.

- **`/common-utilities:convert-to-pdf`** — Convert markdown files (typically reports under `Reports/`) to professionally formatted PDF documents.
- **`/common-utilities:git-delete`** — Safely delete a local and/or remote git branch with confirmation prompts.
- **`/common-utilities:git-delete-comments`** — Remove resolved or stale review comments from a pull request.

## Full marketplace command inventory

For the complete cross-plugin slash-command catalogue (23 commands across `leasing-commercial`, `appraisal-valuation`, `expropriation-law`, and `common-utilities`), see the **Slash Commands** section of the repository root [`CLAUDE.md`](../../../CLAUDE.md).

That document also covers:

- Plugin namespacing conventions (e.g., `/leasing-commercial:abstract-lease`)
- The standard PDF → JSON → Python → Report workflow
- Report file-naming rules (`YYYY-MM-DD_HHMMSS_*.md`, Eastern Time)

## Adding a new utility command

1. Create `[name].md` under `plugins/common-utilities/commands/Utilities/`.
2. Add frontmatter with a clear `description`.
3. Document inputs, workflow, and outputs.
4. Update this README's command list.
