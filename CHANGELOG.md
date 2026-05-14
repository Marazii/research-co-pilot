# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.0] — 2026-05-12

### Changed (substantial overhaul of `manuscript-drafter`)

Based on direct feedback from a senior reviewer who used `manuscript-drafter` to extend a Discussion chapter in Hebrew. The output had value (good ideas, kept existing prose, followed standard structure) but real craft problems (too long, non-academic register, voice mismatch, new methodological ideas not grounded in literature). v0.8.0 addresses each of those problems explicitly.

**F1 — Voice preservation.** New Hard rule 7 plus new **Phase 3 — Extract the manuscript's voice profile (mandatory)** that runs *before* any new drafting. Voice signature captured: sentence length, person/voice, hedge intensity, signature phrases (5+ verbatim), connectors, citation density/style, paragraph length, punctuation habits. Hebrew-specific markers (register tier, gendered forms, classical-vs-contemporary syntax). Voice profile rendered at the top of the working draft and applied to every new paragraph.

**F2 — Length discipline.** New Hard rule 8 plus explicit per-section budgets in Phase 2 (Abstract 150-250; Introduction 800-1500, cap 2000; Related work 1500-2500, cap 3000; Methods 1000-2000, cap 2500; Results 1000-2000, cap 2500; Discussion 1000-1800, cap 2200; Limitations 200-500, cap 600; Conclusion 150-400, cap 500). Defaults to the *low* end of each range. New **Phase 7 Pass C — Compression to budget** runs after first draft and logs every cut.

**F3 — Academic register.** New Hard rule 9 with explicit banned-pattern table (colloquialisms, conversational openers, hedge softeners, vague quantifiers, clichés, contractions, overused sentence-initial interjections). New **Phase 7 Pass D — Register audit** scans the draft for every banned pattern with a replacement table. Hebrew-specific substitutions ("בעצם", "סוג של", "די הרבה", "פשוט", colloquial verbs) included.

**F4 — Literature integration for new ideas.** New Hard rule 10 plus new **Phase 5 — Literature integration for new content**. Distinguishes `[CITATION NEEDED]` (known claim, source presumed to exist but missing from bibliography) from a new `[LITERATURE NEEDED — claim / search terms / likely body of work]` marker for skill-introduced new ideas needing grounding in scholarship. No silent additions.

**F5 — Two-pass ideation → prose workflow.** Restructured Phase 4 into Sub-pass A (ideation outline with `[PULLED] / [RESTRUCTURED] / [NEW]` tags, shown to user before drafting) and Sub-pass B (drafting pass applying voice profile + register rules). Separates the strong part of the skill (ideation) from the weaker part (prose execution) and makes ideation explicitly reviewable.

**F6 — Language-aware behavior.** New Hard rule 11: draft in the language of the existing manuscript. Hebrew → Hebrew academic register; English → English. Voice profile and register rules adapted for the detected language. Auto-detect from manuscript; no explicit flag.

**Phase 7 — Multi-pass refinement (new)** runs after the first prose pass: Compression (Pass C) → Register audit (Pass D) → Voice consistency check (Pass E, comparing random new vs existing paragraphs).

**Phase 8 — Output** expanded to include voice profile, ideation outline, `[CITATION NEEDED]` index, `[LITERATURE NEEDED]` index, source map, word-count-vs-cap table, content-cut-for-length log, register-audit log, voice-consistency-check log.

**Phase 9 — Self-audit** expanded with: voice-profile match check, word-budget compliance, register-audit cleanliness, every-`[NEW]`-grounded-or-marked, language match, Hebrew-specific checks.

### Notes for upgraders
- The skill now insists on an existing manuscript draft for voice extraction. If none is provided, the skill asks once and flags prominently that voice preservation cannot be enforced.
- Output documents are longer (now include voice profile, ideation outline, registers and logs) but the drafted prose itself is shorter and tighter.
- Hebrew users: register substitutions and gendered-form matching are now first-class concerns.

### Deferred to v0.9.0
- Same rigor pass for `grant-writer` (shares the long-form / register / length risks). Will be done after v0.8.0 is tested in real use.

## [0.7.0] — 2026-05-12

