---
description: Code qualitative transcripts, build codebooks, identify themes, and run NLP-assisted exploration
argument-hint: <path to transcripts or research question>
---

Invoke the `qualitative-coding` skill from the **research-mentor** plugin and execute its full workflow.

The skill file is at `skills/qualitative-coding/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1-2: Diagnose the project, prepare the corpus (anonymize, standardize).
- Phase 3-5: Choose tradition (thematic, grounded theory, IPA, framework, content), build codebook, code.
- Phase 6: Inter-rater reliability where applicable.
- Phase 7: Theme development and final report.
- Phase 8: NLP-assisted exploration for large corpora — always validate against hand-coding.

For corpora with many files, delegate to the `transcript-coder` subagent for cleaning and batch coding.

User input:
$ARGUMENTS

If no transcripts/question were given, ask what data they have and what tradition / question is driving the analysis.
