---
description: Get advice on quantitative or qualitative research design, sampling, validity, and ethics
argument-hint: <research question or design problem>
---

Invoke the `methodology-advisor` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/methodology-advisor/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Diagnose the question (paradigm, unit of analysis, constraints).
- Phase 2 / 3 / 4: Quant / Qual / Mixed-methods guidance based on what fits.
- Phase 5: Ethics, IRB, pre-registration.
- Phase 6: Produce a `methodology_<study>.md` document with the specified template.

If the user has committed to a design that doesn't fit their question, push back honestly.

User input:
$ARGUMENTS

If no question or design problem was given, ask what they're trying to study and at what stage they are.
