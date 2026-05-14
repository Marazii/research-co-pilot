# Survey: Workplace Mental-Health Stigma Among Nurses

> **Synthetic example.** Illustrative instrument with validated-scale recommendations.

**Goal:** Inform a hospital-system-level intervention recommendation.
**Population:** Registered nurses in US hospitals, English-speaking.
**Mode:** Web (Qualtrics), anonymous.
**Target N:** 500 completed responses.
**Estimated completion time:** ~10 minutes.
**IRB status:** Required — university IRB (expedited review expected).

## Constructs measured

| Construct | Source | Items | Scale |
|---|---|---|---|
| Internalized stigma toward mental illness | Internalized Stigma of Mental Illness Inventory (ISMI; Boyd et al., 2014) — adapted | 10 | 4-point Likert (Strongly disagree → Strongly agree) |
| Willingness to disclose mental-health concerns at work | Newly developed (this study) | 6 | 5-point Likert |
| Perceived organizational climate for mental-health support | Workplace Outcome Suite — climate subscale (Lennox et al., 2010) | 5 | 5-point Likert |
| Intent to seek professional care | Mental Health Help-Seeking Inventory (Wilson et al., 2011) — short form | 4 | 5-point Likert |
| Self-reported mental-health stigma toward colleagues | Newly developed (this study) | 6 | 5-point Likert |
| Demographics | — | 8 | mixed |

**Validated-scale rationale:** Three of four core constructs already have validated instruments. Inventing new items only where validated scales don't fit (willingness to disclose at work; specific stigma-toward-colleagues facet). New items will need cognitive interviews + factor analysis before final use.

## Survey instrument (excerpt — 3 of 6 sections shown)

### Section 1: Opening + context (engaging, low-cognitive-load items)

*Intro text:*
> Thank you for participating in this anonymous study of workplace mental-health experiences among nurses. There are no right or wrong answers; we are interested in your experience. The survey takes about 10 minutes. You may skip any question or stop at any time.

**Q1.** Which best describes your current nursing role?
- ☐ Direct patient care
- ☐ Charge / shift lead
- ☐ Educator / preceptor
- ☐ Administrator / manager
- ☐ Other (please specify): _____
- ☐ Prefer not to say

**Q2.** Which unit do you primarily work in?
- ☐ ICU
- ☐ Emergency
- ☐ Medical-surgical
- ☐ Operating room / peri-operative
- ☐ Other (please specify): _____
- ☐ Prefer not to say

[...Q3–Q4 in Section 1...]

### Section 3: Workplace organizational climate (validated scale, 5 items)

[Workplace Outcome Suite — climate subscale, 5 items. Used with permission per the WOS author guidelines. Standard 5-point response: Strongly disagree → Strongly agree.]

Sample item:
**Q12.** Mental-health concerns are taken seriously by leadership at my workplace.
- ☐ Strongly disagree
- ☐ Disagree
- ☐ Neither agree nor disagree
- ☐ Agree
- ☐ Strongly agree

### Section 5: Willingness to disclose (newly developed; needs cognitive testing)

*Intro:*
> Thinking about the past 12 months, please indicate the extent to which you agree with each of the following.

**Q21.** I would be comfortable disclosing a mental-health diagnosis to my immediate supervisor.
**Q22.** I would be comfortable disclosing a mental-health diagnosis to my closest colleague on my unit.
**Q23.** I would be comfortable disclosing that I am receiving mental-health treatment to my employer's HR / occupational health team.

[5-point Likert each. Reverse-keyed items: Q24, Q25 — to detect acquiescence bias.]

### Section 6: Demographics

*Intro:*
> A few last questions for grouping responses. All are optional.

**Q27.** Years in nursing: _____ (free text, integer)
**Q28.** Highest level of nursing education completed:
- ☐ ADN / Diploma
- ☐ BSN
- ☐ MSN
- ☐ DNP / PhD
- ☐ Prefer not to say

[...Q29–Q34, all with "Prefer not to say"...]

## Skip logic

- Q2 → if "Other," show free-text field.
- Section 5 items: no skip logic (all participants see all items; "Prefer not to say" is per-item).
- No branching based on disclosed mental-health history (would compromise anonymity).

## Item-writing checklist applied

✓ One concept per item.
✓ Neutral framing (no leading items found).
✓ Concrete time frame ("past 12 months" in Section 5).
✓ Validated scales used where available.
✓ Reverse-keyed items in new sections to detect acquiescence.
✓ All items optional via "Prefer not to say."

**Banned patterns flagged in draft:**
- Initial draft of Q22 was: "I would be comfortable disclosing a mental-health diagnosis to my colleagues, manager, or HR." → **double-barreled.** Split into Q21 (supervisor), Q22 (colleague), Q23 (HR).
- Initial draft of Q23: "Wouldn't you agree that..." → **leading.** Rewritten in neutral form.

## Pilot plan

1. **Expert review** (1 week) — 3 nurse colleagues + 1 mental-health researcher for face validity.
2. **Cognitive interviews** (2 weeks) — 7 nurses recruited via personal network. Walk through the survey thinking aloud. Probe each item's interpretation.
3. **Quantitative pilot** (1 week) — N=50 nurses via online recruitment. Check:
   - Response distributions (any item with > 90% endorsement is uninformative — revise).
   - Item-total correlations within the new scales (target > 0.30).
   - Drop-off points (where participants quit).
   - Time-to-complete distribution.
4. **Iterate** — revise items based on pilot feedback.
5. **Final field** — full N=500 with confirmed instrument.

## Analysis plan (preview)

- **Scoring:** ISMI scored per published key (sum across 10 items, range 10-40). New scales: factor analysis on pilot → factor scores. Workplace Outcome Suite per author guidance.
- **Primary comparisons:** by unit type (ICU / ED / med-surg / other) and by years-of-experience tertile.
- **Statistical tests:** ANOVA or Kruskal-Wallis for unit type; regression with experience-by-stigma interaction as primary HTE check.
- **Missing data:** listwise deletion for primary analysis; multiple imputation as sensitivity.
- **Subgroup cell sizes:** target N=125 per unit type × tertile combination for adequate power; if cells fall below n=30, aggregate.

## Translation

Not applicable for this study (English-only US sample). If extended to bilingual settings: forward-back translation + cognitive interview in each language.

## Caveats

- **Self-report only.** Behavioral measures of stigma (disclosure rates in administrative data, EAP-utilization data) would strengthen — outside this study's scope.
- **Anonymous survey limits longitudinal follow-up.** A linked-anonymized version (coded ID + separate consent for follow-up) would enable better causal claims about intervention effects.
- **Recruitment via professional networks** biases toward digitally-active members — note in Limitations.
- The "Willingness to disclose" scale is newly developed and requires the pilot's psychometric analysis before scores are reportable as a measurement.
