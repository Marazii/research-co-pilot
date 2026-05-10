---
description: Turn a paper (or several) into an academic talk — outline, slides, speaker notes, backups, rehearsal plan
argument-hint: <paper path(s) + length in min + venue + audience>
---

Invoke the `talk-builder` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/talk-builder/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (paper, length, format, venue, audience, your role, slide platform, constraints).
- Phase 2: Pick the structure (length × audience × discipline scaffolds; format-specific moves).
- Phase 3: Storyboard the arc as a sequence of beats with timing.
- Phase 4: Per-slide content (visual, on-slide text, speaker notes, anticipated reaction, transition).
- Phase 5: Opening hook (60 seconds).
- Phase 6: Take-home and closing (one-sentence take-home).
- Phase 7: Backup slides for the 3-5 most-anticipated questions.
- Phase 8: Speaker notes and rehearsal plan.
- Phase 9: Output `talk_<short_title>_<minutes>min.md` (plus optional Marp / Quarto / reveal.js / Beamer stub).
- Phase 10: Self-audit (timing, take-home, one-idea-per-slide, accessibility).

The paper is not the talk. Cut to fit the time. Frame for the audience.

User input:
$ARGUMENTS

If no paper / length / venue were given, ask for: path to the paper, talk length in minutes (and whether Q&A is included), venue + format (contributed / lightning / invited / plenary / keynote / defense / job talk / public lecture / course lecture), audience description, and your role.
