# replication-designer

> Designs direct, conceptual, generalization, or robustness replications of an existing study. Extracts the original spec, justifies every deviation, computes adequate replication power, pre-registers, and pre-specifies replication-success criteria. Supports multi-site logistics for Many-Labs-style work.

**Triggered by:** `/replicate`, plus *"replicate this study"*, *"replication design"*, *"registered replication"*, *"many-labs"*, *"is this finding robust"*, *"direct replication"*, *"conceptual replication"*, *"preregistered replication"*, *"replication power"*.

**Inputs needed:**

- The target study (citation, DOI, or path to the paper PDF).
- Replication intent: direct / close / conceptual / generalization / robustness.
- Why this study (influential / controversial / central to your work / foundational).
- Constraints (sample access, budget, time, single-site vs multi-site, IRB).
- Goal (independent publication / Registered Replication Report / meta-analysis / multi-lab consortium).

**Output:**

- `replication_design_<short_title>.md` with: original-study structured spec / replication intent / design-comparison table (every deviation justified) / sample-size + power calculation / materials sourcing / procedure / analysis plan with pre-specified primary test + equivalence test (TOST) + Bayesian framing if applicable / pre-registration plan (OSF / AsPredicted / ClinicalTrials.gov) / multi-site logistics if applicable / replication-success criterion / ethics summary / communication plan with original authors / timeline / dissemination plan.

**Introduced in:** [v0.2.0](../../CHANGELOG.md#020--2026-05-10).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you want to test the robustness of a published finding that matters to your own work, when participating in a Many-Labs-style consortium replication, when a foundational claim in your subfield is starting to look fragile and you want to estimate the effect honestly, when designing a registered-replication-report submission, or when adding a robustness component to a planned study.

It frames replication as "estimate the effect honestly" — not "prove the original wrong." That framing matters: replications designed as gotchas are weaker science than replications designed as fair tests.

## Example

**Input:** *"Replicate Smith et al. 2018 (J. Psychology, N=89, Cohen's d=0.45, attention-context effect on word recall). Direct replication. Single-site, my university subject pool. ~$2000 budget. Goal: independent publication."*

**Output:** `replication_design_smith2018_attention_recall.md` covering:

1. **Original spec** — design, IV/DV operationalizations, materials availability, original N and effect size, alpha, primary test.
2. **Design comparison table** — what stays equivalent (population type, stimuli, procedure), what unavoidably differs (year of data collection, university subject pool composition), each deviation justified.
3. **Sample size for adequate replication power.** If trusting the original d=0.45, need N≈86 per group for 90% power at α=.05; if planning for inflated effect (50% of original), N≈220 per group — recommend the latter as defensible.
4. **Pre-registration plan on OSF** with primary test, alpha, stopping rule, secondary analyses labeled as such, TOST equivalence bounds (smallest effect of interest = d=0.20).
5. **Replication-success criterion** pre-specified: significance + effect-size CI overlap + meta-analytic synthesis with the original.
6. **Communication with original authors** — draft email inviting protocol review.
7. **Timeline + dissemination** including OSF deposit and journal targets that accept replications.

See [`examples/replication-designer/`](../../examples/replication-designer/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`methodology-advisor`** — Replication-designer adopts most of the original methodology; methodology-advisor pressure-tests deviations.
- **`ethics-committee`** — Replications often re-trigger ethics review even when the original was approved. Run ethics-committee on the replication protocol.
- **`grant-writer`** — Replication funding (Templeton, Sloan, agency replication tracks) benefits from grant-writer drafting the proposal.
- **`data-analysis`** — Once data is collected, data-analysis runs the pre-specified primary test, equivalence test, and meta-analytic synthesis with the original.

## Honest caveats

- **Replication design is collaborative when feasible.** The skill's "communication with original authors" phase is non-optional — pre-registered direct replications gain credibility when original authors have reviewed the protocol.
- **Sample-size rules of thumb** (2-3× original N for inflated-effect adjustment) are defensible defaults; field-specific norms differ.
- **Materials availability** is often the limiting factor for direct replications. The skill notes when stimuli aren't publicly available and proposes paths (contact authors / construct equivalent + flag as deviation).
- **Multi-site consortium logistics** (Many-Labs style) are scaffolded but require human coordination beyond what any skill can do.
- **Conceptual replications** are interpretively harder than direct ones — when results differ, attributing the difference to construct vs. operationalization vs. population is non-trivial. The skill's "what we hope to learn" framing helps but doesn't resolve this.
