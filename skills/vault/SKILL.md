---
name: vault
description: |
  Manage the research project's knowledge vault — the canonical facts (sample size, IRB#, pre-registration,
  target journal, language), the single shared bibliography, the decisions log, consolidated open questions,
  the glossary, the voice profile, and entities (pseudonyms only, never PII). Initializes the vault, shows a
  summary, AUDITS every artifact against the vault to catch drift (the sample size in the abstract vs the
  methods vs the analysis), and lets you add or resolve knowledge by hand. The vault is the knowledge layer
  on top of the .research/ workspace; files stay the source of truth.
  Trigger when: user mentions "vault", "project knowledge", "research vault", "audit my project",
  "check for inconsistencies", "is my sample size consistent", "project facts", "canonical bibliography",
  "decisions log", "what's in the vault", "consistency check across my documents", or runs /vault.
argument-hint: "[show | init | audit | add <type> | resolve <question>]"
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

# Vault — the project's librarian

You manage the research vault: the canonical knowledge layer for a research project. The vault holds knowledge that belongs to the *whole project*, not one artifact — so it is stated once, read by every skill, and checked for drift. You are the librarian: you keep it tidy, you serve knowledge on request, and you audit for contradictions.

Read [`docs/research-vault.md`](../../docs/research-vault.md) — it is the canonical spec (structure, facts schema, note formats, the protocol, the six audit checks, the PII hard rule, portability). This skill implements that spec.

## Hard rules

1. **The vault never holds PII.** `entities.md` stores pseudonyms and non-identifying attributes only. The real-name → pseudonym key stays off-system. If you ever see a real name, email, phone, or address in the vault or about to be written to it, STOP and flag it. The audit scans for this.
2. **Files are the source of truth; the vault is reconciled.** When the vault disagrees with an artifact file, trust the file and correct the vault — never invent an artifact's contents to match the vault.
3. **Distinct facts, not overwrites.** Two legitimately-different-but-related values (recruited N vs analyzed N) are kept as separate keys with notes — never silently overwritten. Only genuine contradictions are flagged.
4. **The vault is opt-in.** If there is no `.research/` workspace and the user just wants a one-off, don't force a vault on them. Offer to start one.
5. **Never fabricate knowledge.** The vault records what skills and the user actually established. Don't populate facts, citations, or decisions you can't trace to a real source.

## Determine the subcommand

Parse `$ARGUMENTS`. Default to `show` if empty.

- (empty) or `show` → **Show** the vault summary.
- `init` → **Initialize** the vault.
- `audit` → **Audit** artifacts against the vault.
- `add <type>` → **Add** a fact / decision / citation / question / term / entity by hand.
- `resolve <question>` → **Resolve** an open question.

If `.research/manifest.json` doesn't exist and the subcommand isn't `init`, say so and offer to run `init` first.

---

## Mode: `init`

Scaffold the vault.

1. If `.research/` doesn't exist, create it. If `manifest.json` doesn't exist, create it with the v0.11.0 base fields (ask the user for a short project name + working language).
2. Add the `facts` block (empty or seeded from anything already known) and the `vault` registry to `manifest.json` (schema in the spec).
3. Create `.research/vault/` with the seven notes, each with its header and an empty body: `facts.md`, `bibliography.md`, `decisions.md`, `open-questions.md`, `glossary.md`, `voice-profile.md`, `entities.md`. Put the **PII hard-rule reminder in bold at the top of `entities.md`**.
4. Report what was created and what to do next ("run a skill, or `/research` pipeline mode, and the vault fills as you go").

Claude Code: write the files. claude.ai: create them in the sandbox and tell the user to download/keep them; the manifest can be pasted across sessions.

---

## Mode: `show`

Print a compact summary read from the vault. Do not dump whole files.

```
📚 Vault — <project>   ·   language: <lang>   ·   stage: <stage>

Facts:
  sample_size           247        (methodology-advisor, final)
  sample_size_analyzed  240        (data-analysis, final — after 7 exclusions)
  irb_number            IRB-…0142  (ethics-committee, final)
  target_journal        J. Hypothetical Studies
  preregistration       https://osf.io/xyz
  …

Bibliography:   18 sources (18 verified)
Open questions: 3 open · 5 resolved
Decisions:      11 logged   (most recent: 2026-06-03 · data-analysis · exclusion rule)
Voice profile:  present (English, passive, moderate hedging)
Entities:       12 participants (pseudonyms), 3 instruments

Run `/vault audit` to check artifacts for drift.
```

Reconcile against the filesystem first (rule 2). If a registered artifact is missing, note it.

---

## Mode: `audit`

The marquee feature. Scan every artifact under `.research/` against the vault and report contradictions. Write `vault_audit_<date>.md` and summarize in chat.

Run the **six checks** from the spec:

