---
description: Clean, analyze, model, and visualize quantitative data — Python or R, with reproducible scripts
argument-hint: <dataset path or analysis question>
---

Invoke the `data-analysis` skill from the **research-mentor** plugin and execute its full workflow.

The skill file is at `skills/data-analysis/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Frame the question (descriptive / inferential / predictive / causal).
- Phase 2-3: Load, inspect, clean — show output to user before transforming.
- Phase 4: EDA before modeling.
- Phase 5-6: Baseline model first; check assumptions; report with effect sizes and CIs.
- Phase 7-8: Visualize and produce `analysis_<topic>.md` + reproducible script.

For heavy computation, delegate to the `data-cruncher` subagent.

User input:
$ARGUMENTS

If no dataset path or question was given, ask where the data lives and what question to answer.
