---
description: Brainstorm and pressure-test research ideas, questions, and angles
argument-hint: <topic, field, or rough idea>
---

Invoke the `research-brainstorm` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/research-brainstorm/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Locate the user (starting point, stage, constraints).
- Phase 2: Map the territory briefly.
- Phase 3: Generate 15-25 ideas using question-form variations, cross-field grafts, contrarian moves.
- Phase 4: Score on interesting / answerable / novel / feasible.
- Phase 5: Sharpen the top 3 into full sketches with predicted findings, risks, follow-ups.
- Phase 6: Output `brainstorm_<topic>.md`.

Resist converging too early. Don't filter for politeness.

User input:
$ARGUMENTS

If no starting point was given, ask for a topic, intuition, or constraint to anchor the brainstorm.
