# Domain lenses for peer review

This file is a template for articulating rigor criteria in any academic field, plus worked examples for several diverse fields. It is illustrative, not exhaustive. The skill is meant to handle any domain (humanities, social sciences, natural sciences, engineering, arts, professional disciplines), not just the ones listed here.

## How to use this file

1. Identify the field(s) the work is operating in (Step 3 in SKILL.md). Pick the granularity at which rigor criteria meaningfully differ from neighboring fields (philosophy of mind, not "philosophy"; evolutionary developmental biology, not "biology").

2. For each field, articulate the rigor criteria a careful reviewer in that field would apply. Use the universal template below. Use the worked examples as references for what the output should look like.

3. State the criteria explicitly in the review (or in reasoning before drafting), so the author can see what standards are being applied.

If the field is one of the worked examples, use it directly. If not, generate criteria following the template.

## Universal template

Every field's rigor criteria fall into roughly these categories, though the content varies enormously:

- **What counts as a contribution.** What does this field consider a meaningful new claim? Originality, novelty, advance, refinement, synthesis, replication, application: each field weights these differently.
- **What counts as evidence.** Empirical data, archival sources, formal proof, textual analysis, ethnographic observation, computational results, expert testimony: each field has its own admissible evidence.
- **Methodological standards.** The methods the field has agreed produce reliable knowledge, plus the typical pitfalls and how to avoid them.
- **Engagement with the literature.** Which traditions, schools, or canonical works must be engaged with? Which counter-positions must be addressed? Which prior critiques cannot be ignored?
- **Argument structure.** What does a well-formed argument look like in this field? Validity, soundness, internal consistency, falsifiability, where applicable.
- **Conceptual clarity.** Are key terms defined, used consistently, and grounded in the field's existing vocabulary (or, if neologistic, justified)?
- **Scope and generalization.** What kinds of claims can this kind of work support? Where does this work overreach or underreach?
- **Reproducibility, transparency, or verifiability** (where applicable). Can someone else reproduce, verify, or check the work?
- **Specific failure modes the field knows to watch for.** Every mature field has characteristic mistakes that come up over and over. A reviewer in that field knows them.
- **Distinctive features.** What does this field uniquely care about that others do not?

For interdisciplinary work, apply multiple lenses; tensions between them often surface real issues.

## Worked examples

The following are examples, not the canonical list. They span humanities, social science, natural science, engineering, and applied fields. Generate analogous criteria for any field not listed.

### Philosophy

- Argument validity: do the conclusions follow from the premises?
- Argument soundness: are the premises true or well-defended?
- Conceptual clarity: are key terms defined and used consistently?
- Distinction between conceptual and empirical claims.
- Engagement with the literature: are the obvious objections addressed?
- Originality of thesis: is the author saying something new, or restating a known position?
- Response to objections: does the paper anticipate and address the strongest counter-arguments?
- Use of examples and thought experiments: are they doing real argumentative work?
- Attention to fallacies: equivocation, straw-manning, false dichotomies, conflations, question-begging.
- Argumentative structure: is the chain of reasoning explicit?

### Philosophy of mind and consciousness studies

- Conceptual hygiene around "consciousness": phenomenal vs. access vs. self-consciousness distinctions.
- Position on the hard problem: explicit (illusionist, physicalist-reductive, non-reductive physicalist, dualist, panpsychist, mysterian)?
- Engagement with major theories: IIT, Global Workspace, Higher-Order, Predictive Processing, Attention Schema, Recurrent Processing.
- Empirical grounding: where neuroscience is invoked, is it argumentatively load-bearing or ornamental?
- Methodology of consciousness experiments: appropriate handling of CFS, masking, blindsight, binocular rivalry, no-report paradigms.
- Treatment of first-person evidence and the limits of introspection.
- Circularity checks on operationalizations of consciousness.
- Functional vs. phenomenal claims about machine consciousness.
- Distinction between metaphysical and empirical questions.

### Empirical psychology

- Research design appropriate to the question (RCT, observational, correlational, qualitative, mixed-methods).
- Operationalization of constructs: validity, reliability.
- Sample: size, demographics, recruitment, generalizability, WEIRD-sample issues.
- Statistical rigor: appropriate tests, effect sizes, confidence intervals, multiple comparisons, power, p-hacking concerns.
- Replicability and pre-registration.
- Theoretical framing and engagement with alternative theoretical lenses.
- Alternative explanations: confounds, demand characteristics, selection effects, reverse causation.
- Ecological validity.
- Ethical handling.

### History

- Archival sourcing: are primary sources used? Well-chosen, with documented access?
- Engagement with secondary literature: which historiographical tradition is the author working in?
- Periodization and contextualization: does the framing fit the period, or impose anachronistic categories?
- Causality and contingency: is the historical explanation appropriately complex, or reductive?
- Treatment of competing interpretations: is historiographical disagreement engaged with?
- Narrative construction: is the narrative serving the evidence, or vice versa?
- Reflexivity about the historian's position and present-day concerns shaping the past.
- Linguistic competence where relevant: are sources read in their original languages?
- Contribution: does this re-read sources, surface new ones, reframe a debate, or apply a new method?

### Chemistry (experimental)

- Experimental design: are controls appropriate? Replicates included? Variables isolated?
- Characterization: are products characterized by appropriate methods (NMR, IR, MS, X-ray, etc.) at appropriate purity?
- Yield reporting: honest, reproducible, reported with standard deviations across runs.
- Mechanism proposals: supported by evidence, or speculative?
- Comparison to literature: is the work positioned against existing methods or syntheses fairly?
- Reproducibility: procedures detailed enough to repeat; starting materials and conditions specified.
- Safety considerations addressed where relevant.
- Specificity and generality of claims: scope clear?

