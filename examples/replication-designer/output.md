# Replication Design: Smith et al. 2018 — Attention-Context Effect on Word Recall

> **Synthetic example.** Illustrative format only. Smith et al. 2018 is fictional.

**Original citation:** Smith, A., Jones, R., & Patel, S. (2018). Attention context modulates word recall. *J. Hypothetical Psychology*, 12(3), 142-158.
**Replication type:** Direct
**Primary investigator:** [user]
**Date:** 2026-05-14

## 1. Original study summary

- **Hypothesis:** Word recall is moderated by attention context at encoding (focused vs. divided).
- **Design:** 2-condition between-subjects experiment.
- **IV:** Attention condition (focused / divided) at encoding.
- **DV:** Free recall accuracy after 20-min delay.
- **Population:** US undergraduates, N=89, 2017-2018 academic year.
- **Sample size:** N=89; reported power = .80 for d=.45.
- **Key effect size:** Cohen's d = 0.45 (95% CI [0.03, 0.87] inferred from N=89 + p=.04).
- **Primary test:** Two-sample t-test, α=.05, two-sided.
- **Pre-registered originally?** No (pre-2018 norms).
- **Materials:** stimuli + analysis code available on the paper's OSF page.

## 2. Replication intent

We replicate to estimate the effect honestly, given (a) the original effect's wide CI suggesting publication noise rather than precision, (b) the attention-recall literature has seen multiple failures of related effects since 2018, and (c) the result is a load-bearing citation in our own ongoing research. The point is fair estimation, not refutation.

## 3. Design comparison

| Element | Original | Replication | Reason for change |
|---|---|---|---|
| Population | US undergraduates, 2017-18 | US undergraduates, 2026-27 | Unavoidable; comparable population type |
| Sample size | N=89 (~45/group) | **N=240 (~120/group)** | 2.5× original to detect even an inflated-down effect |
| Stimuli | Word list from original OSF | Same word list | Direct replication |
| Procedure | In-lab paper | Online (Qualtrics + 20-min computer-paced delay) | Modernization; pilot to verify equivalence |
| Outcome measure | Manual scoring | Automated string match + manual audit of edge cases | Adds inter-rater reliability check |
| Analysis | t-test, α=.05 | **t-test + TOST equivalence test (bounds: d=±0.20)** | Adds informative null test |
| Pre-registration | None | OSF preregistration before data collection | Standard for replications |

Each deviation is methodologically motivated and minor. Documented in pre-registration for transparency.

## 4. Sample size + power

- Assumed effect size: d=0.225 (50% of original, accounting for publication-bias inflation).
- α = .05 two-sided; power = .90.
- → **N=240 total (~120 per group).** `pwr.t.test(d=0.225, power=0.90, sig.level=0.05)` in R.
- Stopping rule: full N=240; no peeking; no early stop.

## 5. Materials

- Stimuli sourced from the original paper's OSF deposit. Confirmed accessible 2026-05-14.
- Online delivery via Qualtrics; 20-min unfilled delay (with attention-check task to prevent rehearsal).
- Pilot N=20 to confirm online procedure produces comparable recall baseline to original (no significant baseline difference expected).

## 6. Procedure

1. Consent + demographics (5 min)
2. Encoding phase: 30 words presented one at a time at 2-sec intervals. Random assignment to focused (single-task) or divided (dual-task with digit-monitoring) attention condition. Manipulation check after encoding.
3. 20-min delay with unrelated filler task.
4. Free recall: 5 minutes, type all words recalled.
5. Debrief + compensation.

## 7. Analysis plan

- **Primary:** Independent-samples t-test comparing recall accuracy between focused and divided conditions. Pre-registered as the primary test.
- **Equivalence test (TOST):** Bounds d=±0.20 (smallest effect of interest). Pre-registered.
- **Secondary analyses (labeled as such):**
  - Effect size with 95% CI.
  - Bayes factor (default JZS prior) for direct evidence quantification.
  - Sensitivity: drop participants who failed manipulation check.
- **Replication-success criterion (pre-specified):**
  - Significance: p < .05 in same direction as original
  - Effect-size CI overlap: replication's 95% CI overlaps original point estimate (d=0.45)
  - Meta-analytic: combining original (N=89) + replication (N=240), pooled d remains significantly different from zero
  - "Successful replication" requires all three; "partial" if at least two; "failed" otherwise

## 8. Pre-registration

- **Platform:** OSF Registries.
- **Pre-registration link:** [to be filed before data collection].
- **Pre-registration date target:** 2 weeks before first participant.
- **Contents:** hypothesis, sample size + stopping rule, inclusion/exclusion, analysis pipeline, success criterion (Phase 7), TOST bounds.

## 9. Multi-site

Not applicable. Single-site for this replication.

## 10. Ethics

- IRB submission required (human subjects, online recruitment). Per the **ethics-committee** skill audit (separate output): standard online-survey protocol with consent + debriefing; low-risk; expected expedited review.

## 11. Communication with original authors

Email drafted to Smith et al. inviting protocol review before data collection. Pre-emptive inclusion increases collaborative posture and reduces "unfair test" critiques.

> **Subject:** Direct replication of your 2018 attention-context effect — protocol invitation
>
> Dear Dr. Smith, ...

## 12. Timeline

| Phase | Duration | Notes |
|---|---|---|
| Pre-registration | 2 weeks | OSF deposit before data |
| IRB | 2-4 weeks | expedited review expected |
| Pilot (N=20) | 1 week | verify online procedure |
| Main data collection (N=240) | 2-3 weeks | online recruitment |
| Analysis | 1 week | per pre-registered plan |
| Manuscript | 4-6 weeks | independent submission |

**Total:** ~3-4 months from now to submission.

## 13. Dissemination

- **Submission target:** *Psychological Science* (Registered Reports track) or *J. Hypothetical Psychology* (registered replication direct).
- **OSF deposit:** stimuli, raw data, analysis code, all replication materials.
- **Pre-print:** PsyArXiv after IRB approval.
