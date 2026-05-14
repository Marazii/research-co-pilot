# literature-review

> Fact-checked academic literature reviews. Synthesizes sources, traces citation chains, flags weak claims, and refuses to fabricate citations.

**Triggered by:** `/lit-review`, plus phrases like *"do a lit review on…"*, *"what does the research say about…"*, *"summarize the literature on…"*, *"find sources on…"*, *"systematic review on…"*, *"background research on…"*.

**Inputs needed:**

- A research question or topic (specific is better than broad).
- Optionally: source PDFs, BibTeX exports, a starter bibliography, prior reviews. User-provided sources take priority over web search.
- The review type if you have a preference: narrative, systematic, scoping, rapid, or thematic. Otherwise the skill asks.

**Output:**

- `lit_review_<topic_slug>.md` written to your working directory (Claude Code) or rendered as a downloadable artifact (claude.ai).
- Structure: research question → methods (if systematic) → synthesis organized by **idea**, not by source → methodological landscape → gaps & open questions → references → appendix source-appraisal table.
- Each claim tagged `[strong]` / `[mixed]` / `[weak]` based on the evidence supporting it.

**Introduced in:** [v0.1.0](../../CHANGELOG.md) — part of the initial release.

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill at the start of a research project, when responding to a reviewer who asked for a "more thorough literature review," when writing a thesis background chapter, or when you suspect the field is more contested than the textbooks let on. It's most valuable when (a) you have at least some seed sources or a focused question — it does better with constraints than with "tell me everything about consciousness," and (b) you care more about defensible synthesis than rapid summary.

It is not a substitute for a librarian's database search, and the skill itself flags the difference. For systematic reviews requiring PRISMA-compliant transparency, treat the output as a structured first pass that you (with your librarian) refine.

## Example

**Input:** *"Do a thematic literature review on the effect of remote work on early-career mentorship in knowledge industries. Time range: 2018-2026. I have 4 starter sources in `./sources/`."*

**Output:** `lit_review_remote_work_mentorship.md` with sections covering:

1. The pre-pandemic mentorship literature (sponsorship vs. mentorship, weak ties, proximity effects).
2. Empirical findings from the 2020-2023 remote-work natural experiment.
3. Conflicting accounts (some studies report mentorship resilience, others report sharp decline by career stage and gender).
4. Methodological landscape (survey-dominated; few longitudinal designs; almost no field experiments).
5. Specific gaps — not "more research is needed" but "no study has yet examined hybrid-by-default cohorts longitudinally, controlling for prior network density."

The synthesis is organized by *idea*, not by source: each section cites multiple supporting studies, names where they disagree, and marks confidence. Every citation is verified before it lands in the document — fabrications are refused.

See [`examples/literature-review/`](../../examples/literature-review/) for the full input/output sample.

## Composes well with

- **`methodology-advisor`** — A good lit review identifies the gap; methodology-advisor designs the study that closes it. Feed the lit-review output into methodology-advisor as input.
- **`manuscript-drafter`** — The lit-review output becomes the related-work / introduction draft. Manuscript-drafter pulls forward the synthesis and cites only from the verified bibliography.
- **`source-finder` subagent** — For reviews with many candidate sources (more than ~5-10), the parent skill spawns the source-finder subagent to read in parallel and return structured digests.
- **`peer-review`** — When reviewing someone else's lit review, peer-review can fact-check the synthesis against actual source content.

## Honest caveats

- **Paywalled sources** that the model can't access are flagged with their citation but the synthesis around them is necessarily based on abstracts. The output notes which sources are abstract-only.
- **Non-English literatures** receive less coverage than English ones, especially for languages with limited web indexing. Provide sources directly if you're working in a less-resourced literature.
- **Predatory or low-quality outlets** are flagged but not always definitively — quality appraisal is one heuristic input, not a verdict. The user still reviews the final source list.
- **Living literatures (LLMs, COVID, etc.)** can produce reviews that are dated within months. The skill notes its search date and recommends re-running before publication.
- This skill does not replace a database search via PubMed / Web of Science / Scopus. Treat it as complementary.
