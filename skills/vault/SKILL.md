---
name: vault
description: |
  Manage the research project's vault — the clean, visible, templated project folder (research/<project>/)
  where every file lives in a numbered lifecycle-stage place, plus the knowledge layer (canonical facts like
  sample size / IRB# / journal, one shared bibliography, decisions log, open questions, glossary, voice
  profile, entities — pseudonyms only, never PII). Initializes the folder from a template, shows a summary,
  ORGANIZES loose files into the right stage folders, AUDITS every artifact against the vault to catch drift
  (the sample size in the abstract vs the methods), and adds/resolves knowledge. Files stay the source of
  truth; the vault is the organized home the whole skill network reads and writes.
  Trigger when: user mentions "vault", "project folder", "organize my research", "research vault", "project
  knowledge", "audit my project", "check for inconsistencies", "is my sample size consistent", "project
  facts", "what's in the vault", "tidy my project", or runs /vault.
argument-hint: "[show | init [<project-slug>] | organize | audit | add <type> | resolve <question>]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Skill
  - AskUserQuestion
  - TodoWrite
---

# Vault — the project's home + librarian

You manage the research vault: the clean, visible, templated folder where a research project lives, and the knowledge layer inside it. The vault is **two things**: an organized project folder (`research/<project>/`, numbered by lifecycle stage) and a knowledge store (`knowledge/`). You scaffold it, keep it tidy, serve knowledge on request, and audit for drift.

Read [`docs/research-vault.md`](../../docs/research-vault.md) — the canonical spec (the folder template, the stage→folder map, the facts schema, the read/update protocol, the audit checks, the PII hard rule, portability). This skill implements that spec.

## Hard rules

1. **The vault never holds PII.** `knowledge/entities.md` stores pseudonyms + non-identifying attributes only; `06-data/` holds anonymized data only. The real-name key stays off-system. If you ever see a real name / email / phone / address in the vault or about to be written, STOP and flag it. The audit scans for this.
2. **Files are the source of truth; the vault is reconciled.** When the vault disagrees with a file, trust the file and correct the vault — never invent an artifact's contents.
3. **Distinct facts, not overwrites.** Two legitimately-different values (recruited N vs analyzed N) are kept as separate keys with notes — never silently overwritten. Only genuine contradictions are flagged.
4. **The vault is opt-in.** If there's no project folder and the user wants a one-off, don't force a vault. Offer to start one.
5. **Never fabricate knowledge.** Record what skills and the user actually established. Don't invent facts, citations, or decisions.
6. **`organize` and `audit` report or move files — they never edit an artifact's content.** Tidying relocates files and updates the manifest/README; fixing drift inside a document is the researcher's call.

## Determine the subcommand

Parse `$ARGUMENTS`; default to `show`. Find the project folder by looking for a `research/<slug>/manifest.json` (or the path the user names). If none exists and the subcommand isn't `init`, say so and offer `init`.

- (empty) / `show` → **Show** the project summary + refresh the root README.
- `init [<slug>]` → **Initialize** the project folder from the template.
- `organize` → **Tidy** loose files into the right stage folders.
- `audit` → **Audit** for drift.
- `add <type>` → **Add** a fact / decision / citation / question / term / entity.
- `resolve <question>` → **Resolve** an open question.

---

## Mode: `init`

Scaffold the full project home from the template (see the spec).

1. Ask for a short **project name** (→ a kebab-case `<slug>`) and the **working language** if not given.
2. Create `research/<slug>/` with the **complete template**: all numbered stage folders (`00-inbox/` … `10-dissemination/`), `knowledge/`, `audits/`, `archive/`. Add a `.gitkeep` to empty folders so the structure is visible.
3. Create `knowledge/` with the seven notes, each with its header + empty body. Put the **PII hard-rule reminder in bold at the top of `entities.md`** and at the top of `06-data/` (a short `README.md` saying "anonymized data only — never the real-name key").
4. Create `manifest.json` with base fields + empty `facts` + the `vault` registry + empty `artifacts`, `stage: "ideation"`.
5. Generate the root **`README.md`** (project title, stage, empty facts table, contents map, "no audit yet").
6. Report what was created and the next step ("run a skill, or `/research` pipeline mode — outputs file themselves into the right stage folder").

Claude Code: write the files. claude.ai: create them in the sandbox and tell the user to keep/download the folder.

---

## Mode: `show`

Read the manifest + `knowledge/*`, reconcile against the filesystem, then print a compact summary AND refresh the root `README.md` to match. Don't dump whole files.

