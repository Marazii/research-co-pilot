# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/Marazii/research-co-pilot/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/Marazii/research-co-pilot/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/Marazii/research-co-pilot/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/Marazii/research-co-pilot/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Marazii/research-co-pilot/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Marazii/research-co-pilot/releases/tag/v0.1.0
