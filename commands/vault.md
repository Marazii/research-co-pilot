---
description: Manage the research project's knowledge vault — show, init, audit (drift check), add, or resolve
argument-hint: "[show | init | audit | add <type> | resolve <question>]"
---

Invoke the `vault` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/vault/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- The PII hard rule (the vault holds pseudonyms only; never real names / emails / phones / addresses).
- Files are the source of truth; the vault is reconciled, never trusted blindly.
- Distinct facts (recruited-N vs analyzed-N) are kept as separate keys, not overwritten.
- Subcommands: `show` (default) / `init` / `audit` / `add <type>` / `resolve <question>`.
- `init` scaffolds the visible `research/<slug>/` folder template (numbered stage folders + `knowledge/` + `audits/` + `archive/` + manifest + root README). `organize` files loose artifacts into their stage folders. `audit` runs the seven checks (fact consistency, citation consistency, terminology, open questions, staleness, PII safety, filing) and writes `audits/vault_audit_<date>.md` with 🔴/🟡/🟢 findings. `organize` moves files and `audit` reports — neither edits an artifact's content.

The vault spec is [`docs/research-vault.md`](../docs/research-vault.md).

User input:
$ARGUMENTS

If no subcommand was given, default to `show`. If there's no project vault yet (no `research/<slug>/manifest.json`), say so and offer to run `init`.
