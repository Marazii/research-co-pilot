---
description: Format citations and bibliographies in any major academic style; convert between styles; build BibTeX
argument-hint: <citations, paths, or "fix references in <file>">
---

Invoke the `citation-formatter` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/citation-formatter/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Determine style, output type, source material, edition.
- Phase 2-3: Use cheat sheets for the requested style; verify DOIs and metadata.
- Phase 4: Handle edge cases (preprints, datasets, software, AI-generated content, social media).
- Phase 5: Build BibTeX/RIS if requested.
- Phase 6: Document-wide consistency check if working on a manuscript.
- Phase 7: Output to `references.md` (or in-place edit) and report verification gaps.

Never invent a missing field. If something can't be verified, say so.

User input:
$ARGUMENTS

If no citations or file path were given, ask what needs formatting and which style to use.
