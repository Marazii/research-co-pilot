# survey-design

> Designs rigorous surveys and questionnaires — question wording, response scales, ordering, validation, pilot testing, translation. Recommends validated instruments rather than inventing new ones. Spots leading questions, double-barreled items, social-desirability traps, acquiescence bias.

**Triggered by:** `/survey`, plus *"design a survey"*, *"questionnaire"*, *"Likert scale"*, *"question wording"*, *"is this question biased"*, *"validated scale for…"*, *"survey pilot"*, *"cognitive interview"*.

**Inputs needed:**

- The goal — what decision will the data inform?
- Constructs you're measuring (list them).
- Population — who, and how you'll reach them.
- Mode — web / phone / mail / in-person / mixed.
- Target sample size and analysis plan.
- Subgroup comparisons planned (drives stratification).

**Output:**

- `survey_<topic>.md` with: goal / population / mode / target N / completion time / constructs measured (with validated-scale citations where applicable) / the survey instrument itself (sections, items, response scales, skip logic) / pilot plan (expert review + cognitive interviews + quant pilot) / analysis-plan preview / translation guidance if multilingual.

**Introduced in:** [v0.1.0](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when designing a new survey instrument, when revising an instrument that's producing weird data (item-total correlations off, ceiling/floor effects, drop-off mid-instrument), when responding to a reviewer who flagged "leading questions" or "non-validated scales," when planning a multilingual survey that needs translation discipline, or when you want to be pushed to use a validated instrument rather than inventing one.

It is opinionated about preferring validated scales when they exist. The construct you want to measure has almost certainly been measured before; the skill searches for and recommends published instruments before drafting new items.

## Example

**Input:** *"Survey for nurses about workplace mental-health stigma. N=500, web mode, US-based, English. Need to measure: stigma toward colleagues, willingness to disclose, organizational climate, intent to seek care. Pilot plan needed."*

**Output:** `survey_nurse_stigma.md` with:

1. **Validated scales recommended** (and located): Internalized Stigma of Mental Illness Inventory; Workplace Outcome Suite; Brief Self-Stigma Scale. Citations + use-terms checked.
2. **New items** drafted only for constructs without good validated coverage (e.g., a specific organizational-climate facet not covered by existing scales) — with the full item-writing checklist applied (one concept per item, neutral framing, mutually exclusive response options, clear time frame).
3. **Instrument structure** — engaging opener, sensitive items in the middle after rapport, demographics at the end with "prefer not to say" options.
4. **Banned patterns flagged** in the drafted items: 2 double-barreled, 1 leading, 1 vague quantifier — revised.
5. **Pilot plan** — expert review (3 named experts), cognitive interviews (5-10 nurses), quant pilot (30-50), iteration plan, then field.
6. **Burden estimate** — completion time ~8 minutes; drop-off acceptable for web-survey norms.

See [`examples/survey-design/`](../../examples/survey-design/) for a worked sample.

## Composes well with

- **`methodology-advisor`** — Survey-design produces the instrument; methodology-advisor specifies the study design that fields it.
- **`ethics-committee`** — Ethics-committee audits the protocol that uses the survey.
- **`data-analysis`** — Once data is collected, data-analysis runs the analysis-plan-preview specified here.

## Honest caveats

- **Validated instruments are population-specific.** A scale validated on US college students may not transfer to your context — the skill notes the validation population and recommends re-piloting in your target sample.
- **Cognitive interviews are non-optional in practice** — they surface more problems than expert review or quant pilot. The skill specifies the protocol but you (or your team) run them.
- **Translation discipline** (forward-back + cultural adaptation + re-pilot per language) is scaffolded but execution requires bilingual collaborators.
- **Demographic items** are handled with current conventions (free-text age + bucket later; gender identity distinct from sex assigned at birth; multi-select race / ethnicity); some local conventions or institutional norms may differ.
- **For complex measurement** (IRT, factor analysis, latent class analysis of measurement structure) the skill specifies what's needed but data-analysis runs the actual psychometrics.
- **A 10-question survey 1000 people complete > a 50-question survey 200 people complete.** The skill applies this principle and may push back on long surveys.
