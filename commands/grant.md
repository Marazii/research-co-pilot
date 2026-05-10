---
description: Draft grant-proposal sections (NSF, NIH, ERC, Wellcome, Horizon Europe, foundations)
argument-hint: <funder + scheme + topic; optional paths to brainstorm / methodology / prior aims>
---

Invoke the `grant-writer` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/grant-writer/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (funder, scheme, stage, inputs, sections needed, deadline).
- Phase 2: Apply the funder-specific cheat sheet (NIH R01/R21/F31/K, NSF / CAREER, ERC, Wellcome, Horizon Europe, NSF GRFP, foundations).
- Phase 3: Section drafting (Specific Aims / Project Summary, Significance, Innovation, Approach, Broader Impacts, DMP, Lay Summary, Budget Justification, Biosketch, resubmission Introduction).
- Phase 4: Output `grant_<funder>_<section>.md` with fit-check note and `[CITATION NEEDED] / [PRELIMINARY DATA NEEDED] / [REVIEWER CONCERN UNADDRESSED]` index.
- Phase 5: Self-audit (criteria addressed, no overpromise, page limits, lay summary at appropriate level).

If the project doesn't fit the funder/scheme honestly, say so before drafting.

User input:
$ARGUMENTS

If no funder or scheme was given, ask which funder + scheme, the project topic, and what inputs (brainstorm output, methodology, preliminary data) are available.
