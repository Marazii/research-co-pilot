---
description: Design a direct, conceptual, or generalization replication of an existing study
argument-hint: <paper to replicate (path / DOI / citation) + replication intent>
---

Invoke the `replication-designer` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/replication-designer/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (target study, replication type — direct / close / conceptual / generalization / robustness — constraints, goal).
- Phase 2: Extract the original design into a structured spec.
- Phase 3: Decide what to hold equivalent vs update; document each deviation.
- Phase 4: Sample size for adequate replication power (often 2-3x the original).
- Phase 5: Pre-registration plan (OSF, AsPredicted, ClinicalTrials.gov).
- Phase 6: Multi-site logistics if applicable.
- Phase 7: Pre-specify replication-success criterion (significance + effect-size CI overlap + meta-analytic synthesis + equivalence test).
- Phase 8: Output `replication_design_<short_title>.md`.

Frame as "estimate the effect honestly," not "prove it wrong."

User input:
$ARGUMENTS

If no target study was given, ask for the citation / DOI / path to the paper and the replication intent.