### Biology (cell or molecular)

- Hypothesis-driven framing or hypothesis-generating, with the distinction stated.
- Experimental controls: appropriate positive and negative controls; vehicle controls; loading controls.
- Replicates: biological vs. technical replicates distinguished; n stated meaningfully.
- Statistical analysis appropriate to the data type and distribution.
- Imaging integrity: not manipulated beyond standard adjustments; representative images actually representative.
- Cell line authentication and mycoplasma testing where relevant.
- Antibody validation.
- Animal use ethics where relevant.
- Translation claims (mouse to human, in vitro to in vivo) calibrated.

### Civil engineering (structural)

- Standards compliance: relevant codes (ACI, AISC, Eurocode, ASCE) cited and followed.
- Load assumptions: appropriate dead, live, environmental, seismic loads; load combinations correct.
- Material properties: appropriate values, sourced from standards or testing.
- Analysis methods: appropriate for the structure type; assumptions stated.
- Safety factors: appropriate; not erroneously stacked or omitted.
- Failure modes considered: primary, secondary, tertiary; brittle vs. ductile.
- Constructability and serviceability addressed alongside ultimate-state.
- Validation: comparison with established cases, FE results, or experiments.

### Computer science (systems and methods papers)

- Novelty: what is new? Is the contribution clearly stated and bounded?
- Comparison to baselines, prior work, state-of-the-art: fair, current, adequately documented.
- Ablations: which components contribute what? Informative ablation studies present.
- Reproducibility: code, data, hyperparameters, random seeds, hardware.
- Evaluation methodology: metrics appropriate to the task; reported with variance.
- Theoretical analysis (where applicable): proofs correct, bounds tight, assumptions reasonable.
- Engineering vs. research contribution: claim type matches evidence type.
- Limitations and failure modes honestly discussed.
- Clarity of system description: reproducible from the description.

### Economics (empirical)

- Identification strategy: how is causality established? IV, RCT, RDD, natural experiment, DiD, structural?
- Threats to identification: addressed honestly.
- Pre-registration where applicable.
- Robustness checks: alternative specifications, alternative samples.
- External validity: from this setting to which others, and how?
- Standard errors clustered at the right level.
- Theoretical model (if structural) plausible and testable.
- Engagement with the relevant prior literature.
- Policy implications calibrated to the evidence.

### Comparative literature or literary studies

- Close reading: textual evidence cited with appropriate granularity.
- Theoretical framework: which tradition (formalist, structuralist, poststructuralist, feminist, postcolonial, queer, materialist, etc.)?
- Engagement with secondary criticism on the works in question.
- Original languages where the work is comparative across languages.
- Periodization and contextualization.
- Distinction between authorial intent, textual operation, and reader reception.
- Originality of reading vs. recapitulation.
- Argumentation supporting interpretation: is the reading defended or merely asserted?

### Music theory or musicology

- Score engagement: actual analysis of musical material, not just description.
- Analytical method: which tradition (Schenkerian, set theory, neo-Riemannian, transformational, ethnomusicological, sociological)?
- Engagement with the analytical literature on the work or repertoire.
- Distinction between analytical claim, historical claim, and aesthetic claim.
- Examples: properly notated, accurately transcribed, supportive of the argument.
- Sound and recording engagement where relevant.
- Cultural and historical context.

### Public health or epidemiology

- Study design appropriate to the question.
- Sample and population: well-defined, representative of the inference target.
- Confounding controlled appropriately.
- Effect modification considered.
- Causal inference (where claimed) supported by design.
- Statistical analysis appropriate.
- Ethics: IRB, consent, vulnerable populations.
- Generalizability: from this population to which others?
- Public-health implications calibrated.

### Gender studies

- Theoretical framework: which feminist tradition (liberal, radical, postmodern, intersectional, materialist, queer, etc.)?
- Sex/gender distinction: how does the author handle this?
- Intersectionality: are race, class, sexuality, disability, and other axes considered where relevant?
- Positionality: does the author reflect on their own standpoint?
- Empirical grounding where applicable: how is gender operationalized? Binary, mosaic, spectrum, identity-based, body-based?
- Engagement with critique-of-gender-studies literature.
- Awareness of contemporary work on gender as mosaic vs. dimorphism where relevant.
- Distinction between descriptive claims about gender and normative claims about gender.
- Treatment of trans and non-binary populations where relevant.

### AI ethics

- Normative framework: which ethical tradition (consequentialist, deontological, virtue, care, justice-based)?
- Distinction between empirical and normative claims.
- Technical literacy: are claims about AI behavior accurate, or relying on outdated framings?
- Stakeholder analysis: who is affected? Are vulnerable populations considered?
- Counterfactual reasoning: compared to what alternative?
- Specificity of harm: vague harms vs. specific, actionable harms.
- Engagement with the AI ethics literature (FAccT, AIES) not just popular discourse.
- Treatment of contested questions (consciousness, moral status, alignment, where consensus is genuinely absent).
- Power analysis: who builds, who deploys, who benefits, who bears the cost?

## When the field is not a worked example

Construct the criteria following the template. State explicitly in the review what criteria are being applied. The criteria a careful reviewer in the field would apply are not arbitrary: they reflect what the field has learned about how to produce reliable knowledge in that domain. The skill's job is to articulate those criteria competently for whatever field the work is in, even if it is not in the worked-examples list.

For very specialized fields (specific subdisciplines, niche methodological traditions, fields requiring extensive specialist training), the skill may be operating outside its sharpest range. The Step 4 self-limitation check and the Header confidence calibration are where this gets flagged honestly.
