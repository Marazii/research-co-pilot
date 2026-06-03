# grant-writer

> Drafts proposal sections — Specific Aims, lay summary, Significance, Innovation, Approach, Broader Impacts, budget justification, data management plan, biosketch — tuned to NIH (R01 / R21 / F31 / K), NSF (Standard / CAREER / GRFP), ERC (Starting / Consolidator / Advanced), Wellcome, Horizon Europe, or foundation grants. Won't overpromise. Honest about scheme fit.

**Triggered by:** `/grant`, plus *"draft my specific aims"*, *"NSF broader impacts"*, *"ERC synopsis"*, *"R01 approach"*, *"fellowship application"*, *"biosketch"*, *"lay summary"*, *"grant proposal"*, *"research proposal"*.

**Inputs needed:**

- Funder + scheme (specific: "NIH R01" or "NSF CAREER" not just "a grant").
- Stage (first-time PI / mid-career / senior; new project / continuation / resubmission).
- Inputs: brainstorm output, methodology document, prior published work, preliminary data, the funder's solicitation, biosketch / CV, prior reviewer comments (for resubmissions).
- Sections needed and word/page budgets.
- Deadline.

**Output:**

- `grant_<funder>_<section>.md` (or a combined proposal document) with: fit-check note at the top (2-3 sentences on whether the project fits the scheme honestly) / the drafted section(s) / `[CITATION NEEDED]` / `[PRELIMINARY DATA NEEDED]` / `[REVIEWER CONCERN UNADDRESSED]` indices / word/page counts vs. target.

**Introduced in:** [v0.2.0](../../CHANGELOG.md#020--2026-05-10).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when drafting a Specific Aims page (the most-read page in any NIH submission), when writing the Significance / Innovation / Approach sections of an R01, when responding to summary-statement criticism for a resubmission, when drafting NSF Broader Impacts that aren't boilerplate, when preparing an ERC synopsis that reads as ground-breaking rather than incremental, or when writing a fellowship Personal Statement that has narrative weight.

It is opinionated about overpromising. Grants that claim to "revolutionize the field" without specifics get flagged. Grants where the project doesn't fit the scheme (under-developed preliminary data for R01; over-senior for an early-career fellowship) get fit-checked at the top so you can adjust before drafting goes deep.

## Example

**Input:** *"NIH R01 application, first-time PI, project on neuroinflammation biomarkers, I have preliminary data from a pilot (N=24), deadline is 6 weeks. Need Specific Aims + Significance + Approach."*

**Output:** `grant_NIH_R01_neuroinflammation.md` with:

1. **Fit-check note:** preliminary data adequate for R01 (n=24 pilot with effect sizes); first-time PI flag for the reviewer's expectation of mentorship + environment substantiation.
2. **Specific Aims (1 page):** paragraph 1 — significance + gap (with hard numbers from prior literature); paragraph 2 — long-term goal + central hypothesis + objective; Aims 1-3 each as a heading with 2-3 sentences and sub-aims as bullets; closing paragraph — expected outcomes + impact.
3. **Significance (~2 pp):** burden quantified, gap specific, why this work is now feasible.
4. **Approach (~9 pp):** per aim — rationale (with preliminary data plot referenced), design, methods at reviewer-judgment depth, expected outcomes for each possible result, pitfalls + alternative approaches named explicitly (a strength, not a weakness).
5. **[REVIEWER CONCERN UNADDRESSED]** markers for two anticipated concerns the user should pre-empt.

See [`examples/grant-writer/`](../../examples/grant-writer/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `.research/` workspace contract live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`research-brainstorm`** — Brainstorm shapes the Specific Aims (each aim should be defensible as one of the strongest candidates from the brainstorm).
- **`methodology-advisor`** — Approach section sourced directly from the methodology document.
- **`literature-review`** — Significance section sourced from the lit-review's gap analysis and key citations.
- **`ethics-committee`** — Data management plan and human-subjects sections benefit from an ethics audit.
- **`citation-formatter`** — Final pass to format the bibliography per funder requirements.

## Honest caveats

- **Grant funding is a function of grantsmanship that no skill can fully replicate** — relationships with program officers, alignment with current portfolio gaps, study-section timing. The draft is one input among many; success depends on broader institutional work.
- **Fit-check is honest.** If the project doesn't fit the scheme as drafted (e.g., insufficient preliminary data for R01; scope mismatch with NSF program), the skill says so before drafting goes deep. This is more useful than producing a polished application destined to be desk-rejected.
- **Specialized schemes** (cooperative agreements, training grants, equipment grants, conference grants, consortium agreements) require non-standard sections — the skill points at the program announcement and adapts where it can.
- **Funder-specific reviewer norms** (NIH study-section culture, ERC panel expectations) are encoded as defaults; the user's own field knowledge of which reviewers will read the proposal is irreplaceable.
- **No fabricated preliminary data.** The skill won't invent pilot results to plug a gap. `[PRELIMINARY DATA NEEDED]` markers surface what would strengthen the proposal.
- **Note on grant-writer v0.X (planned):** v0.9.0 is planned to apply the manuscript-drafter v0.8.0 overhaul (voice preservation, length budgets, register, literature-grounding, two-pass) to grant-writer as well. Until then, grant-writer's discipline is funder-specific rather than voice-specific.
