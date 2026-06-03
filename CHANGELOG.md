# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.11.1] — 2026-06-03

**Research vault.** The knowledge layer on top of the v0.11.0 `.research/` workspace. v0.11.0's `manifest.json` *indexes files*; the vault *holds project knowledge* — stated once, read by every skill, with cross-document drift caught automatically. No skill behavior weakened; the vault is opt-in (standalone runs are unchanged).

### Added

- **`docs/research-vault.md`** — the canonical vault spec: structure, the `facts` schema, the seven note formats, the read/update protocol, the flag-on-write rule, the six `/vault audit` checks, the **PII hard rule**, and portability. Sibling to `docs/skill-network.md`.
- **New `vault` skill + `/vault` command** (the project's librarian — infrastructure, not a lifecycle stage). Subcommands: `show` (vault summary), `init` (scaffold the vault), `audit` (the marquee feature — scan every artifact against the vault and report drift), `add` (deposit a fact/decision/citation/question/term/entity), `resolve` (close an open question). Includes `skills/vault/README.md`.
- **The vault itself** — `.research/vault/` with seven markdown notes (`facts.md`, `bibliography.md`, `decisions.md`, `open-questions.md`, `glossary.md`, `voice-profile.md`, `entities.md`) plus a structured `facts` block + `vault` registry in `manifest.json`. Markdown-first hybrid: human-readable notes + typed facts the audit diffs against.
- **`/vault audit` — drift detection.** Six checks with 🔴/🟡/🟢 severity: fact consistency (the abstract-says-240-but-methods-say-247 class), citation consistency (every cite resolves to the canonical bibliography; no unresolved `[… NEEDED]` at pre-submission), terminology drift vs the glossary, unresolved open questions, staleness, and **PII safety** (scans for accidental real-name PII and flags it).
- **Canonical bibliography.** `bibliography.md` is now the single source of truth for citations: `literature-review` seeds it, `manuscript-drafter` / `grant-writer` / `reviewer-response` cite *by cite-key*, and `citation-formatter` renders any style *from it* rather than a parallel list — killing citation drift and re-fabrication.
- **Reusable voice profile.** `manuscript-drafter` writes `voice-profile.md` once; `talk-builder`, `grant-writer`, and `reviewer-response` now read it so everything sounds like the same author.

### Changed

- All 14 existing skills gained a **`Vault`** block in their `## Handoffs` section — what each reads from the vault at intake and updates at output, plus per-skill flag-on-write rules. Highlights: `data-analysis` records the post-exclusion N as a *distinct* fact (never overwriting the recruited N) and stops if a number would contradict the vault without explanation; `methodology-advisor` / `ethics-committee` deposit the anchor facts (sample size, pre-reg, IRB#); `qualitative-coding` deposits participant *pseudonyms only* (real-name key stays off-system).
- **`docs/skill-network.md`** — manifest schema gains the `facts` + `vault` blocks; the intake/output protocol gains "read the vault / update the vault" with the flag-on-write rule.
- **`/research` conductor** — initializes the vault at project start, runs a **`/vault audit` gate before the pre-submission stage** (catch drift before the paper goes out), and reads key facts + vault counts into the pipeline status report. `/vault` added to the router menu + routing keywords.
- README — new "research vault" paragraph in "How the skills work together", a `vault` row in the skills table, and the vault in the file tree.

### Design rules (held throughout)

- **The vault never holds PII.** Pseudonyms + non-identifying attributes only; the real-name key stays off-system; `/vault audit` actively scans for accidental PII.
- **Files are the source of truth; the vault is reconciled** at intake and by the audit — it never invents an artifact's contents.
- **Distinct facts, not overwrites.** Legitimately-different-but-related values (recruited N vs analyzed N) are kept as separate keys with notes; only genuine contradictions are flagged.
- **Opt-in.** No `.research/`? Every skill runs standalone exactly as before.

### Notes for upgraders

- Nothing breaks. The vault engages only when you start one (via `/vault init`, `/research` pipeline mode, or accepting a skill's offer).
- claude.ai: the vault is markdown notes in the sandbox; invoke the `vault` skill by name (no slash command), and re-upload the vault notes across sessions.
- The plugin now has **15 skills** (added `vault`), 5 subagents, 16 slash commands.

## [0.11.0] — 2026-05-15

**Skill network.** Turns the 14 skills from loosely-coupled islands into an orchestrated network: *skills are nodes, shared artifacts are edges, `/research` is the conductor.* No skill behavior was weakened; this release adds the connective tissue. Workspace use and cross-skill chaining are opt-in — every skill still runs standalone exactly as in v0.10.0.

### Added

- **`docs/skill-network.md`** — the canonical contract for the network: the research-lifecycle DAG, the `.research/` workspace + `manifest.json` schema, the cross-skill invocation protocol, the mandatory human-gate rule, and the full Claude Code ↔ claude.ai degradation table. Every SKILL.md links here.
- **`## Handoffs` section in all 14 SKILL.md files** — a standardized contract replacing the old ad-hoc "composes well with" / "defer to X" prose. Each lists: lifecycle position, **Upstream** (what it reads + the producing skill + the artifact filename), **Downstream** (what it feeds), a **Chaining** block with explicit Claude Code vs claude.ai behavior, and its workspace output convention.
- **Shared `.research/` workspace convention** — skills write their deliverables to predictable paths and register them in `.research/manifest.json`, so downstream skills discover upstream outputs instead of making the user re-supply paths. Files are the source of truth; the manifest is advisory and reconciled at intake.
- **Active cross-skill invocation (Claude Code)** — `Skill` added to `allowed-tools` for the 13 skills that chain (peer-review left unrestricted so it keeps full annotation tooling). Skills can now invoke each other via the `Skill` tool — always behind an explicit human gate.
- **`/research` pipeline mode** — `commands/research.md` is now a router **and** a conductor. "start a project on X" walks the whole lifecycle (brainstorm → review → design → ethics → data → analysis → draft → peer-review → reviewer-response), reads/writes the manifest, pauses at human gates (data collection, IRB, submission/R&R), skips stages whose artifacts already exist, and resumes from the manifest `stage` on re-entry. Router mode (single request → one skill) is unchanged.
- **"How the skills work together"** section in the top-level README with the lifecycle DAG; a network pointer added to every per-skill README's "Composes well with" section.

### Changed

- `reviewer-response` SKILL.md: its bespoke `## Composition` section replaced by the standardized `## Handoffs` format.
- The 14 per-skill READMEs now point to `docs/skill-network.md` and frame "Composes well with" as the human-readable view of each skill's `## Handoffs`.

### Design rules (encoded throughout)

- **Human gate on every cross-skill invocation.** A skill *offers* to chain; the user confirms. No skill auto-runs another, and the conductor never advances past a human gate without a go-ahead. ("Co-pilot, not assistant.")
- **Both surfaces, one SKILL.md.** Every chaining instruction has a Claude Code branch (Skill tool / subagents) and a claude.ai branch (advisory "run /X next" / inline). No skill descriptions changed (char-limit safe).

### Notes for upgraders

- Nothing breaks. Run any single skill exactly as before; the workspace and chaining only engage when you opt in (via `/research` pipeline mode or by accepting a chaining offer).
- claude.ai users: the network degrades to advisory prose — skills tell you which skill to run next rather than auto-invoking, since claude.ai has no Skill tool, subagents, or cross-session filesystem.
- This is the first tag to exercise the `update-citation-doi.yml` workflow end to end (Zenodo integration was toggled on after v0.10.0).

### Deferred

- The `grant-writer` F1–F6 rigor overhaul (mirroring manuscript-drafter v0.8.0) — still parked for a later release.
- Visibility assets (screenshots / demo GIF / social-preview) — still deferred from v0.10.0.

## [0.10.0] — 2026-05-14

**General availability.** Promotes `v0.10.0-rc.1` to stable. Adds the remaining seven example folders, ships the CITATION.cff DOI auto-update workflow, and mints the Zenodo DOI on this tag.

### Added — remaining example folders (7)

- **`examples/replication-designer/`** — input.md (Smith et al. 2018 fictional target paper + direct replication intent) + output.md (full replication design with power calc for 2.5× original N, OSF pre-registration plan, multi-pronged success criterion).
- **`examples/grant-writer/`** — input.md (NSF Standard Grant, sociology, first-time PI) + output.md (Project Summary + first 3 pages of Project Description with fit-check note + `[PRELIMINARY DATA NEEDED]` and `[REVIEWER CONCERN UNADDRESSED]` markers).
- **`examples/talk-builder/`** — input.md (paper to 12-min contributed talk at Hypothetical NLP 2026) + output.md (beat-by-beat arc with timing, 13 slides with visual + speaker script + transitions, 5 backup slides for Q&A, rehearsal plan) + **`talk.md` (Marp slide deck stub)** — fulfilling the PRD Marp commitment.
- **`examples/citation-formatter/`** — input.md (3 messy mixed-style citations) + output.md (APA 7 + Vancouver + BibTeX renderings, plus "could not verify" notes for under-specified fields).
- **`examples/survey-design/`** — input.md (nurse workplace mental-health stigma survey) + output.md (instrument with 4 validated scales identified, 2 newly-developed scales flagged for cognitive testing, full pilot plan).
- **`examples/peer-review/`** — input.md + manuscript_excerpt.md + output.md (structured review: M1-M4 major issues, minor issues, brilliance suggestions, Major-revisions verdict, annotated-source description).
- **`examples/reviewer-response/`** — input/{R1_letter.md, manuscript_draft.md} + output.md (cover letter, point-by-point response to E.1-E.2 + R1.1-R1.4 + R2.1-R2.3 with categorization, change log, self-audit confirming every claimed revision actually appears).

All 14 examples now shipped. `examples/README.md` index updated to reflect completion.

### Added — CITATION.cff DOI auto-update

- **`.github/workflows/update-citation-doi.yml`** — triggers `workflow_run` after `release.yml` completes for a non-prerelease tag (also runnable manually via `workflow_dispatch` with a `tag` input). Polls Zenodo's records API (`/api/records`) for the deposit matching the GitHub repo + tag, with backoff (20 × 30 s = 10 min max wait). When the DOI is available, updates `CITATION.cff`'s `identifiers:` array (concept + version DOI) and `preferred-citation.doi` via `yq`, commits with `[skip ci]`, pushes back to main. Logs a clear warning + falls back to manual procedure if Zenodo doesn't mint within the window.
- **`CITATION.cff`** — added `identifiers:` array with two entries (concept DOI + version DOI), using placeholder values that the workflow replaces. `preferred-citation.doi` also placeholder-filled. Schema is CFF v1.2 compliant.
- **`CONTRIBUTING.md` § Release process** — documents the full release flow including the auto-update workflow's behavior and the manual fallback (toggle Zenodo GitHub integration, fetch DOIs from settings, edit CITATION.cff identifiers manually). Also documents `gh workflow run update-citation-doi.yml -f tag=vX.Y.Z` for re-triggering.
- **README** — added Zenodo DOI badge to the badge row. Initial placeholder URL resolves via the concept DOI once the workflow updates CITATION.cff. HTML comment explains the auto-update mechanism.

### Changed

- Version bumped 0.10.0-rc.1 → 0.10.0 in plugin.json, marketplace.json, README badge, CITATION.cff `version` and `preferred-citation.version`, CITATION.cff `date-released`.

### Notes for upgraders

- The Zenodo DOI badge on the README will show a "PLACEHOLDER-CONCEPT" link until the `update-citation-doi.yml` workflow runs successfully on the v0.10.0 tag. Expect this within 10-15 minutes of tag push.
- The `update-citation-doi.yml` workflow is idempotent — re-running for the same tag has no effect once DOIs are inserted.
- Pre-releases (`-rc.N`, `-beta.N`, etc.) are skipped by both Zenodo (by default) and this workflow's `if:` guard. Only stable tags mint DOIs.
- All 14 example folders are now shipped. Each follows the same input + output template. Contributors adding new skills must add a matching example per CONTRIBUTING.md.

### Out of scope (deferred to v0.10.1+)

- **Visibility assets** — screenshots in `docs/screenshots/`, demo GIF at `docs/demo.gif`, social-preview image. The README's "Visibility & assets" section references the placeholders.
- **rc.1 soak period** — skipped per release decision; any post-final issues become v0.10.1 patches.
- **The deferred grant-writer overhaul** — still parked for a later release (planned mirror of `manuscript-drafter` v0.8.0's F1-F6).

## [0.10.0-rc.1] — 2026-05-12

**Pre-release.** First "double-digit" release — a community-maturity push, no behavior changes to existing skills.

Version 0.9.0 is intentionally skipped at the plugin level; the planned `grant-writer` overhaul that was tentatively scoped as v0.9.0 is deferred to a future release (likely v0.11.0) so the v0.10.0 maturity work can be the focused next milestone. The CHANGELOG retains v0.9.0 as a deliberate gap to record this decision.

### Added — new skill

- **`reviewer-response`** — drafts a rigorous, polite, point-by-point response to reviewer comments (R1 / R2 / R3 letters) plus matching manuscript revisions. Categorizes each comment as concession + revision / partial concession / polite pushback / clarification needed / out of scope / minor; drafts response + revision per comment with verbatim reviewer quote; assembles a cover letter under one page that surfaces pushback up front. Self-audits that every claimed revision actually appears in the revised manuscript. Composes naturally with `peer-review` (consume comments) and `manuscript-drafter` (revise prose preserving voice). New `/respond` slash command. `/research` router updated with menu entry + routing keywords.

### Added — community-facing infrastructure

- **`CITATION.cff`** at repo root — Citation File Format v1.2.0. Renders as a "Cite this repository" widget on GitHub. Includes title, abstract, author, license, version, keywords. Zenodo-mintable on tag.
- **`CONTRIBUTING.md`** — strict-tone contributor guide. Documents what gets accepted and declined. PR-level bar: validation passes, CHANGELOG entry, version bump if applicable, dist rebuild, per-skill README + example update, no real-data leaks, no telemetry. Path for new skills requires a `New skill proposal` issue first.
- **`CODE_OF_CONDUCT.md`** — adopts Contributor Covenant 2.1 by reference (not inlined verbatim).
- **`.github/ISSUE_TEMPLATE/bug.md`**, **`feature.md`**, **`new-skill-proposal.md`** — structured intake for community contributions. New-skill template requires research-workflow articulation, closest-existing-skill comparison, hard rules, phase outline, output format, composition with existing skills, honest caveats, trigger phrases, maintenance commitment.
- **`.github/PULL_REQUEST_TEMPLATE.md`** — checklist enforcing the PR-level bar.
- **`docs/faq.md`** — common questions: citations, HIPAA / GDPR / IRB-protected data, language coverage, version sync, contribution path, comparison to Elicit / Consensus / Scite / ResearchRabbit, local vs. API execution, telemetry policy, license, uninstall path.

### Added — per-skill READMEs

- **`README.md` in every skill folder** (14 total — 13 existing + reviewer-response). Each follows a common template: one-line summary / trigger phrases / inputs / output / introduced-in version / spec link / "When to use this" framing / a synthetic example linked to `examples/<skill>/` / composition with other skills / honest caveats. The main README's skills table now links each skill name to its per-skill README.

### Added — examples

- **`examples/` folder with synthetic minimal examples** (7 shipped in rc.1; 7 deferred to v0.10.0 final). Each example is an input + output pair showing the skill's actual deliverable format. Shipped in rc.1: literature-review, methodology-advisor, ethics-committee, data-analysis, qualitative-coding, research-brainstorm, manuscript-drafter. Deferred to final: replication-designer, grant-writer, talk-builder, citation-formatter, survey-design, peer-review, reviewer-response.
- **`examples/README.md`** — directory index with status per example.

### Added — CI / automation

- **`.github/workflows/validate.yml`** — runs `claude plugin validate .` on every push to `main` and on PRs. Also checks every `SKILL.md` description for the ≤ 1024-char limit. Catches schema regressions and description-overflow before merge.
- **`.github/workflows/build-dist.yml`** — auto-rebuilds `dist/*.zip` when `skills/**` changes. Currently uploads as a workflow artifact (auto-commit-back is commented out in favor of GitHub Release distribution).
- **`.github/workflows/release.yml`** — on tag push matching `v*.*.*` or `v*.*.*-*`, builds all dist zips, extracts the matching CHANGELOG section as release notes, creates a GitHub Release with the zips attached, marks pre-release for tags containing a hyphen.

### Added — visibility (planned for rc.1 → final cycle)

- `docs/screenshots/` directory ready for high-DPI screenshots of typical skill outputs (annotated PDFs, methodology with the AI/ML extensions table, Word docs with anchored comments).
- `docs/demo.gif` / `docs/social-preview.png` placeholders.
- Social-preview image to be uploaded via GitHub Settings → Social preview.

### Changed

- **README badges** — added CI status (from validate.yml) and "Cite this repository" link. Version bumped to 0.10.0-rc.1. Existing badges (license, version, Claude Code, claude.ai) preserved.
- **README install paths for claude.ai users switched from `raw/main/dist/X.zip` to `releases/latest/download/X.zip`** — stable URLs that don't churn with every commit on main. This is the v0.10.0 distribution transition.
- **README skills table** — every skill name now links to its per-skill `README.md`.
- **`/research` router** — added `/respond` to the menu and `reviewer-response` to the routing keywords.

### Notes for upgraders

- This is a pre-release (`-rc.1` suffix). It is functionally complete for the maturity push but the Zenodo DOI mints only on `v0.10.0` final, and the remaining 7 example folders + visibility assets (screenshots, demo GIF, social-preview) land during the rc.1 → final cycle.
- For claude.ai users: the dist zips are now served from GitHub Releases. Update any saved download URLs accordingly. Old `raw/main/dist/X.zip` URLs continue to work for any past versions (no force-push), but new versions are released as Release assets only.
- No existing skill behavior changed in v0.10.0-rc.1. v0.8.0's manuscript-drafter overhaul is intact; v0.7.0's peer-review multi-format anchoring is intact.

## [0.9.0] — not released

The `grant-writer` overhaul originally scoped as v0.9.0 is deferred. The intent is to apply the same rigor pass (F1–F6: voice preservation, length budgets, register, literature-grounding, two-pass ideation/prose, language-aware) that `manuscript-drafter` received in v0.8.0. v0.9.0 is reserved as a placeholder; the actual grant-writer overhaul will likely ship as v0.11.0 after v0.10.0 final lands and the F1–F6 pattern has been tested in real use on manuscript-drafter.

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

[Unreleased]: https://github.com/Marazii/research-co-pilot/compare/v0.11.1...HEAD
[0.11.1]: https://github.com/Marazii/research-co-pilot/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/Marazii/research-co-pilot/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/Marazii/research-co-pilot/compare/v0.10.0-rc.1...v0.10.0
[0.10.0-rc.1]: https://github.com/Marazii/research-co-pilot/compare/v0.8.0...v0.10.0-rc.1
[0.8.0]: https://github.com/Marazii/research-co-pilot/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/Marazii/research-co-pilot/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/Marazii/research-co-pilot/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/Marazii/research-co-pilot/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/Marazii/research-co-pilot/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/Marazii/research-co-pilot/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/Marazii/research-co-pilot/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Marazii/research-co-pilot/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Marazii/research-co-pilot/releases/tag/v0.1.0
