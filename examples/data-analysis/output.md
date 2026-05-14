# Analysis: Treatment Effect on Post-Test, with Cluster Structure

> **Synthetic example.** Toy N (12 students). Output structure illustrative.

## 1. Question

Does the treatment improve post-test scores, controlling for pre-test, accounting for clustering of students within classrooms within schools?

## 2. Data

- N = 12 students, 4 classrooms, 2 schools.
- No missingness.
- Pre-test range 65–82; post-test range 68–88.
- Cleaning: none required (toy data).

## 3. Methods

- Baseline OLS for orientation.
- Mixed-effects linear model with random intercepts for school (and ideally classroom-within-school for adequate N) — `statsmodels.formula.api.mixedlm`. For this toy N the random structure isn't identified; the script flags this honestly.
- Software: Python 3.11, statsmodels 0.14, pandas 2.0. Seed: 42 (pinned).
- Pre-specified: treatment as primary effect with pre-test as covariate. Mixed-effects specification pre-registered as the right model for the clustered design.

## 4. Results

**Headline (from OLS baseline; would use mixed-model in real-N study):**

| Estimate | Value | 95% CI | Notes |
|---|---|---|---|
| Treatment effect (post_test) | +5.4 points | [+2.1, +8.7] | Adjusted for pre-test |
| Cohen's d | ≈ 0.95 | — | Large effect, but toy N |

**Diagnostic notes:**
- Toy N too small for residual diagnostics, mixed-model convergence, or robust inference.
- In real use: would report residuals-vs-fitted plot, Q-Q plot, ICC for the school random intercept, and likelihood-ratio test comparing OLS to mixed-model.

## 5. Sensitivity (real-use template)

| Specification | Treatment estimate | 95% CI | Change vs main |
|---|---|---|---|
| Main (mixed, school + classroom random) | +X.X | [..., ...] | (baseline) |
| OLS ignoring clusters | +X.X | [..., ...] | — |
| Robust SEs (HC3) | +X.X | [..., ...] | — |
| Drop influential observations | +X.X | [..., ...] | — |

## 6. Interpretation

Toy data; interpretive claims out of scope. In real use, the report would:
- State the point estimate with units.
- Pair it with the 95% CI.
- Report Cohen's d and discuss whether the magnitude is practically significant.
- Caveat the inference (cluster-corrected SE, generalizability, alternative specifications).

## 7. Limitations

- Toy N. Real analysis requires N >> 30 per cluster for stable mixed-effects estimates.
- Single time-point; no pre-registered intervention; observational at best.

## Reproducibility

```
python analysis.py
```

Outputs print to console. Script at `analysis.py`; data at `input.csv`. Random seed pinned (42).