```
📁 research/remote-work-mentorship/   ·   stage: drafting   ·   lang: en

Facts:  sample_size 247 · sample_size_analyzed 240 (after 7 excl.) · target_journal J. Hypothetical Studies · IRB …0142
Contents:
  01-ideation/     brainstorm_remote_work.md
  02-literature/   lit_review_remote_work.md
  03-methodology/  methodology_remote_work.md
  07-analysis/     analysis_remote_work.md (draft)
  08-drafts/       manuscript_discussion.md
Knowledge: 18 sources · 3 open questions · 11 decisions · voice profile ✓ · 12 entities
Last audit: 2026-06-03 (1 🔴, 1 🟡)  —  run /vault audit to re-check

Loose/unfiled: 00-inbox/notes.pdf  →  run /vault organize to file it
```

---

## Mode: `organize`

Tidy the project home. **Move files; never edit their content.**

1. Scan the project root and `00-inbox/` for loose artifacts. File each into its correct stage folder by recognizing its type (a `methodology_*.md` → `03-methodology/`, an `analysis_*.md` → `07-analysis/`, a `*_REVIEWED.*` → `09-review/`, etc. — use the stage→folder map). Ask before moving anything ambiguous.
2. For any artifact that supersedes an existing one (same skill + topic, newer), move the **older** version to `archive/` with a dated suffix.
3. Leave `06-data/` alone (the user manages data) except to confirm no real-name key sits there (if it might, flag 🔴, don't move).
4. Update `manifest.json` `artifacts` (paths, stages) to match the tidied layout.
5. Regenerate the root `README.md` contents map.
6. Report what moved and what (if anything) needs the user's decision.

---

## Mode: `audit`

Scan every artifact in the project folder against the vault. Write `audits/vault_audit_<date>.md` and summarize in chat. Run the **seven checks** from the spec: (1) fact consistency, (2) citation consistency, (3) terminology, (4) open questions, (5) staleness, (6) PII safety, (7) filing (artifacts in the wrong stage folder or loose).

Output format:

```markdown
# Vault Audit — remote-work-mentorship — 2026-06-03

**Stage:** drafting · **Artifacts scanned:** 6 · **Findings:** 🔴 2  🟡 2  🟢 1

## 🔴 Blockers
- **Fact mismatch — sample size.** Vault `sample_size` = 247 (methodology-advisor).
  08-drafts/manuscript_abstract.md says "247 participants"; 07-analysis/analysis_remote_work.md
  says "240 analyzed" with no tie. Likely "247 recruited, 240 analyzed". Record both as distinct facts.
- **PII — knowledge/entities.md line 6** looks like a real email. Remove; keep the pseudonym only.

## 🟡 Review
- **Unresolved marker.** [LITERATURE NEEDED] (sponsorship claim) still open in 08-drafts/manuscript_discussion.md.
- **Filing.** lit_review_remote_work.md is loose in the project root — belongs in 02-literature/ (run /vault organize).

## 🟢 Notes
- 07-analysis/analysis_remote_work.md marked `draft` at stage `drafting` — fine for now.

## Suggested next steps
- [ ] Reconcile the sample-size wording; record N-recruited and N-analyzed as distinct facts.
- [ ] Resolve or drop the open [LITERATURE NEEDED].
- [ ] Run /vault organize to file the loose review.
- [ ] Scrub the entities.md PII.
```

If there are no artifacts yet, say so and suggest running some skills first.

---

## Mode: `add <type>` / `resolve <question>`

- `add fact|decision|citation|question|term|entity` — ask for the minimum, write to the right `knowledge/` note (+ the manifest `facts` block for facts). Apply flag-on-write on a conflicting fact. Refuse PII for entities.
- `resolve <question>` — mark an `open-questions.md` item `[x]` with a short note on how (e.g. "added verified citation smith2021"); if it added a citation, fold it into `bibliography.md`.

Refresh the root `README.md` after any change.

---

## Handoffs

Part of the research-co-pilot skill network and the home for it. See [`docs/research-vault.md`](../../docs/research-vault.md) (the vault spec) and [`docs/skill-network.md`](../../docs/skill-network.md) (the network).

**Lifecycle position:** Infrastructure / cross-cutting — the project's home and librarian, not a lifecycle stage.

**Reads:** the whole project folder (`manifest.json` + `knowledge/*` + every stage folder).

**Used by:**
- Every skill — they read the vault at intake and file their output into the right stage folder at output (their own `## Handoffs` carry the specifics).
- `/research` (the conductor) — runs `Skill(vault)` with `init` at project start, `organize` to keep it tidy, and `audit` before the pre-submission stage.
- `peer-review` — a pre-submission `/vault audit` complements the manuscript-level review.

**Chaining:**
- **Claude Code:** `/vault` or `Skill(vault)`. Human-gated — `organize`/`audit` report or move files; they don't edit document content.
- **claude.ai:** invoke `vault` by name; it works on the folder present in the sandbox. No slash command, no cross-session filesystem.

## Notes

- `organize` and `audit` are how the project stays clean over months. Run `organize` after dropping files into `00-inbox/`; run `audit` before submitting anything.
- This is the place to answer "where's the methodology doc / what's our sample size / which journal / what did we decide about exclusions" without hunting through folders.
- Keep summaries tight — surface signal, not dumps.
