# Research Brainstorm: Misinformation and Trust in News

> **Synthetic example.** Illustrative. Topic and constraints from input.

**Stage:** PhD-2, dissertation chapter 2.
**Constraints:** quant department; panel + experiments available; avoid descriptive belief studies.

## Landscape (brief)

Mainstream story: misinformation exposure is widespread; correction-effectiveness is mixed; partisan asymmetry is contested. Dominant methods: survey experiments + corpus studies. Adjacent fields with leverage: behavioral economics, network analysis, computational text analysis. Open debates: backfire-effect replication failures; the "rational misinformation" account (people share strategically rather than from belief); whether AI-generated misinformation is meaningfully different.

## Long list (18 candidates)

1. **Causal** — Does pre-bunking (vs debunking) reduce sharing-behavior more durably?
2. **Causal** — Does platform-design intervention (e.g., friction on share button) reduce misinformation propagation? Quasi-experiment exploiting platform A/B.
3. **Mechanistic** — Is the misinformation-belief gap better explained by motivated reasoning or by selective exposure? Disentangle via instrumental variable.
4. **Predictive** — What features of a news article predict its spread on partisan networks? ML on labeled corpus.
5. **Comparative** — How does misinformation diffusion differ across democracies with different media-trust baselines?
6. **Critical** — Whose interests does the current academic framing of "misinformation" serve? Who is positioned as the misinformer, who as the misinformed?
7. **Constructive** — Design a journalist-corrections-attribution intervention that scales (corrections labeled with source-trust signals).
8. **Methodological** — Are survey-based misinformation measures construct-valid? Triangulate with behavioral measures.
9. **Inverted assumption** — What if misinformation belief is consequentially over-stated in survey research? Test with behavioral validation.
10. **Boundary condition** — Under what conditions does correction *succeed*? Identify the subgroups where it works.
11. **Negative result** — Replication of the backfire effect with adequate power, pre-registered.
12. **Population inversion** — Most studies sample US adults; what about non-Western democracies, elites, or platform-moderators?
13. **Question-behind** — Bigger: how do entire epistemic ecosystems calibrate trust? Smaller: how does one person's trust evolve over a 3-month news consumption period?
14. **Real-world hook** — The 2024 election cycle produced a wave of AI-generated content; pre-registered analysis of its share-rate vs. human-generated misinformation.
15. **Causal ML graft** — Causal forests for heterogeneous treatment effects of correction-intervention across user types.
16. **Behavioral econ graft** — Treat misinformation-sharing as signaling rather than belief; predict sharing from social-status incentives.
17. **NLP graft** — Embed misinformation articles in semantic space; do certain semantic neighborhoods spread differently?
18. **Stretch** — Pre-register an open prediction challenge: which model best predicts misinformation spread on shared corpus.

## Scored (top 7)

| # | Idea | Interesting | Answerable | Novel | Feasible | Total |
|---|---|---|---|---|---|---|
| 8 | Construct validity of survey measures | 4 | 4 | 4 | 5 | 17 |
| 11 | Pre-reg backfire replication | 4 | 5 | 3 | 5 | 17 |
| 15 | Causal forests on heterogeneous correction effects | 5 | 4 | 5 | 3 | 17 |
| 1 | Pre-bunking vs debunking durability | 4 | 4 | 4 | 4 | 16 |
| 14 | AI-generated vs human-generated misinformation spread | 5 | 3 | 5 | 3 | 16 |
| 18 | Open prediction challenge (stretch) | 5 | 3 | 5 | 2 | 15 |
| 6 | Critical framing of misinformation discourse | 4 | 3 | 4 | 4 | 15 |

## Sharpened top 3

### Idea 8: Construct validity of survey misinformation measures

**Research question:** Do standard survey misinformation-belief measures (typically yes/no on a list of claims) predict actual sharing behavior in a controlled platform-mimicking task?
**Why it matters:** Most of the misinformation literature uses survey measures. If they don't predict behavior, a large body of findings is on shaky ground.
**What's known:** Almost no construct-validation studies of these instruments.
**Gap / contribution:** The first construct-validity study linking survey response to behavior.
**Design:** Online study, N=2,000. Random misinformation-belief survey + a delayed behavioral task (mock social feed). Pre-registered.
**Predicted finding (and the contrary):** Modest correlation (r=0.3-0.5). If higher, current literature is on safer ground than I think. If lower, time to rethink.
**Risks:** Mock social feed may not capture real sharing motivations. Pre-pilot with 100 to check ecological validity.
**Follow-on:** Behavioral measure becomes a standard supplement to survey instruments.

### Idea 11: Pre-registered backfire-effect replication

**Research question:** Under what conditions does corrective information increase belief in the corrected claim (the backfire effect)?
**Why it matters:** The original backfire findings (Nyhan & Reifler 2010) have not replicated cleanly; the literature is in flux.
**What's known:** Multiple failed replications; one or two successful ones in specific conditions.
**Gap / contribution:** A pre-registered, adequately-powered, modern replication with the original stimuli and analysis.
**Design:** Pre-registered replication on Prolific, N=1,200 per condition (5x original N). OSF preregistration before data.
**Predicted finding:** Null effect under the original conditions; possible effect under high-identity-salience condition.
**Risks:** Stimuli may have aged (2010 political content); validate with pilot.
**Follow-on:** Could become a Many-Labs-style coordinated replication.

### Idea 15: Causal forests for heterogeneous correction effects

**Research question:** Which subgroups respond to corrective information, and which don't? Pre-specify subgroup discovery with causal forests.
**Why it matters:** The "do corrections work?" question is the wrong unit; subgroup heterogeneity is the real story.
**What's known:** Some moderator analyses exist (partisanship, prior belief), but they're hypothesis-driven rather than data-driven.
**Gap / contribution:** First systematic application of causal-forest HTE methods to correction-intervention data.
**Design:** Reanalysis of an existing large correction-experiment dataset (request from authors); replication on a new experiment.
**Predicted finding:** Strong heterogeneity, with high-trust-in-experts subgroup showing largest correction effect.
**Risks:** Causal forests overfit; report held-out validation. Available data may not be granular enough.
**Follow-on:** Methodological contribution to the political-communication toolkit.

## Recommendation

Idea 8 (construct validity) is the most defensible dissertation chapter — high novelty, high feasibility, the kind of question a quant committee will reward. Idea 11 (backfire replication) is also defensible and lower-risk methodologically. Idea 15 (causal forests) is the most methodologically interesting but adds skills risk and computational complexity.

Most-promising sequence: **Chapter 2 = Idea 8** (construct validity); **Chapter 3 = Idea 11** (replication, using the validated measures from Ch. 2 as a check); **Chapter 4 = Idea 15** (heterogeneity, applied to your own data from Ch. 2 + 3).
