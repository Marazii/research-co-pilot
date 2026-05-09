---
description: Stress-test a research protocol the way an ethics committee (IRB / REC / HREC) would
argument-hint: <protocol description, study summary, or path to a draft IRB application>
---

Invoke the `ethics-committee` skill from the **research-co-pilot** plugin and execute its full workflow.

The skill file is at `skills/ethics-committee/SKILL.md` relative to this plugin. Read it and follow it precisely — including:
- Phase 1: Intake (study summary, population, methods, data, jurisdiction, stage).
- Phase 2: Apply foundational principles (Belmont + GDPR-era extensions).
- Phase 3: Issue-by-issue checklist (consent, vulnerable populations, deception, risks, compensation, data, recruitment, COI, dissemination).
- Phase 4: Modern / digital issues (online & social media, AI/LLM, mobile/biometric, children online, genetic, dual use).
- Phase 5: Jurisdiction-specific notes (US, EU, UK, Canada, Australia, international).
- Phase 6: Optional committee-panel mode (3 reviewer voices + chair's summary).
- Phase 7: Decision letter output with required revisions, recommended changes, and disclaimer.

If the user asks for an ethics statement for a paper/grant rather than a full review, produce that format instead.

User input:
$ARGUMENTS

If no protocol or summary was given, ask for the study summary, target population, methods, data plan, and which ethics framework / jurisdiction applies.
