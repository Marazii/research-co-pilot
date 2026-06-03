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
- `audit` runs the six checks (fact consistency, citation consistency, terminology, open questions, staleness, PII safety) and writes `vault_audit_<date>.md` with 🔴/🟡/🟢 findings. It reports; it does not auto-edit artifacts.

The vault spec is [`docs/research-vault.md`](../docs/research-vault.md).

User input:
$ARGUMENTS

If no subcommand was given, default to `show`. If there's no `.research/manifest.json` yet, say so and offer to run `init`.
