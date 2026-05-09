# Content types: how to evaluate non-prose elements

Apply the relevant lens during Step 4 (reading) and incorporate findings into Sections 3, 4, 5, and 6 of the structured review at the appropriate priority. Non-prose content is content. Skipping it produces incomplete reviews.

## Figures (charts, plots, data visualizations)

What to check:
- **Truthfulness**: does the figure accurately represent the data? Look for truncated y-axes, misleading aspect ratios, cherry-picked time windows, dual-axis plots that imply spurious correlations, log scales unmarked, area charts where length encodes value.
- **Clarity**: is the figure self-explanatory or does it require the reader to hunt for explanation in the text? Are axes labeled with units? Is the legend complete? Are colors used meaningfully or decoratively?
- **Necessity**: does the figure earn its space? A figure that adds nothing the text already says is filler.
- **Consistency with the text**: does the prose accurately describe what the figure shows? A common failure mode is text that describes a stronger pattern than the figure actually displays.
- **Accessibility**: are color choices distinguishable for color-blind readers? Are the smallest text elements readable at print size?
- **Statistical honesty**: are confidence intervals, error bars, or distributions shown where they should be? A bar chart of means with no uncertainty information is a flag.

When to comment in the docx: anchor the comment on the figure caption (Word lets you comment on inline images and their captions).

Common failure modes: chartjunk, misleading scales, decorative figures that don't add information, missing uncertainty, mismatch between figure and prose claim.

## Tables

What to check:
- **Necessity**: is the data better as a table than as prose or a figure? Tables of three numbers are usually prose; tables of comparable measurements across many conditions are usually right.
- **Structure**: are rows and columns organized to support the reader's task? Are headers clear?
- **Completeness**: are units stated? Are sample sizes shown where relevant? Are missing data marked, or just absent?
- **Statistical honesty**: are confidence intervals or standard errors shown? Are p-values reported (and corrected for multiple comparisons where applicable)?
- **Consistency**: numbers in the table must match numbers cited in the prose. Mismatches are flags (and often diagnostic of late-stage edits that did not propagate).

Common failure modes: tables that should have been figures, missing units, missing sample sizes, no uncertainty reporting, prose-table mismatches.

## Equations and mathematical proofs

What to check (depending on reviewer competence; flag in Header if outside it):
- **Correctness**: each derivation step follows. The skill should be honest about its own ability to verify proofs in unfamiliar mathematical territory; if the proof is in advanced category theory or specialized statistics, flag in Header that this requires a domain expert and read what the skill can.
- **Notation**: is notation consistent throughout? Are symbols defined where introduced?
- **Necessary vs. sufficient**: is the proof showing what the prose claims (necessity, sufficiency, equivalence, bound)? A proof of an upper bound being claimed as a tight bound is a real flag.
- **Assumptions**: are assumptions stated explicitly? Hidden assumptions are common.
- **Scope**: does the result apply where the paper claims it does? Edge cases, boundary conditions, and asymptotics should be handled.
- **Connection to prose**: is the equation doing argumentative work, or is it ornamental? An ornamental equation in a paper that does not need formalism is a flag.

Common failure modes: hidden assumptions, notational drift, scope overreach, equations as decoration, results stated more strongly than proven.

## Code blocks and pseudocode

What to check:
- **Correctness**: does the code do what the prose says it does? Read it for off-by-one errors, edge-case handling, undefined behavior, infinite loops, race conditions where relevant.
- **Reproducibility**: is the code complete enough to run? Are dependencies listed? Are random seeds set? Is data preprocessing shown?
- **Idiomatic style**: does the code follow conventions for the language? Non-idiomatic code is harder to verify and a flag for code that may have been generated rather than written.
- **Comments**: are comments load-bearing (explaining non-obvious choices) or noise (restating what the code obviously does)?
- **Pseudocode specifics**: is the pseudocode clear enough to be implemented? Or is it ambiguous on critical operations?
- **Match to prose description**: does the prose accurately describe the algorithm's complexity, behavior, and limitations? An O(n) claim in prose for code that is visibly O(n²) is a real flag.

Reviewer competence note: if the code is in a language outside the reviewer's strong familiarity, flag in Header.

Common failure modes: code that does not match prose, missing dependencies and data, copy-paste errors, hidden state, prose claims about complexity that the code does not support.

## Algorithms and flowcharts

What to check:
- **Completeness**: are all branches accounted for? Termination conditions stated?
- **Determinism vs. nondeterminism**: where the algorithm involves random choices or asynchronous components, is this called out?
- **Match to implementation**: if both an algorithm description and code are present, do they match?
- **Visual clarity**: in flowcharts, are the symbols standard? Is the flow direction consistent?

Common failure modes: missing termination conditions, mismatch between flowchart and code, ambiguous arrows, non-standard symbols.

## Statistical output (regression tables, ANOVA tables, etc.)

What to check:
- **Reporting completeness**: coefficients, standard errors, confidence intervals, p-values, sample sizes, R² or equivalent fit statistics.
- **Reference categories**: in regression tables, the omitted reference category should be stated.
- **Multiple comparisons**: corrected? If not, the p-values should be interpreted with caution.
- **Effect sizes**: present and meaningful? A statistically significant but tiny effect is different from a meaningful one.
- **Match to text**: the prose interpretation must match the table. A coefficient described as "large" should be large.
- **Model specification**: is the model justified? Are interaction terms motivated theoretically or fishing?

Common failure modes: missing standard errors, no multiple-comparison correction, p < .05 reported as the only consideration, prose-table mismatches, model specification fishing.

## Diagrams (conceptual, architectural, system)

What to check:
- **Necessity**: does the diagram clarify something the prose cannot? A diagram of three boxes connected by arrows often does not.
- **Clarity**: are the elements meaningfully distinct? Is the layout principled?
- **Consistency with the text**: does the text describe the diagram accurately? Are all labeled elements explained?
- **Information density**: is the diagram appropriately detailed for its purpose?
- **For system architecture diagrams**: are interfaces specified? Are data flows directional? Are dependencies clear?

Common failure modes: decorative diagrams, inconsistent labeling, unexplained elements, oversimplification or overcomplication.

## Supplementary materials

What to check:
- **Are they actually supplementary?** Material critical to the argument should be in the main text, not in supplements.
- **Reproducibility support**: do supplements include the data, code, materials, and details needed to reproduce the work?
- **Link integrity**: do links to supplements actually work? Broken supplement links are a real flag for both fact-check and substantive review.

Common failure modes: load-bearing analyses hidden in supplements to keep main text clean, unreachable supplement links, supplement contents that contradict main-text claims.

## Annotation guidance for docx

Word lets you anchor comments on inline figures, tables, equations (rendered as objects), and code blocks. When commenting on these elements:
- Anchor the comment on the caption or label, not on individual cells or pixels (more stable across edits).
- Prefix the comment with the content type if helpful: "[FIGURE 3]", "[TABLE 1]", "[EQ. 4]", "[CODE BLOCK]".
- Apply the same volume principle as for prose: comment when there is something substantive to say, not by quota.
