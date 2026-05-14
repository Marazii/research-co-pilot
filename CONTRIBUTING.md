# Contributing to research-co-pilot

This is an opinionated open-source plugin maintained by one person on best-effort time. Contributions are welcome; the bar is high. This document tells you exactly what gets accepted and what doesn't, so neither of us wastes time.

## Maintainer responsiveness

- Issues acknowledged within ~7 days, usually faster.
- PRs reviewed within ~14 days, usually faster.
- Best-effort — no SLA. If a thread goes quiet, ping politely after two weeks.

## What this project is — and what it is not

**Is:** A rigor-first research workflow plugin for Claude Code and claude.ai. Every skill encodes a methodologist's discipline (no fabricated citations, no p-hacking, no themes without an audit trail, etc.). The skills are designed to refuse common AI failure modes, not to be maximally helpful at the cost of correctness.

**Is not:** A general-purpose chatbot wrapper. A SaaS product. A research-data-collection or analytics platform. A pre-print server. A reference manager. A LaTeX editor. A statistical software replacement.

Contributions that drift from "rigor-first research workflow" toward "general productivity" or "AI for everything" will be declined or asked to scope down.

## How to propose a change

| Type of change | Path |
|---|---|
| Bug report | Open an issue using the **Bug** template. Reproduce on the latest tag if possible. |
| Doc improvement (typos, clarification, broken link) | Open a PR directly. No issue needed. |
| New skill | Open an issue using the **New skill proposal** template *first*. Discuss before implementing. PRs for new skills opened without prior discussion will be declined. |
| Skill behavior change (new hard rule, new phase, output format) | Open an issue first. Same reason. |
| New subagent or slash command (for an existing skill) | Open a PR directly with a short rationale in the PR body. |
| New citation style / qualitative tradition / methodological framework support inside an existing skill | Open a PR directly. |
| CI / infrastructure improvement | Open a PR directly. |
| Translation / i18n | Currently out of scope at the front-door (README is English). Skills already support multiple languages including Hebrew. If you have an idea for adding another language's register, open an issue. |

## What gets accepted (PR-level bar)

A PR will be merged only if **all** of these are true:

1. **Tests / validation pass.** `claude plugin validate .` returns zero errors and zero warnings. CI is green.
2. **A CHANGELOG entry exists** under `## [Unreleased]` in the relevant `### Added` / `### Changed` / `### Fixed` / `### Removed` section.
3. **A version bump is included** if the change is user-visible — patch for bug fixes, minor for new functionality, following the existing release cadence. If you're unsure, leave the version alone and the maintainer will bump it on merge.
4. **`dist/` is rebuilt** via `scripts/build-zips.sh` if any file under `skills/` changed. CI auto-rebuilds, but local rebuild + commit is appreciated to keep diffs reviewable. *(After v0.10.0, `dist/` lives in Release assets rather than `main` — see the [v0.10.0 CHANGELOG entry](CHANGELOG.md) for the transition.)*
5. **The per-skill README is updated** if a skill's behavior, triggers, output, or composition changed.
6. **An example is updated** in `examples/<skill>/` if the skill's output format changed.
7. **The PR description follows the template** (`.github/PULL_REQUEST_TEMPLATE.md`) — fill in the checklist; an empty checklist is a sign the PR isn't ready.
8. **No new top-level dependencies** without explicit discussion. The plugin should not require a heavyweight install. Python libraries auto-installed in a skill body are fine; new system dependencies are not.
9. **No telemetry of any kind.** This is a privacy-sensitive use case. Any PR that adds analytics, usage tracking, opt-in or opt-out telemetry, or phone-home behavior will be declined.

## What gets declined

- "I built a quick AI thing for X and bundled it as a skill" — skills require careful methodological grounding (hard rules, phases, output schema, self-audit). A skill that's just a prompt template will be declined.
- Adding features that contradict the rigor-over-fluency philosophy — e.g., a skill that generates "themes" without a codebook, or a literature-review variant that skips citation verification.
- Renaming existing skills or commands without a strong reason (breaks installs).
- Major architectural changes (new skill types, new manifest fields, new SDK targets) without a prior issue discussion.
- Skills that target a single proprietary platform (e.g., requiring a paid Elsevier API) unless they fall back gracefully when the platform isn't available.
- PRs that introduce real participant data, real paper content under copyright, or real personally identifying information into `examples/`. All examples must be synthetic.
- PRs that bundle a behavior change with a refactor with a doc fix. One thing per PR. Reviewers' time is the bottleneck.

## Adding a new skill (the long version)

Skills are the core unit of value here. The bar for a new skill is high because every skill becomes a maintenance commitment. To pass:

