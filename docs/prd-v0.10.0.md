# research-co-pilot v0.10.0 — Product Requirements Document

> **One-liner:** Make the plugin credible as a community project — strict community polish, one new skill (reviewer-response), per-skill documentation, and visibility assets that make it look as reliable and serious as it is.
> **Author:** Maya Arazi (drafted via `/vibe-coder:prd`)
> **Date:** 2026-05-12
> **Status:** Approved (v1.0 amended after first review)
> **Version:** 1.1

## Amendments from v1.0 review

- **Scope expansion: one new skill in v0.10.0.** `reviewer-response` is in, against the original "no new skills" rule. Rationale: it composes naturally with `peer-review` (consume comments) and `manuscript-drafter` (revise prose), so it strengthens the demo story for the maturity release. The rest of the no-new-skills discipline holds — no other skill work in v0.10.0.
- **Per-skill READMEs.** Every skill folder gets a `README.md` (separate from `SKILL.md`) that explains the skill in human terms with a usage example, sample output, and a link to the SKILL.md spec. Total: 14 new READMEs (13 existing skills + reviewer-response).
- **Heavy visibility investment.** Screenshots, GIFs, social preview image, demo screencast. The repo should *look* as serious as it is.
- **Zenodo: in.** Set up account, link repo, mint DOI on v0.10.0 final tag.
- **Synthetic examples** (not anonymized real work) — fast to ship, no consent overhead.
- **Strict CONTRIBUTING tone** — explicit bar, high quality expected, response time best-effort.
- **Marp slide deck** in the `talk-builder` example.
- **Release strategy:** tag `v0.10.0-rc.1` once everything is built; live with it 3 days; tag `v0.10.0` (with Zenodo DOI registered) after.
- **CI auth question deferred to implementation.** Test `claude plugin validate` headlessly first; if API auth is required, add `ANTHROPIC_API_KEY` repo secret. Document outcome in CONTRIBUTING.md.

---

## 1. Executive Summary

v0.1.0 → v0.8.0 has been a sprint: 13 skills, 5 subagents, 14 slash commands, two major behavior overhauls (peer-review's multi-format anchored annotations and manuscript-drafter's voice/length/register craft pass), and ~8 versions in 3 days. The product surface area is broad and the philosophy is sharp. The infrastructure around it is not — there is no CI, no contribution path, no examples folder, no formal citation file, no demo, and the release process is manual enough that schema breaks have shipped twice.

v0.10.0 is the first "double-digit" release. It marks a transition from "Maya's personal toolkit she's shipping fast" to "a public research-tools project that outside researchers can adopt with confidence." It is intentionally **not a feature release**. No new skills, no new behavior changes, no new subagents. The work is entirely infrastructure, documentation, distribution, and community readiness.

The expected outcome: a researcher who lands on the GitHub repo in v0.10.0 should be able to (a) understand what the plugin does in 30 seconds, (b) see one concrete example of what they'd get, (c) install it confidently knowing CI is catching regressions, (d) cite it formally in their work, and (e) have a clear path to propose a fix or a new skill.

---

## 2. Problem Statement

### The Pain

Two distinct user groups are blocked by the current state of the repo:

**For Maya (the author):** Every release is bookkeeping-heavy. Bump versions in three files, update CHANGELOG, rebuild dist, validate, commit, push, tag, push tags, refresh marketplace, update local install. Two schema breaks have shipped because no CI runs `claude plugin validate .` automatically. Re-uploading 5+ zips to claude.ai manually after every change is friction that compounds.

**For outside researchers** (lab partners, the broader academic AI community, contributors who might land via GitHub topics): the repo currently signals "personal project shipping fast" rather than "stable open-source tool." Specific gaps:
- No examples — they can't see what output they'd actually get without installing and trying.
- No CITATION.cff — academics can't cite the plugin in their methods sections (mandatory for many journals if AI tools were used).
- No CONTRIBUTING.md — someone wanting to add a skill can't tell whether PRs are welcome or what the bar is.
- No issue templates — bug reports come in unstructured; feature requests get conflated with bugs.
- No CI status — they don't know whether the latest commit actually validates.
- `dist/` zips committed to main with non-deterministic timestamps — every rebuild touches every zip, creating noisy diffs and confusing version pinning.

