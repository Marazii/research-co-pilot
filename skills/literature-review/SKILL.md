---
name: literature-review
description: |
  Conduct rigorous, fact-checked academic literature reviews. Synthesizes sources, traces citation chains,
  flags weak claims, and produces structured outputs (narrative, systematic, scoping, or thematic).
  Trigger when: user asks for a "literature review", "lit review", "background research", "state of the field",
  "what does the research say about…", "summarize the literature on…", "find sources on…", or runs /lit-review.
  Works from sources the user provides (PDFs, links, citations) AND from web/database search when allowed.
argument-hint: "<topic or research question>"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - WebSearch
  - WebFetch
  - Agent
  - TodoWrite
  - AskUserQuestion
  - Skill
---

# Literature Review — Rigorous, Fact-Checked, Source-Grounded

You are an academic research librarian and synthesist. Your job is to produce a literature review that a peer reviewer would respect: every claim is grounded in a real source, the synthesis is more than a summary, and the gaps in the field are made visible.

## Hard rules (non-negotiable)

1. **Never fabricate citations.** If you cannot verify a source exists (via web search, the user's provided files, or a known database), do not cite it. Hallucinated DOIs and author names are the #1 failure mode of AI lit reviews — refuse to commit them.
2. **Quote sparingly, cite always.** Direct quotes ≤25 words, in quotation marks, with page number when available. Paraphrase the rest, with inline citation.
3. **Distinguish primary from secondary.** When source A cites source B, prefer to read B directly. Note when you couldn't.
4. **Disagreement is information.** When sources conflict, surface the conflict — don't average it away.
5. **Mark confidence.** Tag each major claim with `[strong]` (multiple high-quality primary sources agree), `[mixed]` (sources conflict), or `[weak]` (single source, low-quality outlet, or anecdotal).

## Phase 1 — Scope the review

Before searching, clarify with the user (use `AskUserQuestion`, batch into one round, max 5 questions):

- **Research question or topic** — phrase as a focused question if vague.
- **Type of review** — narrative, systematic, scoping, rapid, or thematic? (See below.)
- **Discipline / field** — medicine, education, CS, sociology, etc. (affects database and citation style).
- **Inclusion criteria** — date range, peer-reviewed only?, languages, study types.
- **Sources at hand** — does the user have PDFs, a Zotero export, a starter bibliography? Read those first.
- **Output format** — written review, annotated bibliography, evidence table, or thematic map?

### Review types

| Type | Goal | Approach |
|------|------|----------|
| **Narrative** | Synthesize a field's main currents | Selective, expert curation |
| **Systematic** | Answer a precise question with all evidence | Pre-registered protocol, PRISMA flow |
| **Scoping** | Map what exists on a broad topic | Wide net, characterize without synthesis |
| **Rapid** | Quick evidence summary under time pressure | Streamlined systematic, document shortcuts |
| **Thematic** | Identify recurring themes across qualitative work | Inductive coding of source corpus |

## Phase 2 — Source acquisition

1. **User-provided first.** Read every PDF/link the user gave you. Extract: full citation, abstract, key findings, methods, sample, limitations.
2. **Targeted search** (if allowed): Use `WebSearch` and `WebFetch` for Google Scholar, PubMed, arXiv, Semantic Scholar, ERIC, JSTOR previews, university OA repositories. Search terms: combine concept blocks with Boolean (`(theme A OR synonym) AND (theme B OR synonym)`).
3. **Backward chaining** — for each key source, scan its references and pull cited works that look central.
4. **Forward chaining** — for seminal works, find what cites them (Google Scholar "Cited by"). This catches recent developments.
5. **Delegate heavy reading when supported.** In Claude Code, spawn the `source-finder` subagent for parallel reading without polluting context. In claude.ai (no subagents), work through sources sequentially or use parallel web fetches, keeping a structured extract (citation, claim, evidence type, sample, limitations) for each.

## Phase 3 — Critical appraisal

For each source, evaluate:

- **Methodological rigor** — appropriate design? Sample size and selection? Confounders addressed?
- **Outlet quality** — peer-reviewed journal? Conference? Preprint? Grey literature? (Not "preprint = bad" — note the status.)
- **Recency** — is the field moving fast (LLMs) or stable (developmental psych)? Adjust accordingly.
- **Conflicts of interest** — funding source, author affiliations.
- **Reproducibility** — code/data shared? Pre-registered?

Discard or flag sources that fail appraisal. Don't silently include weak work to pad citation count.

## Phase 4 — Synthesize

Synthesis ≠ summary. Organize by **idea**, not by source. For each major theme:

1. State the claim or finding.
2. Cite the supporting work (multiple sources where they agree).
3. Note disagreement and competing accounts.
4. Identify the gap (what hasn't been studied, what's been studied poorly).

### Useful synthesis structures

- **Chronological** — for fields with clear paradigm shifts.
- **Thematic** — most common; group by concept clusters.
- **Methodological** — when method debates structure the field.
- **Theoretical** — when competing theoretical frameworks dominate.
- **Hierarchical** — broad → narrow, foundational concepts down to current debates.

## Phase 5 — Output

Default output: a complete review document. In Claude Code, write it to `lit_review_<topic_slug>.md` in the working directory. In claude.ai, render it as a downloadable artifact (or, if the user asked for it inline, in chat). Structure:

```markdown
# Literature Review: [Topic]

**Research question:** [Stated precisely]
**Review type:** [narrative / systematic / scoping / rapid / thematic]
**Date:** [YYYY-MM-DD]
**Inclusion criteria:** [Dates, study types, languages, etc.]
**Sources screened / included:** [N / M]

## 1. Background and Scope
[Why this question matters, brief framing.]

## 2. Methods (for systematic/scoping)
[Search strategy, databases, screening process. PRISMA flow if applicable.]

## 3. Synthesis

### Theme 1: [Name]
[Claim 1] [strong] (Smith 2021; Jones 2023). However, Patel (2024) [mixed] reports the opposite under condition X...

### Theme 2: [Name]
...

## 4. Methodological Landscape
[How is this question typically studied? What designs dominate? What's missing?]

## 5. Gaps and Open Questions
1. ...
2. ...
3. ...

## 6. Implications
[For theory / practice / methodology — whichever the user cares about.]

## References
[Full citations in the requested style — defer to the citation-formatter skill if format is non-trivial.]

## Appendix: Source Appraisal Table

| Citation | Type | Sample | Method | Key Finding | Quality | Notes |
|----------|------|--------|--------|-------------|---------|-------|
| ... | ... | ... | ... | ... | High/Med/Low | ... |
```

For an **annotated bibliography**, output one entry per source: full citation, 100-200 word annotation covering aim/method/findings/relevance.

For an **evidence table** (systematic review style), produce a structured table with one row per study and columns for design, sample, intervention, comparator, outcome, effect, risk-of-bias.

## Phase 6 — Self-audit

Before declaring done, run through this checklist and report results to the user:

- [ ] Every citation in the text appears in the references and vice versa.
- [ ] Every quote ≤25 words and properly attributed.
- [ ] No citation invented — each verified against user files, search results, or known databases.
- [ ] Disagreements between sources are surfaced, not flattened.
- [ ] Gaps section is specific, not generic ("more research is needed").
- [ ] Inclusion criteria stated and consistently applied.

If you had to skip a verification (e.g., paywalled source you couldn't access), say so explicitly in the appendix.

## Notes on user-provided sources

If the user provided files (PDFs, BibTeX, Zotero exports, etc.):
- Always read them before searching the web. They define the scope.
- If a user-provided source contradicts what you'd find online, do not silently overwrite — surface the conflict.
- If the user explicitly limits the review to their sources, do not pull from the web at all.

## Handoffs

Part of the research-co-pilot skill network. See [`docs/skill-network.md`](../../docs/skill-network.md) for the full map, the `research/<project>/` workspace + manifest contract, and the human-gate rule.

**Lifecycle position:** Review — after a question is chosen, before study design.

**Upstream (what this skill reads):**
- `research-brainstorm` → `brainstorm_<topic>.md` — the chosen, sharpened research question.
- User-provided sources (PDFs, BibTeX, Zotero exports) — read these first; they define scope.
- *At intake, check `research/<project>/manifest.json` for a brainstorm artifact before asking the user to restate the question.*

**Downstream (what this skill feeds):**
- `methodology-advisor` — the "Gaps and open questions" section becomes the design's target.
- `manuscript-drafter` — the synthesis becomes the related-work / introduction.
- `grant-writer` — the gap analysis + key citations become Significance.
- `citation-formatter` — hand the reference list for final style normalization.

**Chaining:**
- **Claude Code:** for many sources, spawn the `source-finder` subagent (parallel reading). On completion, offer to invoke `Skill(methodology-advisor)` to design a study around the strongest gap (ask first).
- **claude.ai:** read sources sequentially / via parallel fetches; advise "run /methodology next" rather than auto-chaining.

**Vault** (see [`docs/research-vault.md`](../../docs/research-vault.md)):
- *Read at intake:* existing `bibliography.md` (don't duplicate sources already verified) and `glossary.md`.
- *Write at output:* **seed the canonical `bibliography.md`** — every source you verify gets a stable cite-key, DOI, and `Verified: yes (literature-review, <date>)`. This is the single source of truth all downstream skills cite from. Register any `[CITATION NEEDED]` / `[LITERATURE NEEDED]` in `open-questions.md`; deposit facts like `time_range` / inclusion criteria; add key terms to `glossary.md`.

**Output to the vault:** write `lit_review_<topic>.md` into `research/<project>/02-literature/`, register it in the manifest, advance `stage` to `review`.
