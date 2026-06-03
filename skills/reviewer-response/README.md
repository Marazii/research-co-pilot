# reviewer-response

> Drafts a rigorous, polite, point-by-point response to reviewer comments (R1 / R2 / R3 letters) plus the matching manuscript revisions. Categorizes each comment, drafts the response, drafts the revision, assembles a cover letter. Won't concede a point the data doesn't support. Composes naturally with `peer-review` and `manuscript-drafter`.

**Triggered by:** `/respond`, plus *"respond to reviewers"*, *"R1 response"*, *"R2 response"*, *"rebuttal"*, *"address reviewer comments"*, *"reviewer-response letter"*, *"point-by-point response"*, *"revision and resubmission"*, *"cover letter to editor"*.

**Inputs needed:**

- Path to reviewer comments (one file or multiple).
- Path to the submitted manuscript.
- Round number (R1 / R2 / R3 / final).
- Journal name and submission system (affects formatting).
- For R2 / R3: path to the prior response letter.
- Optional: your posture per reviewer (where to concede, where to push back) — captured but not pre-deciding before reading the comments.

**Output:**

- `response_to_reviewers_<round>/` directory with: `cover_letter.md` (under 1 page) / `response.md` (point-by-point, all reviewers, each comment verbatim-quoted + response + revision pointer) / `revised_manuscript.md` (or `.docx`) / optional `revised_manuscript_tracked.md` for journals requiring tracked-changes / `change_log.md` (section-by-section list of all changes).

**Introduced in:** [v0.10.0-rc.1](../../CHANGELOG.md#0100-rc1--2026-05-12) — this is one of the new skills shipping with the maturity release.

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you've received a decision-with-revisions and need to draft the response package, when responding to R2 or R3 and the commitments from R1 must be reconciled, when reviewer 2 has been ambiguous and you need to interpret carefully, when one revision (e.g., a re-run analysis) addresses multiple reviewer points across the paper and the cross-references need to surface, or when an editor's letter adds asks beyond the reviewers' comments and they need to be triaged separately.

It is most valuable when comments come in conflict — Reviewer 1 wants more methodological depth, Reviewer 2 wants the methods compressed. The skill names the conflict explicitly and proposes a middle path that addresses both concerns.

## Example

**Input:** *"R1 from J. Hypothetical Studies. `./review_round1.md` (3 reviewers + editor letter). Manuscript at `./submission_v1.md`. First revision. Journal wants a single response document + tracked-changes manuscript."*

**Output:** `response_to_reviewers_R1/` containing:

1. **`cover_letter.md`** (under 1 page): acknowledges decision, summarizes 4 most consequential changes, names the one point of pushback up front.
2. **`response.md`**: every comment verbatim-quoted in italics, categorized (concession + revision / polite pushback / partial concession / out of scope), substantive response per category's tone, revision pointer (section + paragraph + lines).
3. **`revised_manuscript.md`** with the revisions applied — voice-matched to the existing draft via `manuscript-drafter` delegation for any revision > 1 paragraph.
4. **`revised_manuscript_tracked.md`** with tracked changes.
5. **`change_log.md`**: section-by-section list of every change with cross-reference back to the reviewer comment.

Self-audit: every comment got a response (count matches input), every claimed revision actually appears in the revised manuscript (cross-referenced), tone polite throughout, voice consistent with the existing manuscript.

See [`examples/reviewer-response/`](../../examples/reviewer-response/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`peer-review`** — When you've gotten pre-submission feedback from a colleague via peer-review, the output of that review is a clean input here. The categorization in Phase 2 maps directly.
- **`manuscript-drafter`** — For any revision longer than one paragraph, this skill delegates to manuscript-drafter so the new prose extracts and preserves the existing manuscript's voice profile + register rules.
- **`citation-formatter`** — Revisions that add new citations get the bibliography cleaned by citation-formatter after.
- **`ethics-committee`** — Reviewer comments that ask for ethics-section clarifications (consent, IRB, vulnerable populations) draw on ethics-committee for the structured response.

## Honest caveats

- **The response letter is a contract with the editor.** Anything you claim in the response must actually appear in the revised manuscript. The skill's self-audit cross-references these — but you read it before submitting.
- **Voice preservation in revisions** is best when manuscript-drafter's Phase 3 voice profile has been extracted (which happens when this skill delegates). If you bypass that delegation, voice mismatch is possible.
- **Tone is polite, not capitulating.** Pushback paragraphs are written firmly with reasoning grounded in the manuscript or data — not vague disagreement, not over-apologetic.
- **R2 / R3 rounds require reading the prior response.** Commitments made in R1 must be honored; the skill flags inconsistencies.
- **Multi-reviewer cross-fire** (R1 wants X, R2 wants the opposite of X) is named explicitly with a proposed middle path; sometimes the right move is to ask the editor for guidance instead — the skill flags when that's the case.
- **Journal-specific formatting** (some journals want one document per reviewer; some want a structured template; some want both clean and tracked-changes manuscripts) — match your target journal's published "response to reviewers" instructions.