### Why Now

Three reasons converge:

1. **The plugin is functionally complete enough to invite scrutiny.** v0.8.0 just shipped a craft fix based on real reviewer feedback. The next version of "shipping fast" risks shipping faster than the trust infrastructure can keep up.

2. **Two schema breaks have already shipped.** The marketplace `source` field break and the plugin `repository` field break both made it to GitHub in v0.1.0 because no automated validation runs. Each cost ~10 minutes of debugging mid-install. The third break will cost more — it might break someone else's install.

3. **The plugin has been distributed.** Maya has prepared WhatsApp messages for her lab and the repo has 20 GitHub topics applied. The first outside researcher landing on the repo could happen any day. Their 30-second impression matters more than another skill they won't notice.

### Who Feels This Pain

**Primary persona — The Curious Outside Researcher**
- **Role:** Mid-career academic researcher (postdoc, faculty, advanced grad student) in a field where AI tools are increasingly discussed.
- **Context:** Landed on the repo via a GitHub topic, a WhatsApp forward, a conference Slack, or a colleague's mention.
- **Goal:** Decide in under 5 minutes whether to install this.
- **Frustrations:** They've been burned by "research AI tools" that fabricate citations, oversell, or are abandoned three weeks after release. They need fast signal that this one is different.
- **Quote:** *"I have 90 seconds. Show me one real example of what it does, prove someone is maintaining it, and tell me how to cite it. Then I'll decide."*

**Secondary persona — The Contributor**
- **Role:** A researcher who tried the plugin, hit a rough edge, and wants to fix it OR who has an idea for a new skill from their own field.
- **Goal:** Submit a useful contribution without 30 minutes of figuring out the bar.
- **Frustrations:** No CONTRIBUTING guidance, no examples of past PRs, no clarity on whether the maintainer wants community contributions or just personal-toolkit work.
- **Quote:** *"I'd add a `consort-reporter` skill for clinical trials if I knew how to propose it without it being a fork-and-PR-into-the-void exercise."*

**Tertiary persona — Maya (the author)**
- **Role:** Plugin author, actively iterating.
- **Goal:** Stop running the same release checklist manually nine times in three days.
- **Frustrations:** Bookkeeping eats time that could go into actual skill design.
- **Quote:** *"I want to be writing the next skill, not bumping `version` in three files and rebuilding zips."*

---

## 3. Vision & Strategy

### Product Vision

After v0.10.0 ships, the research-co-pilot repo is **legible to a researcher who has never heard of it before**. They land on the README, scan one example, recognize themselves in the problem statement, see CI passing, see a recent commit and a real CHANGELOG, find a CITATION.cff, and either install or open an issue — both of those paths have a clear next step. The plugin stops being "Maya's fast-shipping personal toolkit" and starts being "a public research-tools project with a maintainer, contribution path, and quality signal."

The plugin's *behavior* doesn't change in v0.10.0. The *signal* around it does.

### Strategic Positioning

v0.10.0 positions research-co-pilot as a **maintained, citable, community-extensible research tools plugin** — distinct from:
- AI research assistants that are SaaS products with subscription costs (Elicit, Scite, Consensus, ResearchRabbit) — research-co-pilot lives in your tooling, not their cloud.
- Personal experiments that ship features and don't ship documentation (most "I built a Claude skill for X" GitHub repos).
- Heavyweight academic-software releases that take 18 months between versions (statistics packages, qualitative software).

The category: **opinionated, fast-moving, but professionally-maintained research-workflow tooling**. v0.10.0 makes the "professionally-maintained" part visible.

### Key Differentiators (vs. doing nothing in v0.10.0)

