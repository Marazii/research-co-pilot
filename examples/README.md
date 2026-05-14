# Examples

One synthetic, minimal example per skill. The goal is to show **what kind of output you get** for the typical input — not to ship publication-quality artifacts. All names, citations, and findings are fictional.

| Skill | Input | Output | Status |
|---|---|---|---|
| [literature-review](./literature-review/) | Topic + 2 starter citations | Thematic review with confidence-tagged claims | ✅ shipped |
| [methodology-advisor](./methodology-advisor/) | Research question + constraints | Methodology doc including mandatory Phase 5 (AI / ML / Big Data extensions table) | ✅ shipped |
| [ethics-committee](./ethics-committee/) | Protocol summary | IRB-style decision letter with required revisions | ✅ shipped |
| [data-analysis](./data-analysis/) | Tiny CSV + analytic question | Script + report with effect sizes and CIs | ✅ shipped |
| [qualitative-coding](./qualitative-coding/) | 2 short transcripts + research question | Codebook + coded excerpts + themes report | ✅ shipped |
| [research-brainstorm](./research-brainstorm/) | Rough topic + constraints | 18 candidate questions, top 3 sketched | ✅ shipped |
| [manuscript-drafter](./manuscript-drafter/) | Methodology + analysis + existing draft + bibliography | Discussion section with voice profile, ideation outline, `[LITERATURE NEEDED]` markers | ✅ shipped — showcases the v0.8.0 overhaul |
| [replication-designer](./replication-designer/) | A target paper citation | Replication design with power calc, pre-reg plan, success criteria | ✅ shipped |
| [grant-writer](./grant-writer/) | Project + funder (NSF) | Specific Aims + Significance snippets + fit-check note | ✅ shipped |
| [talk-builder](./talk-builder/) | Paper + length + venue | Timed beat-by-beat outline + Marp slide deck stub (`talk.md`) | ✅ shipped |
| [citation-formatter](./citation-formatter/) | 3 messy citations | Cleaned APA 7 + Vancouver + BibTeX | ✅ shipped |
| [survey-design](./survey-design/) | Construct + population | Instrument with validated scales + pilot plan | ✅ shipped |
| [peer-review](./peer-review/) | Manuscript excerpt | Structured review + annotated-document description | ✅ shipped |
| [reviewer-response](./reviewer-response/) | R1 reviewer comments + manuscript draft | Cover letter + point-by-point response + revisions | ✅ shipped |

All 14 examples shipping with `v0.10.0` final.

## Conventions

- All examples are **synthetic and minimal**. Inputs are short; outputs are a representative slice of what the skill produces (not the full 12-page artifact).
- Fictional placeholder journals (`J. Hypothetical Studies`), authors (`Smith et al.`, `Jones & Patel`), and citations. No real paper content is reproduced.
- No real participant data, no PII, no protected health information.
- Examples reflect the **current shipped version** of each skill. If a skill's output format changes, the example must be updated as part of the same PR (see [`CONTRIBUTING.md`](../CONTRIBUTING.md)).

## How to use these

- **As a user evaluating the plugin:** skim a few to decide whether the output matches what you'd want for your research workflow.
- **As a contributor:** when proposing a new skill, follow the input + output pair pattern.
- **As a maintainer reviewing PRs:** confirm the skill change is reflected in the example.
