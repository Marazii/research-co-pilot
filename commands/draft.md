---
description: Draft long-form manuscript sections from methodology + analysis outputs
argument-hint: <section name + paths to inputs (methodology, analysis, lit-review, bibliography)>
---

Invoke the `manuscript-drafter` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/manuscript-drafter/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (sections needed, target journal, word budget, inputs).
- Phase 2: Decide structure (IMRaD, mixed methods, qualitative, theoretical, methods, systematic review, humanities).
- Phase 3: Section drafting (abstract, intro, related work, methods, results, discussion, limitations, conclusion).
- Phase 4: Citations — only from the user's bibliography; flag missing as `[CITATION NEEDED]`.
- Phase 5: Output to `manuscript_<section>_<topic>.md` (or to user-specified path).
- Phase 6: Self-audit — every numerical claim and theme traces back to inputs; word counts within target.

For drafts longer than ~3000 words, delegate to the `manuscript-drafter` subagent.

User input:
$ARGUMENTS

If no inputs were given, ask which section(s), what target journal/format, and the paths to methodology / analysis / lit-review / bibliography.
