---
name: New skill proposal
about: Propose a new skill for research-co-pilot. Required before opening a PR for a new skill.
title: "[new-skill] "
labels: new-skill-proposal
---

> Please read [CONTRIBUTING.md § Adding a new skill (the long version)](../CONTRIBUTING.md#adding-a-new-skill-the-long-version) before filling this in. Skills that are just prompt templates without methodological discipline will be declined.

## Proposed skill name

<!-- kebab-case, matches the skill folder name. e.g., `data-management-plan`, `reproducibility-audit`. -->

## Research workflow this addresses

<!-- Specific. "Helps researchers write better" is not specific. "Generates an NIH-format Data Management Plan from a methodology document" is specific. -->

## Closest existing skill in the plugin

<!-- Which existing skill is closest to what you're proposing? Why does this need to be a separate skill rather than an extension of that one? -->

## Hard rules

<!-- 3-7 hard rules the skill will enforce. These are the methodological commitments that distinguish your skill from a generic prompt template. Examples from existing skills:
- "Never fabricate a citation."
- "Pre-specify the analysis before touching the data."
- "Anchor every annotation at the location it refers to — never bulk-append at the document end."
-->

1.
2.
3.

## Phases

<!-- Outline the workflow as 3-7 phases. Each phase should have a clear input → output transformation. Phases are usually Intake → 1-3 transformation phases → Output → Self-audit. -->

1. **Phase 1 — ...**
2. **Phase 2 — ...**
3. **Phase 3 — ...**

## Output format

<!-- What does the skill produce? File type, naming convention, structure. Example: "Writes `dmp_<funder>_<project>.md` with sections: Data Description / Metadata Standards / Storage and Access / Sharing and Reuse / Roles and Responsibilities / Compliance." -->

## Concrete usage examples

<!-- 2-3 short examples of how a user would invoke the skill and what they'd get back. -->

1.
2.

## Composition

<!-- Which existing skills does this compose with? How would they chain? -->

- Composes with `<skill>` because ...

## Honest caveats

<!-- What this skill cannot do or won't try to verify. What's left to human judgment. -->

## Trigger phrases

<!-- 5-10 example phrases that should route the user to this skill. These will go in the SKILL.md `description` field. -->

## Maintenance commitment

<!-- Are you willing to maintain this skill post-merge? Respond to bug reports, update for behavior changes elsewhere in the plugin? -->