1. **Fact consistency.** For each fact in the manifest `facts` block, grep the artifacts for the value and for likely alternative phrasings of the same quantity. Where an artifact states a *different* value for the same fact, report it. Be smart about distinct-but-related facts: recruited-N vs analyzed-N are not a contradiction *if both are represented and the artifact is using the right one in the right place*. A 🔴 is a genuine mismatch (the abstract says 240 recruited; methods say 247 recruited).
2. **Citation consistency.** Every in-text citation in the artifacts should resolve to a `bibliography.md` cite-key; every bibliography entry should be marked verified; at stage `pre-submission` or later, no `[CITATION NEEDED]` / `[LITERATURE NEEDED]` should remain.
3. **Terminology.** Flag artifact terms that drift from the `glossary.md` canonical form (e.g., "mentoring" where the glossary says "mentorship", if the distinction matters).
4. **Open questions.** List unresolved markers across all artifacts and `open-questions.md`; flag any that should block submission.
5. **Staleness.** Facts or artifacts still `draft` at a late lifecycle stage (`pre-submission`+).
6. **PII safety.** Scan `entities.md` and all `.research/` artifacts for apparent real-name PII — email patterns, phone patterns, "Firstname Lastname" in participant context. Any hit is 🔴.

Output format:

```markdown
# Vault Audit — <project> — <date>

**Stage:** <stage>   ·   **Artifacts scanned:** <n>   ·   **Findings:** 🔴 <n>  🟡 <n>  🟢 <n>

## 🔴 Blockers
- **Fact mismatch — sample size.** Vault: `sample_size` = 247 (methodology-advisor).
  `manuscript_abstract.md` line 3 says "247 participants"; `analysis_remote_work.md` says
  "240 analyzed" with no note tying them. Likely the abstract should say "247 recruited,
  240 analyzed." Resolve and record both as distinct facts.
- **PII — entities.md line 6** contains what looks like a real email. Remove; keep pseudonym only.

## 🟡 Review
- **Unresolved marker.** `[LITERATURE NEEDED]` in manuscript_discussion.md (sponsorship claim) still open.
- **Terminology.** talk_outline.md uses "mentoring"; glossary canonical form is "mentorship".

## 🟢 Notes
- `analysis_remote_work.md` still marked `draft` at stage `drafting` — fine for now.

## Suggested next steps
- [ ] Reconcile sample-size wording across abstract / methods / analysis; record N-recruited and N-analyzed as distinct facts.
- [ ] Resolve the open [LITERATURE NEEDED] or drop the claim.
- [ ] Scrub the entities.md PII.
```

If there are no artifacts yet, say so and suggest running some skills first.

---

## Mode: `add <type>`

Deposit knowledge by hand. Types: `fact`, `decision`, `citation`, `question`, `term`, `entity`.

- Ask for the minimum needed (e.g., fact: key + value + status; citation: cite-key + full citation + DOI + verified?).
- For `fact`: if the key already exists with a different value, apply the flag-on-write rule — surface the conflict, ask whether it's a distinct fact or a correction, then record accordingly.
- For `entity`: refuse anything that looks like PII; record pseudonym + non-identifying attributes only.
- Write to the right note + (for facts) the manifest `facts` block. Keep `facts.md` and the manifest in sync.

---

## Mode: `resolve <question>`

Mark an open question in `open-questions.md` as resolved (`[x]`), with a short note on how (e.g., "added verified citation smith2021" or "claim dropped"). If resolving means a new citation, add it to `bibliography.md`.

---

## Handoffs

Part of the research-co-pilot skill network and the knowledge layer for it. See [`docs/research-vault.md`](../../docs/research-vault.md) (the vault spec) and [`docs/skill-network.md`](../../docs/skill-network.md) (the network + manifest contract).

**Lifecycle position:** Infrastructure / cross-cutting — not a lifecycle stage. The librarian for the whole project.

**Reads:** the entire vault (`manifest.json` facts + `.research/vault/*`) and every artifact under `.research/` (for the audit).

**Used by:**
- Every skill, indirectly — they read the vault at intake and update it at output (their own `## Handoffs` sections carry the specifics).
- `/research` (the conductor) — runs `Skill(vault)` with `init` at project start and `audit` before the pre-submission stage.
- `peer-review` — a pre-submission `/vault audit` complements the manuscript audit.

**Chaining:**
- **Claude Code:** invoked via `/vault` or as `Skill(vault)` by the conductor. Human-gated like everything else — the audit reports; it doesn't auto-fix.
- **claude.ai:** invoke the `vault` skill by name; it operates on the artifacts present in the conversation/sandbox. No slash command, no cross-session filesystem.

## Notes

- The audit **reports**; it does not auto-edit artifacts. Fixing drift is the researcher's call (often a one-word wording change, sometimes a real correction). Offer to make specific fixes, but don't apply them unprompted.
- Keep `show` and audit summaries tight — the vault can get large; surface signal, not dumps.
- This skill is the natural place to answer "what's our sample size again?" / "which journal are we targeting?" / "what did we decide about exclusions?" without re-reading every document.
