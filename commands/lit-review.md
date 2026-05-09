---
description: Conduct a rigorous, fact-checked literature review on a topic
argument-hint: <topic or research question; optional: paths to source PDFs/files>
---

Invoke the `literature-review` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/literature-review/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Scope the review (clarify type, discipline, inclusion criteria, sources at hand).
- Phase 2: Source acquisition — read user-provided files first, then targeted search if allowed.
- Phase 3-4: Critical appraisal and synthesis (organize by idea, not by source).
- Phase 5: Output to `lit_review_<topic>.md` with the specified structure.
- Phase 6: Self-audit checklist.

For >5 sources, delegate parallel reading to the `source-finder` subagent.

User input:
$ARGUMENTS

If no topic was given, ask what to review and what sources/scope are in play.