### Added
- `peer-review`: **PDF annotation support.** Submits a `.pdf` and gets back `_REVIEWED.pdf` with sticky-note comments anchored at the exact text location via PyMuPDF's `page.search_for` + `add_highlight_annot` / `add_text_annot` / `add_strikeout_annot`. Works in any PDF reader (Acrobat, Preview, browsers). Annotations carry the "Reviewer" author tag so they're filterable in Acrobat / Preview.
- `peer-review`: **LaTeX annotation support.** Submits a `.tex` and gets back `_REVIEWED.tex` with `% REVIEWER:` line comments immediately above the relevant line. Optional `--latex-changes` flag for `changes`-package markup (`\added`, `\deleted`, `\replaced`) for tracked-change-style edits. Also handles `.bib` files.
- `peer-review`: Restructured Step 6 (Annotate the source document) to cover all four supported formats explicitly — `.docx`, `.pdf`, `.pptx`, `.tex` — with a per-format mechanics subsection for each, plus a fallback section for other formats (Markdown, RTF, HTML, ODT, Pages, Google Docs, Jupyter, plain text) which produce a structured review only.
- `peer-review`: New hard rule on anchoring: every inline annotation must attach at the location it refers to (specific text span, highlighted rectangle, specific shape, line above the relevant code). Bulk-appending all comments at the end of the document is not acceptable. Anchoring failures must fall back to the nearest possible anchor with the imprecision noted in the comment body — never silently dropped.

### Changed (breaking for users on v0.5.0–v0.6.0)
- `peer-review` PPTX annotation: **switched from "append to speaker notes" default to "native PowerPoint comments anchored to slides / shapes."** Native comments appear in PowerPoint's Review pane (and Keynote / Google Slides comment threads), where reviewers expect them — the same mechanism PowerPoint's "New Comment" button uses. The speaker-notes-append behavior introduced in v0.5.0 was a workaround; this is the right mechanism. Comments are anchored to specific shapes where possible, with slide-level fallback for findings that aren't shape-specific. Author tag "Reviewer" lets users filter by author in the Review pane.
- `peer-review` frontmatter description refreshed to advertise all four format outputs explicitly.
- README peer-review row updated.

### Notes for upgraders
- Re-running an old PPTX review on v0.7.0 will produce a different output file: native comments instead of speaker-notes appendices. Old speaker-notes annotations from prior runs are unaffected (they live in the file, not the skill).
- PDF and LaTeX support auto-install required libraries (`pymupdf`, `lxml`) on first use; no manual setup required.

## [0.6.0] — 2026-05-12

### Changed
- `manuscript-drafter`: substantial fix based on user feedback from Maya's professor. The skill was strong on ideation and structure but weak on writing craft — too long, insufficiently academic register, didn't preserve the existing manuscript's voice, and added new methodological ideas without grounding them in literature.

### Added (in `manuscript-drafter`)
- **Phase 3 — Voice profile extraction (mandatory).** Before any drafting, the skill reads existing manuscript prose and records a voice signature: sentence length, person/voice, hedge intensity, signature phrases (verbatim examples), connectors, citation density and style, paragraph length, punctuation habits. For Hebrew manuscripts: register tier (classical / contemporary), gendered forms, classical vs. modern syntax. The profile is applied to every new paragraph.
- **Phase 4 restructure — two sub-passes.** Sub-pass A: ideation outline with every item tagged `[PULLED]` / `[RESTRUCTURED]` / `[NEW]`, shown to the user before any prose is written. Sub-pass B: draft each idea as academic prose using the voice profile. This separates the strong part of the skill (ideation) from the weaker part (prose), and makes both reviewable.
- **Phase 5 — Literature integration for new content (mandatory for every `[NEW]` item).** Skill must search the user's bibliography and lit-review for sources that ground, extend, or contradict the new claim. If sources exist, embed them with framing. If none exist, emit `[LITERATURE NEEDED — claim: "..."; suggested search: <keywords>; likely body of work: <area>]` — never silent. Distinguishes `[CITATION NEEDED]` (known claim, source missing) from `[LITERATURE NEEDED]` (skill-introduced new idea needing grounding).
- **Phase 7 — Multi-pass refinement.** Pass C: compression to per-section word-budget cap (deliberate prioritization, cut content logged separately). Pass D: register audit (scan + replace banned colloquialisms, conversational openers, vague quantifiers, hedge softeners, clichés, and contractions — with Hebrew-specific variants). Pass E: voice consistency check (compare random new vs. existing paragraph; ask "would a careful reader notice they're by different authors?" and revise if yes).
- **Per-section word budgets as hard caps**: Introduction 800-1500 (cap 2000), Discussion 1000-1800 (cap 2200), etc. Defaults to the low end of each range. Cut content is logged under "Content cut for length (consider for appendix or separate paper)" — never silently dropped.
- **Language-aware drafting.** Hard rule: draft in the language of the existing manuscript. Hebrew-specific register guidance for both voice profile and register audit.
- Four new hard rules added (preserve voice / length is hard / academic register / literature-ground new ideas / language matches manuscript), bringing total to 11.
- Expanded self-audit checklist with voice, length, register, language, and literature-grounding checks.

