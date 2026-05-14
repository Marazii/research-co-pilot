# Methodology: Feedback Intensity and Member Retention in Online Communities

> **Synthetic example.** Illustrative output. Not a real study.

## 1. Research question

Does feedback intensity received during the first 30 days of platform membership causally predict 12-month retention?

## 2. Paradigm and approach

Post-positivist, predictive + causal-blend question. Quantitative design with an identification strategy for the causal claim.

## 3. Design

**Primary:** Difference-in-differences (DiD) exploiting a 2024 platform feature rollout that changed feedback-intensity defaults for a subset of cohorts. (Citation: Angrist & Pischke 2009 for DiD; Cunningham 2021 for staggered-adoption corrections.)

**Backup identification:** Regression discontinuity (RDD) at the platform's existing engagement-tier threshold, if a meaningful policy break exists at the threshold.

## 4. Setting and participants

- Population: members joining the platform between 2022-01 and 2024-12.
- Sampling: full population (no sampling — N≈50,000).
- Inclusion: members with ≥30 days of platform exposure.
- Exclusion: bot accounts (per platform's bot-flagging heuristic); accounts banned within 30 days.
- Justification: full-N analysis, with subgroup checks for small-cell stability.
- Recruitment: n/a (secondary data).

## 5. Data collection

- Source: platform admin tables (read-only access via signed DPA).
- Variables: feedback-received count (30-day window), feedback-sentiment (NLP-derived), retention (12-month binary + duration), control variables (join cohort, age tenure on platform, prior engagement signals).
- Timeline: data already collected; analysis window 2026 Q2.

## 6. Analysis plan

- **Primary:** Staggered-adoption DiD with Callaway & Sant'Anna 2021 estimator. Pre-specified.
- **Secondary:** RDD at engagement threshold (labeled as secondary).
- **Outcome models:** Logistic for binary 12-month retention; Cox PH for survival framing.
- **Robust SEs** clustered at the cohort level.
- **Missing data:** listwise (admin data has near-zero missingness by construction; flag any exception).
- **Software:** R, `did` package + `survival` package. Random seeds pinned.

## 7. Creative AI / ML / Big Data Extensions *(mandatory — see Phase 5)*

| # | Idea | Bucket | Fit (H/M/L) | Data needed | Skills / tooling | Validation | Ethical | Why not |
|---|---|---|---|---|---|---|---|---|
| 1 | NLP-classify feedback content (constructive vs critical vs supportive) using BERTopic | NLP/CV/multimodal | H | Feedback text (already in admin data) | Python, sentence-transformers, BERTopic | Hand-code 200 feedback excerpts; agreement κ ≥ 0.7 | Re-identification risk low (anonymized) | Worth doing |
| 2 | Causal forests for heterogeneous treatment effects (which subgroups are most retention-sensitive to feedback intensity) | Causal ML | H | Same admin data + covariates | R `grf` package | Compare to interaction terms in main DiD | Same as #1 | Worth doing |
| 3 | Agent-based simulation of community dynamics as theory test | Generative/simulation | M | Community-structure parameters | Mesa (Python) or NetLogo | Compare simulated to observed retention curves | n/a | Theory-test exercise, not empirical evidence |
| 4 | Survival analysis as alternative outcome operationalization (time-to-attrition rather than binary retention) | Predictive ML | H | Same admin data | R `survival` package | Compare to logistic results | n/a | Already in primary plan as secondary |
| 5 | Platform-network embedding to define "active community membership" instead of binary retention | New data sources / predictive ML | M | Member-interaction graph data | node2vec or GraphSAGE | Compare against retention-based labels | Re-identification via graph structure — verify with platform DPO | High-value but adds scope |
| ⭐ Stretch | **Pre-register the question as an open prediction challenge** for the IS research community — competing models on shared held-out platform data, with the platform as a co-author | various | M | Coordination with platform + IS conference | Substantial — partnership work | Pre-registration on OSF + community participation | Platform consent + author co-authorship governance | High effort but meaningful methodological contribution |

**Researcher decision:** Adopt #1 (NLP feedback classification) and #2 (causal forests for heterogeneous effects) as planned secondary analyses. #5 (graph embedding) as future-work alternative outcome. #3 simulation deferred — would require a separate methods paper. Stretch idea (challenge) flagged for advisor discussion before committing.

## 8. Ethics

- IRB status: Exempt determination expected (anonymized secondary admin data, no contact with members). Submit for confirmation before analysis.
- Consent: Members consented to platform's research-use clause at registration; verify scope.
- Confidentiality: Data accessed via signed DPA; analysis on platform-provided sandbox or local with encryption.
- Risks + mitigations: Re-identification risk minimal but non-zero — apply standard k-anonymity check for any subgroup analysis with small cells.

## 9. Threats to validity / trustworthiness

- **Internal:** Selection — members who join during the feature-rollout window may differ from baseline. Address via comparable pre-rollout cohort + parallel-trends test.
- **External:** Generalizes to this platform; transfer to other communities depends on community-norm similarity. Flag in Limitations.
- **Construct:** "Feedback intensity" operationalized as count; ignores quality. NLP extension (#1 above) addresses this.
- **Statistical conclusion:** Multiple comparisons across subgroups — pre-specify family-wise correction (Benjamini-Hochberg) and label any post-hoc analyses.

## 10. Researcher positionality

n/a — quantitative study with no interpretive coding.

## 11. Pre-registration

OSF pre-registration to be filed before analysis starts. Specify: hypothesis, primary test (DiD with C&S estimator), secondary tests (RDD, Cox PH), success criterion (significance + meaningful effect size), exploratory analyses (NLP classification, causal forests) labeled as such.

## 12. Limitations (anticipated)

- Single-platform generalizability.
- Self-selection into the platform — population isn't randomly sampled from "people who would benefit from feedback."
- Feedback "intensity" is a count, not a quality measure (addressed via NLP extension).
- Identification depends on the feature rollout being effectively exogenous from member characteristics — placebo tests recommended.
