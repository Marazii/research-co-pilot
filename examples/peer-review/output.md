# Peer Review: "How Online Communities Shape Trust"

> **Synthetic example review.** Illustrative format only. Real reviews are typically 1000-3000 words on a full manuscript.

**Reviewer:** Reviewer (simulated, social psychology persona)
**Manuscript:** "How Online Communities Shape Trust" — excerpt
**Mode:** Paper verdict
**Discipline detected:** Empirical social psychology
**Language:** English

---

## Header

The manuscript investigates a topical question (online communities and media trust) with a college-sample survey design. The writing is clear and the analytic framework is straightforward. However, the excerpt contains substantial methodological and interpretive overreach that, if reflective of the full paper, would warrant major revisions before publication.

This review evaluates: the causal-inference claims, the analytic transparency, the framing of subgroup analyses, and the broader-population claims in the discussion. (Full review of a full manuscript would also evaluate: literature review, hypothesis specification, ethics, pre-registration status, and limitations sections.)

## Strengths

1. **Clear, accessible writing.** The abstract communicates the central claim and findings concisely. The manuscript will be easy to read for a broad social-psych audience.
2. **Sensible primary measure.** Regressing trust on community participation with age / gender / education controls is a reasonable starting analytic move.
3. **The phenomenon matters.** Media trust is a high-stakes social-science topic with policy implications, and the paper engages a real-world question rather than a contrived laboratory effect.

## Major issues

### M1. Causal-language overreach

The abstract and discussion repeatedly use causal language ("causally increase," "establish a strong causal link") that the methods do not support. The design is a cross-sectional survey with no instrumentation, no temporal ordering, no within-subject variation, and no quasi-experimental identification. The β = 0.34 estimate is an *association*, not a causal effect.

**What's needed:** rewrite the abstract and discussion to use associational language ("is associated with") rather than causal ("increases"). The paper can still be useful as documentation of a robust association without overclaiming.

### M2. Subgroup analyses framing

The Results section states "this association being significant for all subgroups examined" without listing the subgroups, the cell sizes, the effect sizes per subgroup, or whether multiple comparisons were corrected. This raises three concerns:
- Family-wise error: how many tests were run?
- Selective reporting: which subgroups were tested and which omitted from reporting?
- Pre-registration: were these subgroup analyses pre-specified?

**What's needed:** a complete subgroup table with N per cell, effect sizes with 95% CIs, multiple-comparison correction or explicit "exploratory" labeling, and pre-registration check.

### M3. The "non-significant moderator" interpretation

The interaction with political ideology is reported as non-significant (p = .12) and interpreted as showing "the effect is uniform across the political spectrum." This is a classic absence-of-evidence vs evidence-of-absence error. Non-significance with N = 412 doesn't establish uniformity — only that the design was underpowered to detect the moderator. The 95% CI on the interaction term would tell the reader much more than the p-value.

**What's needed:** report the interaction estimate with its 95% CI, and acknowledge whether the design was powered to detect plausible moderator effect sizes.

### M4. External-validity claims unanchored to sample

The discussion's policy implications ("policymakers should encourage community-based news consumption") assume the finding generalizes well beyond the studied sample. The sample is a college-aged subject pool (ages 18-34) at a single institution. The discussion does not address whether the association would hold among older adults, less-educated populations, or in non-US democracies — populations whose trust dynamics may differ substantially from college samples.

**What's needed:** scope the policy implications to the population the data actually represent, OR establish generalizability with separate samples, OR move policy implications to a clearly-labeled "speculative implications" subsection.

## Minor issues

1. **Abstract — sample description.** "412 participants" omits the population description; specify "young adults" or "college-aged" so a reader understands the sample.
2. **Methods — recruitment incentives not disclosed.** State whether participants received compensation; this affects sample composition.
3. **Results — table or figure of the primary association.** The β alone is hard to interpret; a scatter plot or coefficient-with-CI figure would help.
4. **Discussion — "future research should explore additional populations" is the textbook generic future-direction.** Replace with a specific next study (e.g., "a longitudinal panel of community joiners in their first 12 months").
5. **Citation density appears low for the topic.** Trust in media is a heavily-studied topic; the manuscript should engage with prior empirical work more substantively.
6. **Effect size in plain language absent.** β = 0.34 is interpretable to a methodologist but not to a policy audience. Add a counterfactual translation ("members who participate in communities daily report trust scores 0.5 SD higher than non-participants").

## Brilliance suggestions

1. **Pre-register a follow-up longitudinal study.** The cross-sectional limitation is the paper's biggest weakness. A pre-registered 12-month longitudinal panel of new community members would convert this from association to plausible causal evidence and would strengthen the paper's contribution to the field substantially.
2. **Engage the "trust is downstream of identity-fit" hypothesis.** A growing line of work argues that what looks like trust-by-participation is actually trust-by-identity-fit (people seek communities that match their pre-existing trust dispositions). A serious moderator analysis exploring identity-fit measures would make this paper a much stronger contribution.
3. **Open data + materials would substantially elevate the contribution.** The paper would be a strong candidate for an OSF deposit of the analysis pipeline and (de-identified) data, given the topic's policy salience.

## Verdict

**Major revisions required.**

The paper has a reasonable core finding but needs to (a) abandon causal language that the design does not support, (b) provide transparent subgroup-analysis reporting, (c) revise the moderator interpretation to address the absence-of-evidence problem, and (d) scope the policy implications to the sample's actual generalizability. The list of major issues is substantive but addressable. The strengths — clarity, topical importance, sensible measurement — are real and worth preserving in revision.

## Forward-looking notes

- The cross-sectional → longitudinal pivot (Brilliance #1) would convert this from a marginal contribution to a meaningful one. If the authors are early-career, the longitudinal follow-up could become a stronger second paper rather than retrofitting this one.
- The identity-fit moderator framing (Brilliance #2) is increasingly important in this literature and represents an opportunity for the authors to engage rather than defend against.

---

## Annotated source file

For DOCX input: the structured review above is delivered in chat. The skill would also produce `manuscript_REVIEWED.docx` with:

- ~12 inline comments anchored at the specific text spans in the manuscript (e.g., "These results demonstrate that online communities causally increase media trust" → inline comment: *"M1. Causal-language overreach. The design is cross-sectional with no identification strategy; this claim cannot be supported. Recommend rewrite as 'is associated with.'"*)
- ~6 tracked-changes line-level edits (typo fixes, wording improvements offered as accept/reject changes)
- Every annotation carries the "Reviewer" author tag for filtering in Word's Review pane.

For this excerpt, the annotated file would render the M1–M4 + minor issues + brilliance suggestions inline. For PDF input: native PDF annotations (sticky notes + highlights + strikethrough) at the same locations via PyMuPDF.

---

*This review is illustrative. A real peer review on a real full manuscript would be longer in some sections (e.g., M1 might cite 3-5 papers showing how cross-sectional designs misidentify causal effects) and would include literature-review/methods/ethics sections evaluated against discipline-specific standards.*
