# methodology-advisor

> Quant + qual research-design advisor. Picks the right design for the question, justifies sample sizes, anticipates threats to validity, plans pre-registration, and — mandatory — forces creative AI / ML / Big Data extensions for every project.

**Triggered by:** `/methodology`, plus phrases like *"what method should I use?"*, *"RCT vs quasi-experiment"*, *"what sample size do I need?"*, *"how do I sample for…"*, *"validity threats for…"*, *"pre-register my study"*, *"AI methods for my study"*, *"ML approach"*, *"big data approach"*.

**Inputs needed:**

- A research question (phrased as a question, not a topic).
- Question type (descriptive / exploratory / explanatory / predictive / evaluative / interpretive — or the skill diagnoses it).
- Unit of analysis (individuals / groups / texts / time points).
- Available data type (primary / secondary / both).
- Constraints (time, budget, access, your own skills).
- Stakes (dissertation / publication / internal report / policy).

**Output:**

- `methodology_<study>.md` with sections: Research Question / Paradigm / Design / Setting & Participants / Data Collection / Analysis Plan / **Creative AI / ML / Big Data Extensions (mandatory)** / Ethics / Threats to Validity / Researcher Positionality / Pre-registration / Limitations.
- The Creative AI / ML / Big Data section is the distinguishing feature: at least 5 candidate extensions across 5 buckets (new data sources, predictive ML, NLP / CV / multimodal, causal ML, generative & simulation) + one ambitious "stretch" idea, each assessed for fit, data needs, skills, validation plan, ethical concerns, and reasons to reject.

**Introduced in:** [v0.1.0](../../CHANGELOG.md). The mandatory creative-methods section was added in [v0.3.0](../../CHANGELOG.md#030--2026-05-10).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you have a research question but aren't yet sure what design fits, when you've committed to a design and want pressure-testing before the design is locked in, when responding to a reviewer asking for "more methodological rigor," or when you want to be pushed past the conventional method just because it's what you know. Particularly valuable for graduate students who haven't yet seen the full design space, and for senior researchers in fast-moving fields where new methods (causal ML, computational text analysis, passive sensor data) might reframe a familiar question.

It is not a substitute for a methodologist colleague — but it surfaces the option space, asks the questions a thesis committee would ask, and refuses to bless designs that don't fit their questions.

## Example

**Input:** *"My question: 'Does feedback intensity in online communities predict member retention?' I have access to platform log data (anonymized) for ~50,000 users over 24 months. Constraint: must be defensible in a quant-focused information-systems department. Stakes: dissertation chapter."*

**Output:** `methodology_feedback_retention.md` covering:

1. Question is **predictive + causal blend** → primary design is longitudinal panel with an identification strategy.
2. Identification recommendation: difference-in-differences exploiting a feature rollout that changed feedback intensity, with regression-discontinuity backup if a threshold exists.
3. Sample-size justification using prior platform-data effect sizes; pre-registration template for OSF.
4. Threats to validity (selection, attrition, regression to mean) named explicitly with mitigations.
5. **Creative AI / ML / Big Data Extensions table** with 5+ candidates: causal forests for heterogeneous treatment effects, NLP-based feedback-content classification (BERTopic), survival analysis as alternative outcome operationalization, agent-based simulation as theory test, and a "stretch": pre-register the question as a Many-Labs-style replication challenge across platforms.

See [`examples/methodology-advisor/`](../../examples/methodology-advisor/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`literature-review`** — Use literature-review's "Gaps and open questions" section as input here. Methodology-advisor designs the study that closes one of those gaps.
- **`ethics-committee`** — Hand the methodology output to the ethics-committee skill for a pre-IRB audit before submitting.
- **`data-analysis`** — The Analysis Plan section feeds directly into data-analysis when the data arrives.
- **`research-brainstorm`** — Brainstorm 15-25 candidate questions first; pick the strongest 1-3; methodology-advisor designs studies around them.

## Honest caveats

- The mandatory creative-methods section will sometimes generate AI / ML / Big Data options that don't actually fit your study. That's expected — the rule is to consider and reject explicitly, not to adopt. The skill names which extensions to skip and why.
- For tradition-specific quantitative methods (psychometrics, time-series econometrics, network science), the skill provides a defensible default but is not as deep as a domain methodologist. Treat its output as a strong starting point you'd review with a specialist.
- It cannot tell you whether your IRB will exempt or accelerate-review your protocol — see the `ethics-committee` skill for that audit.
- It does not run G*Power or simulate power numerically. Power calculations are scaffolded conceptually with software pointers; you (or `data-analysis`) run the actual numbers.
