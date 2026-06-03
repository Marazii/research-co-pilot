# ethics-committee

> Pre-submission IRB / REC / HREC stress-test. Simulates a research ethics committee review across consent, vulnerable populations, AI/LLM use, social-media data, and GDPR. Returns a decision letter with required revisions. **Not a substitute for institutional approval.**

**Triggered by:** `/ethics`, plus *"is this study ethical?"*, *"review my IRB application"*, *"informed consent"*, *"draft an ethics statement"*, *"Belmont"*, *"Helsinki"*, *"vulnerable population"*, *"REC"*, *"HREC"*, *"ethics committee"*.

**Inputs needed:**

- Study summary (research question + what will be done with whom).
- Population, recruitment, sample size, anticipated vulnerabilities.
- Methods (surveys, interviews, observation, biospecimens, digital traces, intervention, deception).
- Data plan (what's collected, identifiability, storage, retention, sharing).
- Jurisdiction / framework — US Common Rule, EU GDPR, UK HRA / REC, Canada TCPS-2, Australia NHMRC, Helsinki for international.
- Stage — pre-submission audit / responding to IRB feedback / paper ethics statement / mid-study amendment.

**Output:**

- `ethics_review_<study>.md` formatted as a committee decision letter: required revisions, recommended changes, notes for consideration, section-by-section assessment, suggested next steps, **and an explicit disclaimer that this is not institutional approval.**
- Optional **3-reviewer panel mode**: simulates participant-advocate, methodological, and regulatory voices separately, with a chair's synthesis.

**Introduced in:** [v0.2.0](../../CHANGELOG.md#020--2026-05-10).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill before sending a protocol to your IRB to catch issues your committee will flag, when responding to IRB / REC revisions and you want to pressure-test your reply, when drafting the ethics section of a manuscript or grant, when a study scope changes mid-stream, when reviewing someone else's published study for ethics in a journal-review context, and when you want a 3-reviewer panel that surfaces tensions a single-voice review can hide.

It is most valuable as a *pre-submission audit*. It cannot grant approval. Anything genuinely legal (data residency, mandated reporting specifics, jurisdiction-specific consent forms) must go to your institution's compliance office.

## Example

**Input:** *"Protocol: online survey of 500 nurses about workplace-mental-health stigma. Recruited via professional Facebook groups. Pays $5 gift card. US-based. Pre-submission audit."*

**Output:** `ethics_review_nurse_survey.md` with required revisions including:

1. Recruitment via Facebook professional groups raises the question of group-level consent (the group exists for professional discussion; ethics of recruitment in that space).
2. "Nurses" can be vulnerable when the disclosure topic is workplace stigma — employer-identifiability risk if data is breached or re-identified.
3. $5 compensation is reasonable; the platform fee model needs spelling out.
4. Online-only consent flow needs documentation; recommend an attention check ensuring participants read it.
5. Data-sharing plan absent — recommend pre-specifying.
6. Recommend US Common Rule Subpart D considerations don't apply (no minors), but flag that recruitment in a professional forum can shade into "employees" if employer-managed groups are used — clarify.

See [`examples/ethics-committee/`](../../examples/ethics-committee/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`methodology-advisor`** — Send the methodology output here for an ethics audit before IRB submission.
- **`replication-designer`** — Replications often re-trigger ethics review; pair these skills when designing replications.
- **`grant-writer`** — The data-management-plan section in grant-writer benefits from the ethics audit's privacy guidance.
- **`survey-design`** — Survey-design proposes the instrument; ethics-committee audits the protocol that fields it.

## Honest caveats

- **Not a substitute for institutional approval.** Every output includes this disclaimer; honor it.
- The skill is jurisdiction-aware (US / EU / UK / Canada / Australia + Helsinki / CIOMS) but won't replace your institution's specific compliance office for legal questions.
- It surfaces concerns more readily than it dismisses them — false-positive flags are expected. The user-as-researcher decides which concerns the design actually needs to address vs. which are non-issues in context.
- AI / LLM-use-in-research framing is covered (data sent to APIs, validation of NLP outputs, synthetic participants framing); rapidly evolving — re-run for protocols where AI involvement is central.
- Indigenous-research ethics (OCAP, AIATSIS) and other community-specific frameworks are noted but should be supplemented with community-specific consultation.
