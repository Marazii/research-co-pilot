# vault

> The project's librarian. Manages the research knowledge vault — canonical facts (sample N, IRB#, pre-reg, journal, language), the single shared bibliography, the decisions log, consolidated open questions, the glossary, the voice profile, and entities (pseudonyms only, never PII). Audits every artifact against the vault to catch drift.

**Triggered by:** `/vault`, plus *"audit my project"*, *"check for inconsistencies"*, *"is my sample size consistent"*, *"project facts"*, *"canonical bibliography"*, *"what's in the vault"*, *"consistency check across my documents"*.

**Inputs needed:**

- A `.research/` workspace (run `/vault init` if you don't have one). The vault reads `manifest.json` (facts block) and `.research/vault/*` notes.
- For `audit`: the artifacts under `.research/` to scan.
- For `add` / `resolve`: the knowledge to deposit or the question to close.

**Output:**

- `show` — a compact vault summary (facts table, bibliography count, open/resolved questions, recent decisions, voice profile, entities) in chat.
- `init` — a scaffolded `.research/vault/` + the manifest `facts`/`vault` blocks.
- `audit` — `vault_audit_<date>.md` with 🔴/🟡/🟢 findings + a chat summary. **Reports drift; does not auto-edit.**
- `add` / `resolve` — updated vault notes + manifest.

**Introduced in:** [v0.11.1](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md) · canonical vault contract: [`docs/research-vault.md`](../../docs/research-vault.md)

## When to use this

Use this when you want a single answer to "what's our sample size / target journal / IRB number again?" without re-reading every document; when you're about to submit and want to catch the abstract-says-240-but-methods-say-247 class of error before a reviewer does; when you want one canonical bibliography that the draft, the talk, and the grant all cite from; or when you want a consolidated list of every open `[CITATION NEEDED]` / `[LITERATURE NEEDED]` across the whole project.

It's the knowledge layer on top of the `.research/` workspace. Most of the time the vault fills itself as you run other skills — they read it at intake and update it at output. You reach for `/vault` directly to **see** it (`show`), **start** it (`init`), or **check** it (`audit`).

## Example

**Input:** *"/vault audit"* — with a project where the methodology says N=247 and the analysis (after exclusions) says N=240, and one `[LITERATURE NEEDED]` still open in the discussion.

**Output:** `vault_audit_2026-06-03.md` reporting:

- 🔴 **Fact mismatch — sample size:** the abstract says "240 participants" but the vault + methods say 247 recruited / 240 analyzed; the abstract is using the wrong N. Resolve and record both as distinct facts.
- 🟡 **Unresolved marker:** `[LITERATURE NEEDED]` (sponsorship claim) still open in `manuscript_discussion.md`.
- 🟢 **Note:** `analysis_remote_work.md` still marked `draft` — fine at this stage.

Plus suggested next steps. The audit reports; you decide what to fix.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md), and the manager of the [research vault](../../docs/research-vault.md) that the whole network reads and writes.*

- **Every skill** — they read the vault at intake (facts, bibliography, glossary, voice profile) and update it at output. The vault is where their shared knowledge lives.
- **`/research` (conductor)** — runs `vault init` at project start and `vault audit` before the pre-submission stage.
- **`peer-review`** — a pre-submission `/vault audit` complements the manuscript-level audit: one checks the paper, the other checks consistency across *all* the project's documents.
- **`citation-formatter`** — renders any citation style from the vault's canonical `bibliography.md` rather than a parallel list.

## Honest caveats

- **The audit reports; it doesn't auto-fix.** Drift is often a one-word wording change, but sometimes a real correction only you can make. The skill offers specific fixes; it won't apply them unprompted.
- **The vault never holds PII.** Pseudonyms and non-identifying attributes only; the real-name key stays off-system. The audit scans for accidental PII and flags it 🔴.
- **Files are the source of truth.** If the vault and an artifact disagree, the file wins and the vault is corrected — the vault never invents artifact contents.
- **Opt-in.** No `.research/`? Run any skill standalone exactly as before; the vault only engages when you start one.
- **claude.ai** has no slash command or cross-session filesystem — invoke the `vault` skill by name; it works on the artifacts present in the conversation/sandbox, and you re-upload the vault notes across sessions.
