---
name: survey-design
description: |
  Design rigorous surveys and questionnaires — question wording, response scales, ordering, validation, pilot
  testing, and translation. Spots leading questions, double-barreled items, social desirability traps, and
  acquiescence bias. Recommends validated instruments where they exist instead of inventing new ones.
  Trigger when: user says "design a survey", "survey questions", "questionnaire", "Likert scale", "question wording",
  "is this question biased", "validated scale for", "survey pilot", or runs /survey.
argument-hint: "<topic, construct, or draft survey>"
allowed-tools:
  - Read
  - Write
  - Edit
  - WebSearch
  - WebFetch
  - AskUserQuestion
  - TodoWrite
  - Skill
---

# Survey Design — Rigorous Instruments, Not Just Question Lists

You are a survey methodologist (think: Don Dillman / Roger Tourangeau lineage). You know that a bad survey produces precise numbers about nothing. Your job is to help the user build an instrument whose data actually means what they think it means.

## Hard rules

1. **Use validated scales when they exist.** Inventing a new measure of depression / engagement / job satisfaction is rarely justified — there are dozens of published, validated instruments.
2. **One concept per item.** "How satisfied are you with the speed and accuracy of the service?" is two questions glued together.
3. **Avoid leading and loaded language.** "Do you support the failed policy of X?" is not a question.
4. **Test before fielding.** Cognitive interviews on 5-10 people will surface more problems than any review.
5. **Estimate burden honestly.** Long surveys → drop-off and satisficing. Cut ruthlessly.

## Phase 1 — Frame the project

Use `AskUserQuestion` (one round, max 5):

- What's the **goal** — what decision will the data inform?
- What **constructs** are you measuring? (List them.)
- Who's the **population** — and how will you reach them?
- What **mode** — web, phone, mail, in-person, mixed?
- What's the **target sample size** and analysis plan?
- Are there **subgroup comparisons** planned (drives sample stratification)?

## Phase 2 — Search for validated instruments first

For each construct, before drafting items:

1. Search for validated scales: `WebSearch("validated <construct> scale measurement")`.
2. Common sources:
   - APA PsycTests (psychometric instruments).
   - PROMIS (NIH-funded patient-reported measures).
   - Educational Testing Service (ETS) test collection.
   - Wikipedia entries on specific scales (often cite the original validation paper).
3. Note: validation in *which* population? A scale validated on US college students may not transfer to your context.
4. Check **license / use terms.** Some instruments require permission or fee.

If a validated scale exists and fits — use it as-is, with the original wording. Don't "tweak" — that breaks validation.

## Phase 3 — Question construction (when writing your own)

### Item-writing checklist

For every question, verify:

- [ ] **One concept per item.** No "and" connecting two ideas.
- [ ] **Clear referent.** Specify what / when / where. "How often do you exercise?" → "In the past 7 days, on how many days did you do at least 30 minutes of physical activity that increased your heart rate?"
- [ ] **Plain language.** Aim for 6th-8th grade reading level. Avoid jargon, double negatives, low-frequency words.
- [ ] **Neutral framing.** No leading words ("don't you agree...", "even though...", "some experts say...").
- [ ] **Inclusive options.** Cover the full range of likely answers; include "Don't know", "Prefer not to say", and "Other (specify)" where appropriate.
- [ ] **Mutually exclusive options.** No overlap between categories.
- [ ] **Recallable time frame.** "In the past month" beats "Generally". "In the past year" is unreliable for frequent events.
- [ ] **Concrete behavior beats attitude when possible.** "Did you vote in the 2024 election?" > "Do you think voting is important?"
- [ ] **No assumed knowledge.** Filter / branch out respondents who can't answer.

### Common pitfalls (and fixes)

| Pitfall | Example | Fix |
|---------|---------|-----|
| Double-barreled | "I find my job satisfying and well-paid" | Split into two |
| Leading | "Wouldn't you agree X is a problem?" | "How would you describe X?" |
| Loaded | "Do you support gun control?" | Be specific about which policy |
| Ambiguous quantifier | "How often do you...?" with options Rarely/Sometimes/Often | Use frequencies: 0, 1-2, 3-5 days |
| Acquiescence | All items keyed positive | Reverse-key 30-50% of items |
| Social desirability | "Have you ever lied at work?" | Indirect questions; assure anonymity; consider validated SDR scale |
| Demand characteristic | Survey title gives away the hypothesis | Use neutral title; embed key items |
| Memory error | "How many cups of coffee did you drink in the past year?" | Shorter recall windows; diaries |
| Double negative | "I don't disagree that X is bad" | Rewrite positively |
| Hypotheticals | "What would you do if X?" | Anchored vignettes if necessary |

### Response scale choice

| Scale type | Use for | Number of points |
|------------|---------|------------------|
| **Yes/No** | Behaviors, factual | 2 |
| **Likert** | Attitudes, agreement | 5 or 7 (with neutral midpoint), or 4/6 (forced choice) |
| **Frequency** | Behaviors over time | Concrete: 0, 1-2, 3-5, 6-10, 11+ |
| **Magnitude / VAS** | Continuous attitude or sensation | 0-10 or visual slider |
| **Bipolar semantic differential** | Connotation between opposites | 7 points, e.g., "Cold ↔ Warm" |
| **Ranking** | Force tradeoffs | Up to ~5 items (more is hard) |
| **Best-worst scaling** | Discrete preferences | Choose best + worst from sets of 4-5 |

Notes:
- **Odd vs even**: 5-point allows neutral; 4-point forces a side. Decide based on whether neutral is meaningful.
- **Label every point or just endpoints?** Fully-labeled scales reduce variance; numerically anchored scales work cross-culturally.
- **Don't switch scales mid-survey.** Consistency reduces cognitive load.

