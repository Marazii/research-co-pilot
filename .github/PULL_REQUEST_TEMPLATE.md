## Summary

<!-- One paragraph: what does this PR change and why? Link the issue it resolves: "Closes #X" or "Refs #X". -->

## Type of change

- [ ] Bug fix (non-breaking)
- [ ] New functionality (non-breaking)
- [ ] Behavior change to an existing skill (potentially breaking — note in CHANGELOG)
- [ ] New skill (requires prior **New skill proposal** issue — link it: #)
- [ ] Documentation only
- [ ] CI / infrastructure
- [ ] Other (explain):

## Pre-merge checklist

Tick every box that applies. If a box doesn't apply, leave it unchecked but say why under "Notes."

- [ ] `claude plugin validate .` passes with zero errors and zero warnings.
- [ ] CHANGELOG entry added under `## [Unreleased]` in the correct section (`### Added` / `### Changed` / `### Fixed` / `### Removed`).
- [ ] Version bumped in `plugin.json`, `marketplace.json`, and the README badge (if user-visible).
- [ ] `dist/` rebuilt via `scripts/build-zips.sh` if any `skills/` file changed. *(After v0.10.0, this is handled by CI on release tag — local rebuild appreciated for review.)*
- [ ] Per-skill `README.md` updated if a skill's behavior, triggers, output, or composition changed.
- [ ] Example in `examples/<skill>/` updated if the skill's output format changed.
- [ ] Description char counts ≤ 1024 for every changed SKILL.md.
- [ ] No real participant data, copyrighted paper content, or personally identifying information in `examples/` or anywhere else.
- [ ] No new top-level dependencies introduced without prior discussion.
- [ ] No telemetry / analytics / phone-home behavior added.

## Notes

<!-- Anything reviewers should know. Trade-offs, alternatives considered, follow-ups for a future PR. -->

## Screenshots / output samples

<!-- For visible changes: before / after. For skill changes: a short input → output excerpt showing what's different. -->