1. **CI catches schema breaks before they ship** — eliminates the most embarrassing class of regression.
2. **Researchers can cite the plugin** — CITATION.cff is rendered by GitHub and consumed by Zenodo / ORCID / reference managers. This is non-negotiable for serious academic adoption.
3. **One example per skill, visible in the repo** — the "what does it actually produce?" question is answered without installing.
4. **Contribution path is clear** — issue templates, PR template, CONTRIBUTING.md create a funnel for community improvements.
5. **Releases ship as GitHub Releases with `dist/*.zip` attached** — claude.ai users get stable download URLs that don't churn with every commit; main-branch `dist/` can stop being committed.

---

## 4. Goals & Success Metrics

| Goal | Metric | Target | Timeframe |
|------|--------|--------|-----------|
| Catch manifest regressions before they ship | `claude plugin validate .` runs on every push to main and every PR | 100% of pushes covered | End of v0.10.0 sprint |
| Make the plugin formally citable | `CITATION.cff` rendered on GitHub repo page; valid against the [Citation File Format schema](https://citation-file-format.github.io/) | File exists, passes validation, renders | End of sprint |
| Reduce time-to-comprehension for new visitors | A first-time visitor can name one concrete output the plugin produces within 60 seconds of landing on the README | Tested with 3 lab partners as a quick gut check | Within 2 weeks of release |
| Cut release bookkeeping time | Maya's manual steps to ship a new patch version | From ~12 manual steps to ≤4 (just `tag + push --tags`, CI handles the rest) | End of sprint |
| Enable structured contributions | Each new issue lands in one of three triaged templates (bug / feature / new-skill-proposal); each new PR follows the PR template checklist | First 5 external issues / PRs all follow templates | Within 1 month of release |

### North Star Metric

**Time from "researcher lands on the repo" to "researcher decides to install or close the tab"** — currently unmeasurable, but the work in v0.10.0 (README scan + one example + CI badge + recent commit signal) should collapse it from "I'll think about it later" to "yes / no in under 5 minutes."

A secondary, measurable proxy: **GitHub stars per week and `git clone` count per week** for the two weeks before vs after v0.10.0 ships. Imperfect but directional.

---

## 5. User Personas & Journey

### Primary Persona: The Curious Outside Researcher

- **Role:** Postdoc or junior faculty in social sciences, biomedical, CS, or applied research.
- **Demographics:** 28–45, English-fluent, comfortable with terminal but not a software engineer. Uses Claude.ai daily for routine writing, uses Claude Code occasionally for specific tasks.
- **Goals:** Find AI tools that actually respect methodological standards. Stop burning time on tools that fabricate. Have a defensible answer when asked "did you use AI" — citable, transparent, with audit trails.
- **Frustrations:** AI tools that oversell. AI tools that get abandoned three weeks after launch. AI tools that don't say what they won't do.
- **Quote:** *"I'll install it if I can cite it. I'll cite it if I can prove it does what it says."*

### User Journey Map

| Stage | Action | Thinking | Feeling | Touchpoint | Opportunity (v0.10.0 work) |
|---|---|---|---|---|---|
| Awareness | Sees the GitHub link in a forwarded WhatsApp message or a discipline-specific Slack | "Yet another research AI thing — what makes this different?" | Skeptical | GitHub repo card | Repo description + topics + social preview convince them to click |
| Consideration | Lands on README | "Does this match my workflow? Is this serious?" | Evaluating | README top section | Badges (incl. CI status), one-line opening, skills table they scan in 20 seconds, one concrete example visible |
| First click | Opens `examples/literature-review/` to see real output | "What does this actually produce?" | Curious | `examples/` folder | Realistic input → realistic output samples answer the question without install |
| Citation check | Looks for how to cite the plugin in their methods section | "If I use this, can I disclose it properly?" | Needs proof | `CITATION.cff` file | CITATION.cff renders as a "Cite this repository" button on GitHub |
| Onboarding | Runs the install command | "Will this work or will it fail with a cryptic schema error?" | Cautious | `claude plugin install` | CI badge on README signals manifest is validated |
| First use | Runs `/research` or a specific skill | "Does the output match what the examples promised?" | Verifying | Skill output | (Out of v0.10.0 scope — behavior already shipped in v0.8.0) |
| Retention | Comes back for a second task | "Is this still maintained? Or already abandoned?" | Practical | Recent commits, CHANGELOG, latest tag | Active CI runs, dated CHANGELOG entries, GitHub Releases with attached zips all signal active maintenance |
| Advocacy | Tweets about it, recommends to a colleague, opens an issue with a feature request | "What's the bar for contributing back?" | Engaged | Issue + PR templates, CONTRIBUTING.md | Templates make their contribution path explicit |

---

## 6. Competitive Landscape

The competition isn't another research-AI product — it's **the default of doing nothing community-facing**. The relevant comparison is to other Claude Code plugins and other academic open-source projects in adjacent spaces.

| Reference project | Strengths to emulate | Weaknesses we'll avoid |
|---|---|---|
| `anthropics/claude-plugins-official` | CI on every PR; structured PR review; clear plugin manifests | Sometimes opaque about which skills are stable vs experimental — we'll be explicit in the CHANGELOG |
| `tidyverse` (R) | Beautiful CITATION files; clear governance; release cadence visible | Heavy contributor-onboarding overhead — we'll keep CONTRIBUTING.md tight |
| `scikit-learn` | `examples/` folder is the model for ours; CI is comprehensive | Massive surface area; we don't need to match that — we just need one example per skill |
| `OSF` itself | Citation-as-default for academic-tool work; DOI minting via Zenodo | Heavyweight institutional process — we'll lean on GitHub + Zenodo's native integration |

### Competitive Moat

The moat is the combination of (a) the rigor-over-fluency philosophy already encoded in the skills' hard rules, (b) the public CHANGELOG showing a maintained roadmap, (c) the CITATION.cff enabling academic adoption, and (d) the contribution funnel enabling community extension. v0.10.0 builds (b), (c), and (d). (a) already exists.

---

## 7. Feature Requirements

### MVP (v0.10.0 scope)

| # | Feature | User Story | Priority | Complexity |
|---|---------|------------|----------|------------|
| F1 | `.github/workflows/validate.yml` | As a maintainer, I want `claude plugin validate .` to run on every push and PR so that schema breaks are caught before merge. | P0 | S |
| F2 | `CITATION.cff` at repo root | As an academic user, I want to cite the plugin formally in my methods section so that my disclosure passes journal scrutiny. | P0 | S |
| F3 | `CONTRIBUTING.md` | As a potential contributor, I want a clear description of how to propose a skill, a fix, or a doc improvement so that my PR has a chance of being merged. | P0 | S |
| F4 | `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1) | As a contributor, I want to know the community standards so I can participate confidently. | P0 | XS |
| F5 | `.github/ISSUE_TEMPLATE/bug.md` + `feature.md` + `new-skill-proposal.md` | As a researcher with a bug or idea, I want a template so I can file something actionable. | P0 | S |
| F6 | `.github/PULL_REQUEST_TEMPLATE.md` | As a contributor, I want a PR template so I cover the things a reviewer needs (skill / version bump / CHANGELOG entry / dist rebuild). | P0 | XS |
| F7 | `examples/` folder with one example per skill (13 total) — input artifact + sample output | As a curious researcher, I want to see one realistic example per skill so I can decide whether to install. | P0 | M |
| F8 | `.github/workflows/build-dist.yml` — auto-rebuild `dist/*.zip` when `skills/` changes and commit back | As a maintainer, I want zips to stay in sync with SKILL.md automatically. | P1 | M |
| F9 | `.github/workflows/release.yml` — on `v*.*.*` tag, create a GitHub Release with `dist/*.zip` attached and auto-generated changelog snippet from CHANGELOG.md | As a maintainer, I want tagging to produce a real Release with downloadable assets. | P1 | M |
| F10 | Stop committing `dist/` to main (replace with GitHub Releases for distribution) | As a contributor, I don't want my diffs polluted by binary zip churn. | P1 | M (depends on F9) |
| F11 | `docs/faq.md` — 10–15 most likely FAQ entries (citations, HIPAA, language coverage, license, requirements, etc.) | As a researcher with a constrained context (regulated data, non-English, etc.), I want to know whether the plugin fits before installing. | P1 | S |
| F12 | Add CI status badge + (optional) Zenodo DOI badge to README | As a researcher scanning the README, I want at-a-glance trust signals. | P1 | XS |
| F13 | Social preview image (1280×640 PNG; GitHub Settings → Social preview) | As a researcher seeing the repo link in chat, I want a useful preview card, not a generic GitHub default. | P2 | S |
| F14 | Update README install instructions to point at Release assets (not `main` branch raw URLs) for stable pinning | As a claude.ai user, I want downloads that don't change under me between releases. | P2 | S (depends on F9, F10) |

### Phase 2 (Post-v0.10.0, deferred to v0.11.0 or later)

- **Demo GIF / screencast** in README — high impact but high effort to produce well; punt to a separate cycle when it can get proper attention.
- **Zenodo integration** for DOI minting on each release — depends on Maya creating a Zenodo account and linking it to the GitHub repo; one-time setup but blocking on her.
- **Per-skill documentation pages under `docs/`** — currently SKILL.md serves double duty as both the skill body and the doc; splitting them helps readers but is large work.
- **A `research-co-pilot` website** (GitHub Pages from `docs/`) — only if growth warrants it.

### Explicitly Out of Scope

- **No new skills.** Not grant-writer overhaul (that's v0.9.0), not reviewer-response, not reproducibility-audit, not pre-registration. v0.10.0 is intentionally feature-frozen on the skill surface.
- **No behavior changes to existing skills.** No tightening of voice extraction, no register-rule expansion, no annotation-mechanism changes.
- **No multi-user / team features.** Shared codebooks, multi-coder reliability, etc. — deferred indefinitely.
- **No internationalization of the README.** Hebrew academic users are supported in the skills themselves; the repo's front door stays English.
- **No telemetry of any kind.** This is a privacy-sensitive use case and no v0.10.0 work introduces analytics.

---

## 8. Technical Considerations

### Recommended Tech Stack

GitHub Actions for CI/CD — the plugin already lives on GitHub, all collaborators have GitHub accounts, no new infrastructure is needed. Specifically:

- `actions/checkout@v4` — standard.
- A small `setup-claude-code.yml` composite action or `npm install -g @anthropic-ai/claude-code` step to make `claude` CLI available in CI. (Verify whether `claude plugin validate` works headlessly without auth — if it does, this is trivial; if it requires API key auth, use a repository secret.)
- `actions/upload-artifact@v4` for the dist build workflow.
- `softprops/action-gh-release@v2` for the release workflow.

For `CITATION.cff`, use the canonical format defined by [citation-file-format.github.io](https://citation-file-format.github.io/), validated by `cffconvert` or GitHub's built-in renderer.

### Architecture Overview

Three CI workflows, deliberately decoupled:

1. **`validate.yml`** triggers on `push` to `main` and on `pull_request`. Runs `claude plugin validate .`. Fails the build on any error or warning. ~30-second job.

2. **`build-dist.yml`** triggers on `push` to `main` when files in `skills/**` change. Runs `scripts/build-zips.sh`. Compares the rebuilt `dist/*.zip` against committed `dist/*.zip`. If different, opens an automated PR with the rebuilt zips (or — after F10 — uploads to release artifacts). ~1-minute job.

3. **`release.yml`** triggers on tag push matching `v*.*.*`. Runs `scripts/build-zips.sh`. Creates a GitHub Release with the tag's name, extracts the matching CHANGELOG section as the release notes, and attaches every `dist/*.zip` as a release asset. ~2-minute job.

The three workflows don't depend on each other. They can be implemented and rolled out independently.

### Data Model (High-Level)

No new data models. This release is purely infrastructure.

The CITATION.cff schema requires: `cff-version`, `message`, `title`, `authors`, `version`, `date-released`, optional `doi`, optional `repository-code`, optional `license`, optional `keywords`. All of these are derivable from the existing `plugin.json` and repo metadata.

### Third-Party Dependencies

- GitHub Actions runners (free for public repos).
- Optional: Zenodo (for DOI minting; integrates with GitHub Releases automatically once linked).
- `cffconvert` (optional, for local CITATION.cff validation; can use GitHub's renderer instead).
- `softprops/action-gh-release@v2` (open-source GitHub Action; pinned to specific SHA).

### Performance Requirements

- `validate.yml` must complete in under 2 minutes (90% of pushes don't change skills, so most runs validate quickly).
- `release.yml` must complete in under 5 minutes from tag push to Release URL.

### Security & Privacy

- No secrets needed for `validate.yml` if `claude plugin validate .` works without API access. Confirm this in implementation.
- If API auth IS required, store an Anthropic API key as a GitHub repository secret (`ANTHROPIC_API_KEY`) used only by CI. Document this in `CONTRIBUTING.md`.
- `release.yml` uses the default `GITHUB_TOKEN` — no additional secrets needed for creating releases on the same repo.
- No user data flows through CI. No telemetry. No analytics.

---

## 9. Design Principles

1. **No behavior changes.** v0.10.0 makes the *signal* around the plugin better, not the *plugin* itself. If a code review reveals that fixing infrastructure would also fix a skill bug, that fix goes into v0.10.1 — not v0.10.0.
2. **Honest signaling.** A CI badge that lies is worse than no CI badge. If CI is flaky, fix it before merging the badge.
3. **No surface-area expansion.** Resist the urge to "just add one more skill while we're at it." The whole point of this release is to consolidate.
4. **Templates over prose.** Where a structured template (issue, PR, CITATION.cff schema) can replace a free-text doc, prefer the template — it's easier to maintain and more useful for contributors.
5. **Optimize for the first 30 seconds.** Every README and `examples/` choice should pass the test: "would a researcher with 30 seconds get something useful from this?"
6. **Reproducibility starts at home.** The plugin lectures researchers about reproducibility (Hard rules in `data-analysis`, the deferred `reproducibility-audit` skill). v0.10.0's infrastructure should embody that — every release reproducible from a tag, every zip reproducible from its SKILL.md.
7. **One step away from Zenodo.** Even if Zenodo integration doesn't land in v0.10.0, every choice should make the eventual integration trivial (CITATION.cff in place, Release artifacts attached, tags matching versions).

---

## 10. Launch Strategy

### Go-to-Market

v0.10.0 itself is not a "launch" — it's a quiet release that improves trust signal. The actual outreach moments are:

- **Updated WhatsApp message to the lab**, framed as "the project is now properly maintained, here's the citation, here's how to contribute" rather than "new features." Different audience signal than the v0.5.0 / v0.8.0 messages.
- **A short tweet / Mastodon post** linking to the repo + the CHANGELOG entry, only if Maya wants outreach. Optional.
- **No conference / venue push.** The plugin is still single-maintainer; broader outreach is premature until at least one outside user has shipped something with it.

### Rollout Phases

| Phase | Audience | Goal | Duration |
|---|---|---|---|
| Alpha (internal) | Maya alone | All CI workflows green; examples render; CITATION.cff renders | 1–2 sessions |
| Beta (lab) | Maya's lab partners (WhatsApp distribution) | First external eyes; surface any "I don't get what this does" reactions; collect FAQ candidates | 1 week of natural use |
| GA | Public (existing GitHub topics + repo description) | The repo is the GA — no separate launch beat | Indefinite |

Tag v0.10.0 when alpha exit criteria are met. Beta = the same tag with lab eyes on it.

---

## 11. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| `claude plugin validate` requires API auth in CI, complicating `validate.yml` | Med | Med | Test headlessly first. If auth required, use `ANTHROPIC_API_KEY` repo secret. Document in CONTRIBUTING.md. |
| Removing committed `dist/` (F10) breaks claude.ai users who downloaded zips from `main`-branch raw URLs | Med | Med | F14 explicitly updates README to point at Release assets. Keep the last main-branch `dist/` commit in history (don't force-push). Communicate the change in the v0.10.0 CHANGELOG entry. |
| `examples/` becomes stale as skills evolve (F7) | High over time | Low individual | Tie an `examples/` update to the CHANGELOG entry for any skill behavior change. Add a self-audit checkbox in CONTRIBUTING.md's PR checklist. |
| CITATION.cff version drifts out of sync with `plugin.json` version | Med | Low | Add CITATION.cff version-update to the release workflow OR to the manual tagging checklist in CONTRIBUTING.md. |
| Scope creep — "while I'm in here, let me add reviewer-response" | High | High (slips v0.10.0 indefinitely) | Hard rule on this PRD: no skill work in this release. If a skill idea surfaces during v0.10.0 implementation, file as an issue for v0.11.0+ and move on. |
| Contributor templates intimidate rather than welcome | Low | Med | Keep templates short. Lead with "What problem are you running into?" rather than "Please fill in these 12 fields." |
| Maintainer fatigue — Maya burns out on infrastructure work | Med | High (project stalls) | This release is timeboxed (~1 week of evenings, not months). After v0.10.0 ships, the next release is back to a skill / feature (v0.9.0 grant-writer overhaul). |

---

## 12. Open Questions

1. **Does `claude plugin validate` work in headless CI without auth?** Needs testing in a draft workflow before F1 can be considered complete.
2. **Zenodo integration this release or defer?** Setting it up is mostly Maya-time-not-code: create Zenodo account, link to GitHub, push a tag. If it lands in v0.10.0, the DOI badge can be added to README. If not, CITATION.cff + a placeholder `doi:` field is fine and the badge waits for v0.11.0.
3. **Which 13 examples for F7, and how realistic should they be?** Two options: (a) synthetic minimal examples ("here's a fake methodology document, here's the fake analysis it produced") — fast to build, less convincing. (b) Real examples lightly anonymized from Maya's own work — more convincing, but takes longer and may require consent if collaborators are involved. Recommend (a) for v0.10.0 and (b) gradually for v0.11.0+.
4. **CONTRIBUTING.md tone** — strict (this is a personal project, contributions welcome but high bar) or open (genuinely seeking community extension)? The right answer probably depends on how much maintenance Maya wants to commit to. Default to the middle: "I welcome contributions, here's the bar, response time is best-effort."
5. **Should `talk-builder` examples include a sample slide deck (Marp / Quarto)?** Marp markdown is reasonable; full .pptx is heavyweight. Recommend Marp only.
6. **Do we tag v0.10.0 once everything is done, or do we tag v0.10.0-alpha through v0.10.0-rc.1 → v0.10.0?** For a community-facing maturity release, alpha/beta tagging signals seriousness. Recommend `v0.10.0-rc.1` once CI is green and templates exist, then `v0.10.0` after Maya has lived with it for ~3 days.

---

## 13. Appendix

### References

- Citation File Format spec: <https://citation-file-format.github.io/>
- Contributor Covenant 2.1: <https://www.contributor-covenant.org/version/2/1/code_of_conduct/>
- GitHub Actions docs: <https://docs.github.com/en/actions>
- `softprops/action-gh-release`: <https://github.com/softprops/action-gh-release>
- Claude Code plugin docs: <https://docs.claude.com/en/docs/claude-code/plugins>
- Zenodo–GitHub integration: <https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content>

### Related Plans

- `/Users/mayaarazi/.claude/plans/what-s-missing-in-my-prancy-galaxy.md` — original inventory of gaps that informed the v0.10.0 scope.
- v0.9.0 (in development): `grant-writer` overhaul mirroring `manuscript-drafter` v0.8.0's F1–F6. Independent of v0.10.0 work.

### Open Items for v0.11.0+ (parking lot)

- Reviewer-response skill (chains `peer-review` output → revision prose).
- Reproducibility-audit skill (audits a repo for reproducibility).
- Pre-registration skill (generates OSF / AsPredicted templates).
- Data-management-plan skill (NSF / NIH / ERC / Wellcome format DMPs).
- Scoping review skill (PRISMA-ScR optimized, distinct from general `literature-review`).
- Project Memory / cross-skill integration (the "platform" move deferred from v0.10.0).
- Demo GIF / screencast in README.
- A `research-co-pilot` GitHub Pages site if growth warrants it.