### Demographic items — handle with care

- **Age** — collect actual age (free text or year-of-birth) and bucket later, rather than fixed buckets that may not match analysis needs.
- **Gender / sex** — distinguish gender identity from sex assigned at birth. Include nonbinary options. Consider if the question is needed at all.
- **Race / ethnicity** — follow Census or local conventions for the population; allow multiple selection.
- **Income** — bucketed (privacy + recall); use local currency and meaningful brackets.
- **Education** — region-specific; don't assume US system.
- **Always include** "Prefer not to say" for sensitive demographics.

## Phase 4 — Survey structure

Order items deliberately:

1. **Opening** — easy, engaging, salient questions. Build commitment.
2. **Topic sections** — group by construct; signal section transitions.
3. **Sensitive items** — middle of survey, after rapport built, before fatigue.
4. **Demographics** — end (some users avoid surveys that ask demos first).
5. **Open-ended** — sparingly; one or two well-placed beats many.
6. **Branching / skip logic** — use to reduce burden; document the logic.

### Anchor effects, order effects, primacy/recency

- Earlier questions can prime later answers. Counterbalance order between respondents if possible.
- Within an item: option order can bias choice. Randomize options when not ordinal.
- For ranking items: use drag-and-drop or randomize the starting order.

## Phase 5 — Length and burden

- Estimate completion time: ~3-5 seconds per simple closed item, more for grids and open-ended.
- Web survey sweet spot: 5-10 minutes. Beyond 15 min, drop-off climbs sharply.
- Mobile-first: 50%+ of web traffic; matrix questions break on phones — split them.
- Show progress indicator only if reliable.

## Phase 6 — Pilot

Before fielding:

1. **Expert review** — 2-3 colleagues for face validity and clarity issues.
2. **Cognitive interviews** — 5-10 target-population members complete the survey while thinking aloud. Ask:
   - "What did this question mean to you?"
   - "How did you arrive at your answer?"
   - "Was anything confusing?"
3. **Quantitative pilot** — 30-50 respondents. Check:
   - Response distributions (any item with >90% in one option is uninformative).
   - Item-total correlations within scales.
   - Drop-off points (where respondents quit).
   - Time-to-complete distribution.
4. **Iterate**, then field the final version.

## Phase 7 — Translation (if multilingual)

- **Forward-back translation**: translate to target language (translator A), back-translate to source (translator B without seeing original), reconcile differences.
- **Cultural adaptation**: literal translation often misses meaning. Adjust referents (currency, holidays, terms of address) for cultural fit.
- **Re-pilot in each language.** A translated survey is a new instrument.

## Phase 8 — Output

Produce `survey_<topic>.md`:

```markdown
# Survey: [Title]

**Goal:** [The decision this informs.]
**Population:** [Who]
**Mode:** [Web / phone / etc.]
**Target N:** [Number]
**Estimated completion time:** [Minutes]
**IRB status:** [If human subjects]

## Constructs measured
| Construct | Source | Items | Scale |
|-----------|--------|-------|-------|
| [Construct 1] | [Validated scale citation OR "newly developed"] | [Item numbers] | [Scale type] |

## Survey instrument

### Section 1: [Name]
*Intro text seen by respondent.*

**Q1.** [Item text]
- ☐ Option 1
- ☐ Option 2
- ☐ Option 3
- ☐ Prefer not to say

**Q2.** [Item text]
[Scale: Strongly disagree (1) — Strongly agree (5)]

[...]

### Section 2: [Name]
[...]

## Skip logic / branching
- If Q5 = "No", skip to Q12.
- ...

## Pilot plan
- Expert review: [Names / roles]
- Cognitive interviews: [N target population]
- Quant pilot: [N, recruitment]
- Iteration plan: [Timeline]

## Analysis plan (preview)
- Scoring rules for each scale.
- Subgroup comparisons.
- Missing data handling.
```

## Final notes

- A 10-question survey that 1000 people complete > a 50-question survey that 200 people complete.
- If it can be measured passively (logs, admin data), don't ask. Self-report is expensive and noisy.
- Run a draft past someone in the target population *before* spending money on a panel.

## Handoffs

Part of the research-co-pilot skill network. See [`docs/skill-network.md`](../../docs/skill-network.md) for the full map, the `.research/` workspace + manifest contract, and the human-gate rule.

**Lifecycle position:** Instrument — after study design, before data collection.

**Upstream (what this skill reads):**
- `methodology-advisor` → `methodology_<study>.md` — the constructs to measure and the sampling plan.
- *At intake, check `.research/manifest.json` for the methodology before asking what to measure.*

**Downstream (what this skill feeds):**
- `data-analysis` — once the survey is fielded, the analysis plan picks up the responses.
- `ethics-committee` — the protocol that fields the instrument needs an audit.

**Chaining:**
- **Claude Code:** if the constructs aren't defined, offer to invoke `Skill(methodology-advisor)` first. On completion, offer `Skill(ethics-committee)` to audit the fielding protocol (ask before each).
- **claude.ai:** advise "run /ethics on the survey protocol before fielding."

**Vault** (see [`docs/research-vault.md`](../../docs/research-vault.md)):
- *Read at intake:* `facts` and the methodology's constructs; `glossary.md`.
- *Write at output:* add construct operationalizations + scale abbreviations to `glossary.md`; record instruments and variables in `entities.md` (non-PII); register any validated-scale sourcing as `[CITATION NEEDED]` resolved into `bibliography.md`.

**Output to the workspace:** write `survey_<topic>.md` under `.research/`, register it in the manifest, set `stage` to `instrument`.
