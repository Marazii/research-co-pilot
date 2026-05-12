# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/Marazii/research-co-pilot/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/Marazii/research-co-pilot/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/Marazii/research-co-pilot/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/Marazii/research-co-pilot/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/Marazii/research-co-pilot/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/Marazii/research-co-pilot/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Marazii/research-co-pilot/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Marazii/research-co-pilot/releases/tag/v0.1.0
