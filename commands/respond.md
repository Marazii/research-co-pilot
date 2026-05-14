---
description: Draft a rigorous, polite, point-by-point response to reviewer comments (R1 / R2 / R3) plus the matching manuscript revisions
argument-hint: <path to reviewer comments + manuscript path + (optional) prior response>
---

Invoke the `reviewer-response` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/reviewer-response/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (reviewer comments, manuscript, round number, journal, posture).
- Phase 2: Categorize every comment (concession + revision / partial concession / polite pushback / clarification / out of scope / minor).
- Phase 3: Draft response per comment with verbatim reviewer quote, substantive response, and revision pointer.
- Phase 4: Draft prose revisions (delegate to `manuscript-drafter` for anything > one paragraph to preserve voice).
- Phase 5: Cover letter to editor (under one page; surface pushback up front).
- Phase 6: Assemble package — `response_to_reviewers_<round>/` directory with cover letter, response, revised manuscript, tracked-changes version if needed, change log.
- Phase 7: Self-audit — every comment addressed; every claimed revision actually present; tone polite throughout; voice matches existing manuscript.

Address every reviewer point. Never concede a point the data doesn't support. Be unfailingly polite even when pushing back.

User input:
$ARGUMENTS

If no inputs were given, ask for: path to reviewer comments (one file or multiple), path to the manuscript, round number (R1 / R2 / R3), journal name, and (if R2 or later) the path to the prior response letter.
