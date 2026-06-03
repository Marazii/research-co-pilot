# peer-review

> Multi-mode rigorous academic peer review in the voice of a seasoned professor. Two verdict modes (paper, homework), four alternative workflows (committee panel, fact-check audit, plagiarism-check, draft thinking-partner), plus iterate mode for post-review dialogue. **Returns a reviewed file with annotations anchored at the relevant locations** across `.docx` / `.pdf` / `.pptx` / `.tex`. Auto-detects Hebrew or English and the work's academic domain.

**Triggered by:** `/peer-review`, plus *"review my paper"*, *"critique this draft"*, *"feedback on my thesis"*, *"peer review"*, *"fact-check this manuscript"*, *"plagiarism audit"*, *"thinking partner on a draft"*, *"committee review"*, *"is this argument tight"*, *"review my slides"*.

**Inputs needed:**

- The document to review (`.docx`, `.pdf`, `.pptx`, `.tex`, or pasted text).
- Mode: paper verdict (Accept / Minor revisions / Major revisions / Reject) / homework verdict (grade band) / committee panel (3-5 reviewers with deliberate diversity) / fact-check audit / plagiarism-check / draft thinking-partner / presentation feedback / iterate (post-review).
- Optional: discipline / target venue / persona (e.g., "review as a senior empirical-psych professor") / language override.
- For `--presentation` mode: talk length, venue, audience.
- For iterate mode: link to or paste the prior review.

**Output:**

- Structured review delivered in chat: Header / Strengths / Major issues / Minor issues / Brilliance suggestions / Verdict / Forward-looking notes.
- **Annotated source file** anchored at the relevant locations:
  - `.docx` → inline comments + tracked changes (`_REVIEWED.docx`).
  - `.pdf` → sticky-note comments + highlights + strikethrough via PyMuPDF (`_REVIEWED.pdf`).
  - `.pptx` → native PowerPoint comments anchored to specific slides and shapes (`_REVIEWED.pptx`).
  - `.tex` → `% REVIEWER:` line comments above relevant lines, optional `changes`-package markup (`_REVIEWED.tex`).
- For Markdown / RTF / HTML / ODT / Pages / Google Docs / Jupyter / plain text: structured review only (with location markers like "section 3, paragraph 2").

**Introduced in:** [v0.1.0](../../CHANGELOG.md). Multi-mode workflows and the presentation-feedback mode added in [v0.5.0](../../CHANGELOG.md#050--2026-05-12); multi-format anchored annotations (PDF, PPTX native comments, LaTeX) in [v0.7.0](../../CHANGELOG.md#070--2026-05-12).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when getting pre-submission feedback on a paper (before sending it to a journal or to your advisor), when grading homework / dissertation chapters with the rigor of a senior reviewer, when auditing AI-assisted writing for hallucinated citations or factual drift, when checking a draft for paraphrased-but-uncredited arguments (plagiarism-style), when working through an unfinished draft as a thinking partner (no verdict, no scoring — just engagement), when getting a committee panel's worth of viewpoints before submission, when reviewing a colleague's conference talk before they give it, or when continuing a prior review with revision diffs (iterate mode).

The skill is intentionally not deferential. It is calibrated to give the kind of feedback an experienced reviewer who respects you would give — substantive, methodical, neither cruel nor flattering. Reviewers who only mark problems and reviewers who only give praise are equally useless.

## Example

**Input:** *"Review `./manuscript.docx`. Paper mode. Empirical psych. Target venue: J. Personality and Social Psychology."*

**Output:**

1. **Structured review** in chat: 8 major issues (3 methodological, 2 conceptual, 1 statistical, 2 framing), 12 minor issues (line-level), 4 strengths (with specifics), 2 brilliance suggestions (moves that would strengthen the paper beyond the minimum), verdict: Major revisions, forward-looking notes about a follow-up paper.
2. **`manuscript_REVIEWED.docx`** with: 23 inline comments anchored at the specific text spans they refer to (substantive concerns, citation requests, terminology checks); tracked changes for 14 line-level edits (typos, awkward phrasing with tighter alternatives, citation format errors). Every annotation rendered in Word's review pane.

For `.pdf` input: sticky-note comments + highlights at the located text + strikethrough where a wording change is suggested. For `.pptx`: native PowerPoint comments anchored per-slide and per-shape. For `.tex`: `% REVIEWER:` line comments above each relevant line.

See [`examples/peer-review/`](../../examples/peer-review/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`manuscript-drafter`** — Submit your manuscript-drafter output to peer-review for a pre-submission audit before sending to a journal.
- **`reviewer-response`** — When you receive an R&R, this skill's output structure (categorized issues + line-anchored comments) maps directly to reviewer-response's intake.
- **`literature-review`** — Cross-checks lit-review syntheses against actual source content in fact-check mode.
- **`talk-builder`** — Submit your drafted slides to peer-review in `--presentation` mode for a pre-conference critique.
- **`ethics-committee`** — Peer-review flags ethics-relevant issues in a manuscript; ethics-committee handles the deep audit.

## Honest caveats

- **Discipline coverage is broad but not infinite.** The skill applies rigor criteria appropriate to the work's auto-detected field. For highly specialized subfields, treat the output as a strong general review that a domain expert refines.
- **Fact-checking is best-effort.** Citations are checked against the bibliography and the web where accessible; paywalled sources flagged.
- **Anchoring requires the source file.** For pasted text or non-supported formats, the structured review still works but inline annotations require one of the four supported file types.
- **For .pptx native comments**, python-pptx + lxml authoring is used (the v0.5.0 speaker-notes-append behavior was replaced in v0.7.0 because native comments are the right mechanism, not a workaround).
- **The persona stays in role even in iterate mode.** Don't expect a generic chat-assistant tone in follow-up dialogue — the reviewer voice is preserved.
- **It is not a substitute for journal review.** Pre-submission audit only. Journals run their own.

## Author note

Designed by Maya Arazi. Maya specified the requirements, made the design calls (workflow modes, voice, hard rules, division of labor between structured review and inline annotations, anti-sycophancy posture, multi-format anchoring), and refined the skill across an extended back-and-forth.
