---
description: Design rigorous surveys — question wording, scales, ordering, validation, pilot plan
argument-hint: <topic, construct, or draft survey>
---

Invoke the `survey-design` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/survey-design/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Frame the project (goal, constructs, population, mode, target N).
- Phase 2: Search for validated instruments first — use them rather than inventing when they fit.
- Phase 3: Question construction with the item-writing checklist; flag pitfalls (double-barreled, leading, etc.).
- Phase 4: Survey structure and ordering; demographic items handled with care.
- Phase 5: Length and burden estimate.
- Phase 6: Pilot plan (cognitive interviews + quant pilot).
- Phase 7: Translation if multilingual.
- Phase 8: Output `survey_<topic>.md`.

Push back on long surveys. Recommend passive measurement when appropriate.

User input:
$ARGUMENTS

If no topic or draft was given, ask what they're trying to measure and who the population is.
