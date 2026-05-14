# manuscript-drafter

> Drafts long-form manuscript sections (abstract, intro, related work, methods, results, discussion, limitations, conclusion) from your methodology and analysis outputs. **Preserves the existing manuscript's voice**, **enforces hard per-section word budgets**, **enforces academic register**, and **literature-grounds every new idea**. Two-pass ideation → prose workflow. Drafts in the manuscript's language (English, Hebrew, etc.).

**Triggered by:** `/draft`, plus *"draft my paper"*, *"write the intro"*, *"write the methods section"*, *"draft the discussion"*, *"write the abstract"*, *"extend my discussion chapter"*, *"manuscript draft"*, *"first draft of paper"*.

**Inputs needed:**

- The existing manuscript draft (critical for voice extraction — without it the skill flags voice preservation cannot be enforced).
- The methodology document (output of `methodology-advisor` or your own).
- The analysis report (output of `data-analysis` or your own).
- The literature review (output of `literature-review` or your own).
- Your bibliography (BibTeX or paths to PDFs).
- Target journal / format + word budget per section.
- Sections needed (single section or full paper).

**Output:**

- `manuscript_<section>_<topic>.md` with: voice profile (extracted from existing prose) at top / ideation outline (each item tagged `[PULLED]`, `[RESTRUCTURED]`, or `[NEW]`) / the drafted section(s) / `[CITATION NEEDED]` index / `[LITERATURE NEEDED]` index / source map / word-count-vs-cap table / content cut for length log / register-audit log / voice-consistency-check log.

**Introduced in:** [v0.1.0](../../CHANGELOG.md). Comprehensively overhauled in [v0.8.0](../../CHANGELOG.md#080--2026-05-12) based on direct feedback from a senior reviewer: voice preservation (F1), hard word budgets (F2), academic register enforcement (F3), literature-ground every new idea (F4), two-pass ideation-then-prose workflow (F5), language-aware drafting (F6).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you have a methodology document and an analysis report and need them turned into manuscript prose, when extending an existing manuscript draft (the v0.8.0 overhaul prioritizes voice preservation for this case), when a reviewer asked you to "expand the discussion," when responding to an R&R that requires substantive new prose, and when you want the strong-part-of-the-skill (ideation) reviewable separately from the weaker part (prose execution) via the two-pass workflow.

It is not a substitute for the senior author's prose pass. Treat the output as a strong first draft that you read, revise, and own. The voice and register passes here aim to reduce that revision burden, not eliminate it.

## Example

**Input:** *"Extend the Discussion chapter of my dissertation (Hebrew, qualitative research on classroom dynamics). Inputs: existing_draft.md (full thesis-so-far), methodology.md, qual_findings.md, references.bib. Target: ~1500 words of new Discussion. Match the rest of the thesis."*

**Output:** `manuscript_discussion_classroom_dynamics.md` with:

1. **Voice profile** at top: sentence length (avg N words), person/voice (passive-leaning, third-person impersonal), hedge intensity (moderate), 5+ verbatim signature phrases from the existing thesis, connector vocabulary used ("אם כן", "יתרה מזאת", "בנוסף לכך"), citation style, paragraph length, Hebrew register tier (contemporary academic), gendered forms (feminine — matching the existing thesis).
2. **Ideation outline** with each new idea tagged `[NEW]` (3 methodological extensions and 2 interpretive moves), each accompanied by either a citation from references.bib or a `[LITERATURE NEEDED — claim / search terms / likely body of work]` marker.
3. **The drafted Discussion** (~1500 words, in Hebrew, matching the voice profile) with `[CITATION NEEDED]` markers inline where applicable.
4. **Logs:** word count vs. cap (target 1000-1800, cap 2200) — under cap, no cuts. Register audit log: no banned everyday-Hebrew patterns survived. Voice consistency log: 3 random new paragraphs sampled vs. 3 random existing paragraphs — indistinguishable to a careful reader.

See [`examples/manuscript-drafter/`](../../examples/manuscript-drafter/) for a worked sample.

## Composes well with

- **`literature-review`** — Pulls forward the synthesis into the related-work section.
- **`methodology-advisor`** — Methods section sourced verbatim where possible.
- **`data-analysis`** — Results section sourced from the analysis report; numerical claims trace back to it.
- **`qualitative-coding`** — Findings section sourced from the themes report.
- **`citation-formatter`** — Hand the draft to citation-formatter to clean the bibliography post-draft.
- **`peer-review`** — Submit the finished draft to peer-review for a pre-submission audit.
- **`reviewer-response`** — When responding to R&R, reviewer-response delegates new prose to manuscript-drafter so the revision matches the manuscript's voice.
- **`manuscript-drafter` subagent** — For drafts longer than ~3000 words, the parent skill delegates to the same-named subagent so the heavy prose work happens in isolation.

## Honest caveats

- **Voice preservation requires an existing manuscript.** Without one, the skill flags this prominently and proceeds with discipline-default voice — but every new paragraph is at risk of mismatch when the manuscript is eventually written.
- **Register audit is mechanical.** It substitutes banned patterns, but some banned patterns require rewriting whole sentences — the audit flags them and revises but may need a follow-up human pass.
- **Hard caps are enforced.** If your content exceeds the cap, the compression pass cuts; the cut content is logged separately (never silently dropped) for your decision about appendix / future paper.
- **Hebrew-specific register markers** (banned everyday patterns, classical-vs-contemporary connectors, gendered forms) are first-class. Other non-English languages are supported via the same voice-profile mechanism but the banned-pattern list is less elaborated.
- **No citations invented.** Sources must exist in your bibliography or be findable in lit-review output. Anything else is marked `[CITATION NEEDED]` (known claim, source missing) or `[LITERATURE NEEDED]` (new idea introduced, needs grounding).
