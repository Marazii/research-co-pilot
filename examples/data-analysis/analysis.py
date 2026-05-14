"""Synthetic example analysis script (illustrative only — toy N).

Real use would have N in the hundreds or thousands; this 12-row file just
demonstrates the script structure the data-analysis skill produces.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

DATA = Path(__file__).parent / "input.csv"
np.random.seed(42)  # pinned

df = pd.read_csv(DATA)

# --- Phase 2: inspection ---
print("Shape:", df.shape)
print("\nDtypes:")
print(df.dtypes)
print("\nMissing per column:")
print(df.isna().sum())
print("\nSample:")
print(df.head())
print("\nDescriptives:")
print(df[["pre_test", "post_test"]].describe())

# --- Phase 4: EDA ---
# Treatment-group means
print("\nTreatment-group means (post_test):")
print(df.groupby("treatment")["post_test"].agg(["mean", "std", "count"]))

# --- Phase 5: Model ---
# Baseline OLS
ols = smf.ols("post_test ~ pre_test + treatment", data=df).fit()
print("\n--- OLS (baseline; ignores clustering) ---")
print(ols.summary())

# Mixed-effects model — random intercepts for classroom nested in school
# (For this toy N, this model is unidentified; in real use, this is the right
# specification once you have meaningful between-cluster variance.)
try:
    mlm = smf.mixedlm(
        "post_test ~ pre_test + treatment",
        data=df,
        groups=df["school_id"],
        re_formula="~1",
    ).fit(reml=True)
    print("\n--- Mixed-effects model (school random intercept) ---")
    print(mlm.summary())
except Exception as exc:
    print(f"\nMixed model failed on toy N (expected): {exc}")
    print("In real use with N>>4 clusters this specification fits cleanly.")

# --- Phase 6: Effect-size + CI ---
# Cohen's d for the treatment effect from OLS estimate
beta = ols.params["treatment"]
se = ols.bse["treatment"]
ci_lo = beta - 1.96 * se
ci_hi = beta + 1.96 * se
pooled_sd = df["post_test"].std()
cohens_d = beta / pooled_sd
print(f"\nTreatment effect: {beta:.2f} points (95% CI [{ci_lo:.2f}, {ci_hi:.2f}])")
print(f"Cohen's d (approx): {cohens_d:.2f}")
print("In real analysis with adequate N, report the mixed-model estimate, not OLS.")