### Maps to user feedback (translated from Hebrew)
1. "Useful for ideas, less for writing" → Phase 4 split + Phase 7 multi-pass refinement.
2. "Used existing content — excellent" → Preserved; ideation outline now tags `[PULLED]` / `[RESTRUCTURED]` so this is visible.
3. "Added new methodological ideas but missing literature links" → New Phase 5 with `[LITERATURE NEEDED]` marker and search guidance.
4. "Used standard article structure — excellent" → Preserved; Phase 2 unchanged.
5. "Writes too long" → Hard per-section word-budget caps + Phase 7 Pass C compression.
6. "Not academic enough; everyday expressions slip in" → Hard rule 9 + Phase 7 Pass D register audit with explicit banned-pattern list.
7. "Didn't preserve writing style of the article" → New Phase 3 voice profile + Phase 7 Pass E consistency check.

## [0.5.0] — 2026-05-11

### Added
- `peer-review`: new **`--presentation`** mode for talks and slide decks. Operates on `.pptx` (extracted via `python-pptx`), `.pdf` of slides, Beamer `.tex`, and Marp / Quarto / reveal.js source. Produces:
  - Per-slide commentary (estimated time, content summary, one-idea-per-slide check, visual-first check, concrete suggested fix).
  - Talk-level evaluation (take-home message, opening 60 seconds, arc and pacing, closing, audience fit, discipline / venue match, backup-slide suggestions for Q&A, accessibility).
  - Delivery-readiness verdict register (Ready to deliver / One rehearsal pass needed / Revisions before delivery / Rebuild from outline) — separate from the academic verdict register.
  - For `.pptx` inputs, an annotated `_REVIEWED.pptx` copy with `--- REVIEWER NOTES ---` blocks appended to each slide's speaker notes (portable across PowerPoint, Keynote, Google Slides, LibreOffice Impress).
- Composes with all existing modes: `--presentation --paper`, `--presentation --homework`, `--presentation --committee`, `--presentation --draft`, `--presentation --fact-check`.
- Cross-skill handoff: redirects to `talk-builder` when no slides exist yet.

### Changed
- `peer-review` description trimmed and refreshed: now lists 5 alternative workflows (was 4), mentions both `.docx` and `.pptx` annotation, adds presentation / slide-deck triggers.
- `peer-review` Step 1 (mode identification) updated with the new `presentation` workflow and 4 new composition examples.
- Hard rules and edge cases extended for presentation-specific failure modes (missing context, pure-image slides, vague per-slide commentary, slides-not-yet-built).
- README peer-review row updated to surface the new mode.

## [0.4.1] — 2026-05-10

### Changed
- Plugin and marketplace descriptions reframed from "research assistant" to "research co-pilot" to align with the tool's stated philosophy. The plugin is named `research-co-pilot` because it's a *peer collaborator*, not a subservient assistant or hierarchical mentor — the descriptions now reflect that consistently.
- README opening: "A Claude assistant for the entire research lifecycle" → "A Claude co-pilot for the entire research lifecycle".
- GitHub repo description updated to match.
- Marketplace + plugin descriptions also refreshed to mention `talk-builder`, which shipped in 0.4.0 but wasn't in those descriptions yet.

