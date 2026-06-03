# research-brainstorm

> Generates and pressure-tests 15–25 research ideas, scores them, sharpens the top 3 into study sketches. Pushes past the obvious next study.

**Triggered by:** `/brainstorm`, plus *"what should I study?"*, *"brainstorm research ideas"*, *"thesis topic ideas"*, *"novel angles on…"*, *"I'm stuck on what to research"*, *"contrarian framings"*.

**Inputs needed:**

- A starting point — a topic, a vague intuition, an existing dataset, a problem you've encountered, a paper that bugged you.
- Your stage — picking a thesis topic / finding the next study after a published one / designing a new project / looking for a paper to write.
- Constraints — discipline, methods you can use, data you can access, timeline.
- The contribution type you want — empirical / theoretical / methodological / critical / applied.

**Output:**

- `brainstorm_<topic>.md` with: landscape summary / long list (15-25 candidates) / scored top candidates (interesting × answerable × novel × feasible) / sharpened top 3 with full study sketches (research question, why it matters, what's known, gap, possible design, predicted finding + the contrary, risks, adjacent follow-on ideas).

**Introduced in:** [v0.1.0](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when picking a thesis topic, when finding the next study after a published one (the "what now?" moment), when you're stuck on what to study, when you want to be pushed past the obvious follow-up your last paper implied, or when you're looking for a paper-shaped idea to commit to. Particularly useful for graduate students two years in who feel they've exhausted the obvious questions.

It's not a substitute for sustained reading in your field — but it surfaces variation in question-form, cross-field grafts, and contrarian framings that researchers often miss because they've internalized the field's defaults.

## Example

**Input:** *"I work on misinformation and trust in news, broadly. I have access to panel survey data and can run online experiments. Constraint: must be defensible in a quant-focused department. Stage: second-year PhD, looking for dissertation chapter 2."*

**Output:** `brainstorm_misinfo_trust.md` with 19 candidate questions across descriptive, causal, predictive, evaluative, mechanistic, comparative, critical, constructive, and methodological framings — including cross-field grafts (behavioral economics → news trust; network analysis → information cascades), contrarian moves (what if the dominant correction-effectiveness finding is wrong under condition X), and question-behind-the-question reframings. Scored on interesting × answerable × novel × feasible. Top 3 sharpened into full study sketches with predicted findings, devil's-advocate paragraphs naming why each might already exist or might be undoable, and follow-on study chains.

See [`examples/research-brainstorm/`](../../examples/research-brainstorm/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`literature-review`** — Run brainstorm first to identify candidate questions; run literature-review on the top 1-2 to verify novelty before committing.
- **`methodology-advisor`** — Once a question is chosen, methodology-advisor designs the study.
- **`grant-writer`** — A brainstorm output shapes the Specific Aims for a grant proposal.

## Honest caveats

- The skill optimizes for variety, not for "the right answer." A 25-idea long list is meant to surface options; converging on one is your job.
- It may surface ideas that are infeasible for your specific constraints — the scoring helps but doesn't fully filter. The devil's-advocate paragraphs are where infeasibility usually surfaces.
- It does not check whether an idea has already been published — that's the next step (literature-review on the top candidates).
- For purely theoretical work (math, philosophy, theoretical physics) the skill's question-form variations are less applicable; it still works but its sweet spot is empirical research.
