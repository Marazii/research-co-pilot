# vault

> The project's home + librarian. Manages the **research vault** — a clean, visible, templated folder (`research/<project>/`) where every research file lives in a numbered lifecycle-stage place, plus the knowledge layer (canonical facts, one shared bibliography, decisions log, open questions, glossary, voice profile, entities — pseudonyms only, never PII). Files your outputs, keeps the folder tidy, and audits every document for drift.

**Triggered by:** `/vault`, plus *"organize my research"*, *"tidy my project"*, *"audit my project"*, *"check for inconsistencies"*, *"is my sample size consistent"*, *"project facts"*, *"what's in the vault"*, *"where's my methodology doc"*.

**Inputs needed:**

- A project vault (run `/vault init` to scaffold one). It reads `research/<project>/manifest.json` + `knowledge/*` + the stage folders.
- For `organize`: loose files in the project root or `00-inbox/`.
- For `audit`: the artifacts across the stage folders.
- For `add` / `resolve`: the knowledge to deposit or the question to close.

**Output:**

- `init` — a scaffolded `research/<project>/` folder: numbered stage folders (`01-ideation/` … `10-dissemination/`), `knowledge/` (seven notes), `audits/`, `archive/`, `manifest.json`, and an auto-generated root `README.md`.
- `show` — a compact project summary (facts, stage, contents map, vault counts) + a refreshed root `README.md`.
- `organize` — loose files moved into their stage folders, superseded versions to `archive/`, manifest + README updated. **Moves files; never edits content.**
- `audit` — `audits/vault_audit_<date>.md` with 🔴/🟡/🟢 findings + a chat summary. **Reports drift; does not auto-edit.**
- `add` / `resolve` — updated `knowledge/` notes + manifest + README.

**Introduced in:** [v0.11.1](../../CHANGELOG.md) (knowledge layer); the visible templated project folder landed in [v0.11.2](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md) · canonical vault contract: [`docs/research-vault.md`](../../docs/research-vault.md)

## When to use this

Use this to **start an organized project** (`/vault init` gives you a clean folder where every skill's output has a place), to **find anything** ("what's our sample size / which journal / where's the methodology doc") without hunting, to **tidy up** after dropping files into `00-inbox/` (`/vault organize`), and — most importantly — to **catch drift before you submit** (`/vault audit`): the abstract that says N=240 while the methods say 247, a citation that doesn't resolve, a term used three ways, or PII that slipped into the wrong file.

Most of the time the vault fills itself as you run other skills — they read it at intake and file their output into the right stage folder at output. You reach for `/vault` to **start** it (`init`), **see** it (`show`), **tidy** it (`organize`), or **check** it (`audit`).

## Example

**Input:** *"/vault audit"* — a project where the methodology says N=247 and the analysis (after exclusions) says N=240, one `[LITERATURE NEEDED]` is still open, and a lit review is sitting loose in the project root.

**Output:** `audits/vault_audit_2026-06-03.md` reporting:

- 🔴 **Fact mismatch — sample size:** the abstract uses 240 where the vault + methods say 247 recruited / 240 analyzed. Record both as distinct facts.
- 🟡 **Unresolved marker:** `[LITERATURE NEEDED]` (sponsorship claim) still open in `08-drafts/manuscript_discussion.md`.
- 🟡 **Filing:** `lit_review_remote_work.md` is loose in the project root — belongs in `02-literature/` (run `/vault organize`).

Plus suggested next steps. The audit reports; you decide what to fix.

## Composes well with

*The home for the [skill network](../../docs/skill-network.md). Full contract: the [research vault spec](../../docs/research-vault.md).*

- **Every skill** — they read the vault at intake (facts, bibliography, glossary, voice profile) and file their output into the right stage folder at output.
- **`/research` (conductor)** — runs `vault init` at project start, `organize` to keep it tidy, and `vault audit` before the pre-submission stage.
- **`peer-review`** — a pre-submission `/vault audit` complements the manuscript-level review: one checks the paper, the other checks consistency across *all* the project's documents.
- **`citation-formatter`** — renders any citation style from the vault's canonical `knowledge/bibliography.md` rather than a parallel list.

## Honest caveats

- **The audit reports; `organize` only moves files. Neither edits an artifact's content.** Fixing drift inside a document is your call; the skill offers specific fixes but won't apply them unprompted.
- **The vault never holds PII.** Pseudonyms + non-identifying attributes only; `06-data/` is anonymized data only; the real-name key stays off-system. The audit scans for accidental PII and flags it 🔴.
- **Files are the source of truth.** If the vault and a file disagree, the file wins and the vault is corrected — the vault never invents an artifact's contents.
- **Opt-in.** No project vault? Run any skill standalone exactly as before; the vault only engages when you start one.
- **claude.ai** has no slash command or cross-session filesystem — invoke the `vault` skill by name; it works on the folder present in the sandbox, and you re-upload the project folder across sessions.
