# data-analysis

> End-to-end quantitative data work: cleaning, EDA, statistical testing, modeling, visualization, and reproducible scripts in Python or R. Checks assumptions; reports effect sizes and uncertainty, not just p-values.

**Triggered by:** `/analyze`, plus *"clean this dataset"*, *"fit a regression"*, *"run an ANOVA"*, *"EDA"*, *"power analysis"*, *"sensitivity analysis"*, *"Python script for…"*, *"R script for…"*, *"summary stats"*, *"visualize this data"*.

**Inputs needed:**

- The dataset (CSV / Parquet / SAV / Excel / Stata, or a path to it).
- The research question or analytic goal (descriptive / inferential / predictive / causal).
- Unit of analysis and whether data is independent vs clustered / repeated.
- Pre-existing analysis plan or methodology document if available.
- Language preference (Python / R; defaults to Python).

**Output:**

- `analysis_<topic>.md` report with: question / data summary / methods / results table (effect sizes + CIs, not just p-values) / sensitivity analyses / diagnostics / interpretation / limitations / appendix with full model output.
- Reproducible script saved alongside (`analysis.py` or `analysis.R`).
- Figures saved as PDF / PNG.
- Cleaned data saved as Parquet (preserves dtypes) when applicable.

**Introduced in:** [v0.1.0](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you have data and a question and want a defensible analysis, when reviewer 2 asked for "more rigorous statistics," when you suspect your analysis is missing assumption checks, when you want to switch from p-value-first reporting to effect-size + CI reporting, when you need a baseline sanity-check before fitting fancier models, and when you want a reproducible script + report you can hand to a collaborator.

It is not a substitute for an applied statistician on edge cases (non-standard hierarchical structures, complex survey-weighting, Bayesian model comparison, causal-inference identification arguments that need domain knowledge). Treat its output as a strong default that a specialist would refine.

## Example

**Input:** *"Cleaned CSV at `./data/study2.csv`, N=247 students. Outcome: post-test score. Predictors: pre-test, treatment condition, classroom. Reviewer asked us to account for the clustered structure (students within classrooms within schools)."*

**Output:** `analysis_study2.md` covering data inspection (missingness, dtypes, head sample shown to user), EDA, baseline OLS (which the user had), the appropriate mixed-effects model (`lme4::lmer` or `statsmodels.MixedLM`) with `(1 | school/classroom)` random intercepts, diagnostics (residual checks, ICC, model comparison via likelihood-ratio), effect sizes with 95% CIs, sensitivity analyses (with/without outliers, alternative random-effect specification, robust SEs), and an honest discussion of what changes from the user's original OLS-only result.

See [`examples/data-analysis/`](../../examples/data-analysis/) for a worked sample.

## Composes well with

- **`methodology-advisor`** — The Analysis Plan section of a methodology document is direct input here. The Creative AI / ML / Big Data section often suggests modeling extensions data-analysis can execute.
- **`data-cruncher` subagent** — For heavy computation (many model variants, sensitivity grids, simulation-based power, cross-validation), data-analysis spawns the data-cruncher subagent to work in isolation.
- **`stats-validator` subagent** — For an independent second-look on someone else's analysis (no narrative contamination), spawn stats-validator instead.
- **`manuscript-drafter`** — The analysis report's Results section feeds directly into manuscript-drafter's Results section.

## Honest caveats

- **Assumption checks but not assumption proofs.** If linearity fails subtly, residual plots may not catch it. The skill flags what it can; subtle misspecification needs domain knowledge.
- **Causal claims** require an identification strategy beyond the analysis itself. The skill reports associations and runs the specified models; it does not adjudicate whether a research design supports the causal interpretation. Methodology-advisor does that upstream.
- **Bayesian analysis** is supported (mention `brms` / `pymc` / `Stan`) but not as deeply as the frequentist toolkit. Specify if you want a Bayesian primary analysis.
- **Time-series and survival models** are supported with standard defaults; specialized applications (state-space, joint longitudinal-survival, multi-state) benefit from a domain methodologist.
- **Data with strong privacy constraints** should be anonymized before reaching the model. The skill does not anonymize automatically — use `qualitative-coding`'s anonymization step or your own pipeline first.