## [0.4.0] — 2026-05-10

### Added
- New skill `talk-builder` — turns one or more papers into a complete academic talk: outline, per-slide content, speaker notes, opening hook, single take-home message, backup slides for Q&A, rehearsal plan, and accessibility/inclusivity guidance. Adapts to talk length (3-min lightning to 90-min defense), audience, format (contributed / lightning / invited / plenary / keynote / defense / job talk / public lecture / course lecture), and discipline conventions (sciences, social sciences, CS/ML/HCI, medicine, education, humanities, law, math). Produces deck-platform-agnostic outline plus optional Marp / Quarto / reveal.js / Beamer stubs.
- New slash command `/talk`.
- `/research` router updated with the new command and routing keywords.
- README tables and file tree updated.

## [0.3.0] — 2026-05-10

### Added
- `methodology-advisor`: new mandatory **Phase 5 — Creative AI / ML / Big Data extensions**. Every methodology output must now generate at least 5 candidate AI / ML / Big Data extensions across 5 buckets (new data sources, predictive ML, NLP / CV / multimodal, causal ML, generative & simulation), plus one ambitious "stretch" idea — each assessed for fit, data needs, skills, validation, ethical concerns, and reasons to reject. The point is to widen the option space before researchers default to what they know.
- New section `7. Creative AI / ML / Big Data Extensions` in the methodology output template; sections 7-11 renumbered to 8-12.
- Added "always force creative-method consideration" as a second core principle.

### Changed
- `methodology-advisor` description updated to surface the new creative-extensions capability and add trigger phrases ("AI methods for my study", "ML approach", "big data approach", "creative methods").

## [0.2.0] — 2026-05-10

### Added
- New skill `ethics-committee` — IRB / REC / HREC pre-submission stress test, with optional 3-reviewer panel mode.
- New skill `manuscript-drafter` + same-named subagent — drafts long-form manuscript sections from methodology + analysis outputs.
- New skill `grant-writer` — drafts grant-proposal sections (NSF, NIH, ERC, Wellcome, Horizon Europe, foundations).
- New skill `replication-designer` — designs direct, conceptual, or generalization replications of an existing study.
- New subagent `stats-validator` — independent second-look on a colleague's analysis without context contamination.
- New slash commands: `/ethics`, `/draft`, `/grant`, `/replicate`.
- `docs/philosophy.md` — short essay on design choices and the AI failure modes each skill refuses.
- `CHANGELOG.md`, `SECURITY.md`, marketplace `metadata.description`, README badges.

### Changed
- `peer-review` skill `description` trimmed from 1308 to 1013 chars to fit the SKILL.md 1024-char schema limit. All trigger phrases, mode names, language auto-detection, and .docx annotation capability preserved.
- `/research` router updated to know about every new skill (menu + routing logic).
- README: new tables for the additional skills, subagent, and slash commands.

### Fixed
- `dist/peer-review.zip` rebuilt with the corrected description.

## [0.1.0] — 2026-05-09

### Added
- Initial release as `research-mentor`, renamed to `research-co-pilot` on the same day.
- 8 skills: `literature-review`, `methodology-advisor`, `data-analysis`, `qualitative-coding`, `research-brainstorm`, `citation-formatter`, `survey-design`, `peer-review`.
- 3 subagents: `source-finder`, `data-cruncher`, `transcript-coder`.
- 9 slash commands including `/research` as the entry-point router.
- `dist/` upload bundles for claude.ai (one zip per skill).
- `scripts/build-zips.sh` for rebuilding bundles.
- Claude Code marketplace manifest at `.claude-plugin/marketplace.json`.
- MIT License.
- README with install paths for both Claude Code and claude.ai.

[Unreleased]: https://github.com/Marazii/research-co-pilot/compare/v0.8.0...HEAD
[0.8.0]: https://github.com/Marazii/research-co-pilot/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/Marazii/research-co-pilot/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/Marazii/research-co-pilot/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/Marazii/research-co-pilot/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/Marazii/research-co-pilot/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/Marazii/research-co-pilot/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/Marazii/research-co-pilot/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Marazii/research-co-pilot/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Marazii/research-co-pilot/releases/tag/v0.1.0