1. **Open a new-skill-proposal issue first.** Use the `.github/ISSUE_TEMPLATE/new-skill-proposal.md` template. Include: the research workflow this addresses, the existing skill closest to it (and why a separate skill is needed), the 3–7 phases your skill will use, the hard rules, the output format, and 2–3 concrete usage examples.
2. **Wait for maintainer confirmation** before implementing. Some proposals get declined at the proposal stage to save you time.
3. **Implement to the skill template.** Frontmatter (`name`, `description` ≤ 1024 chars including triggers, `argument-hint`, `allowed-tools`). Body with hard rules section, numbered phases, output template, self-audit checklist. The voice should match the existing skills — calm, opinionated, refusing AI failure modes by name.
4. **Add the slash command** under `commands/`.
5. **Update `commands/research.md`** (menu + routing keywords).
6. **Add the per-skill README** under `skills/<your-skill>/README.md`.
7. **Add a synthetic example** under `examples/<your-skill>/`.
8. **Add the row to the main `README.md`** skills table.
9. **Add a CHANGELOG entry.**
10. **PR with a checklist** and link to the proposal issue.

Skills that pass: substantive workflow with discipline, hard rules that catch real failure modes, output schema a reviewer can audit, clear composition with at least one existing skill.

## Release process (for maintainers)

The release flow for a stable `vX.Y.Z` tag:

1. **Bump version** in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` (plugin-entry), `CITATION.cff` (`version` and `preferred-citation.version`), and the README version badge.
2. **Add a CHANGELOG entry** under `## [X.Y.Z] — YYYY-MM-DD` with the changes; update the link refs at the bottom of `CHANGELOG.md`.
3. **Rebuild `dist/*.zip`** locally for sanity (`./scripts/build-zips.sh`). CI will rebuild on tag push anyway.
4. **Validate**: `claude plugin validate .` — zero errors and zero warnings.
5. **Commit, push to `main`**.
6. **Tag**: `git tag -a vX.Y.Z HEAD -m "vX.Y.Z — <short summary>"` then `git push --tags`.
7. **CI takes over.** The `release.yml` workflow creates a GitHub Release with all 14 `dist/*.zip` files attached and the matching CHANGELOG section as release notes. Pre-release flag is set automatically when the tag contains a hyphen (e.g., `vX.Y.Z-rc.N`).
8. **Wait for Zenodo to mint the DOI** (1-10 minutes for stable tags; pre-releases are skipped by Zenodo by default).
9. **`update-citation-doi.yml` runs automatically** after `release.yml` completes for a non-prerelease tag. It polls Zenodo, updates `CITATION.cff`'s `identifiers:` array and `preferred-citation.doi` with both the concept DOI and the version-specific DOI, and commits with `[skip ci]`.
10. **Refresh marketplace cache + update local install:**
    ```bash
    claude plugin marketplace update research-co-pilot-marketplace
    claude plugin update research-co-pilot@research-co-pilot-marketplace
    ```

### Manual fallback if Zenodo DOI auto-update fails

If the `update-citation-doi.yml` workflow logs `Zenodo deposit not found within 10 minutes`, fall back to manual:

1. Go to <https://zenodo.org/account/settings/github/> and confirm the integration is toggled ON for `Marazii/research-co-pilot`. If not, toggle it and re-run the workflow via `gh workflow run update-citation-doi.yml -f tag=vX.Y.Z`.
2. Find the deposit at <https://zenodo.org/account/settings/github/> (or search Zenodo for the repo + tag). Copy the concept DOI and the version DOI.
3. Edit `CITATION.cff` manually: replace the two `value:` lines under `identifiers:` and the `preferred-citation.doi` line. Commit with `[skip ci]`, push.

### Re-trigger DOI workflow manually

The workflow accepts `workflow_dispatch` input for a tag:

```bash
gh workflow run update-citation-doi.yml -f tag=vX.Y.Z
```

Useful if Zenodo mints late, or if the first run failed for a transient reason.

## Reviewing a PR

If you have commit access and are reviewing on the maintainer's behalf:

- Read the PR description first; if the checklist is incomplete, ask for it before reading code.
- Run `claude plugin validate .` locally on the PR branch.
- Read `CHANGELOG.md` — is the entry accurate and in the right section?
- For skill changes: read the SKILL.md as a researcher (does the workflow read as rigorous?), then read it as an editor (does the prose hold up?).
- For example changes: try the example mentally — does the input → output flow make sense?
- Flag scope creep aggressively. PRs that grew during review should be split.

## Code of Conduct

By contributing, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md) (Contributor Covenant 2.1).

## License

By submitting a PR, you agree your contribution will be released under the project's [MIT License](LICENSE).

## Security

If you find a security issue (e.g., a skill that mishandles user-provided files, a script that runs unintended commands), follow the responsible-disclosure process in [SECURITY.md](SECURITY.md). Do not file a public issue with exploit details.

## Contact

Issues: <https://github.com/Marazii/research-co-pilot/issues>
Maintainer: Maya Arazi (open a GitHub Discussion for non-bug questions).
