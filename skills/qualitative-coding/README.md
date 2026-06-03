# qualitative-coding

> Codebook development and application using thematic analysis, grounded theory, IPA, framework analysis, or content analysis. Inter-rater reliability (Cohen's κ, Krippendorff's α). NLP-assisted exploration for large corpora — with required validation against hand-coding.

**Triggered by:** `/code-themes`, plus *"thematic analysis"*, *"code transcripts"*, *"build a codebook"*, *"find themes"*, *"grounded theory"*, *"inter-rater"*, *"NLP on transcripts"*, *"topic modeling"*.

**Inputs needed:**

- Transcripts or open-ended response data (paths to files, or pasted text for short corpora).
- Research question + the analytic tradition you're using (thematic / grounded theory / IPA / framework / content / discourse).
- Approach: inductive (codes from data) / deductive (from theory) / hybrid.
- Pre-existing codebook if any; otherwise the skill develops one.
- For team coding: whether inter-rater reliability is needed.

**Output:**

- A codebook (`codebook_v1.md`, versioned as it evolves).
- Coded data (JSON or markdown, one entry per excerpt with location reference, applied codes, and memo).
- Anonymization key file (kept separate, never returned to chat).
- Themes report (`qualitative_findings_<project>.md`) with theme names, essences, illustrative quotes (with participant IDs), prevalence, disconfirming cases, and reflexivity statement.
- For NLP-assisted work: a separate report distinguishing model-generated outputs from hand-validated codes.

**Introduced in:** [v0.1.0](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you have interview transcripts, focus groups, field notes, open-ended survey responses, or document data and need a defensible thematic analysis. Particularly useful when the corpus is too large to hand-code fully (where NLP-assisted exploration surfaces patterns to investigate by hand), when team coding requires IRR computation, when responding to a reviewer who asked for "more rigorous qualitative analysis," or when you want an explicit audit trail of every analytic decision.

It is not a substitute for the interpretive labor of a careful qualitative researcher — it scaffolds the work, applies discipline, and computes the technical bits. The interpretation remains yours.

## Example

**Input:** *"18 interview transcripts in `./transcripts/`, study of post-pandemic remote-work decisions. Want a reflexive thematic analysis (Braun & Clarke). Solo coder. Inductive."*

**Output:**

1. Anonymization pass produces standardized transcripts in `./transcripts_clean/` with placeholder names ([NAME_1], [ORG_2], etc.) and an anonymization key kept off-system.
2. Familiarization read with brief reactions.
3. Initial codebook with ~40 codes, each defined with inclusion / exclusion criteria and 2-3 verbatim example excerpts.
4. Coded JSON across all 18 transcripts with location references (`P03:142-148`).
5. Theme construction into 5 candidate themes; iteration after reviewing against the full corpus.
6. Final report with theme essences, illustrative quotes, prevalence (which themes appeared in how many participants), disconfirming cases addressed explicitly, and a reflexivity statement.

See [`examples/qualitative-coding/`](../../examples/qualitative-coding/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `.research/` workspace contract live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`literature-review`** — Lit-review identifies the theoretical framework that informs deductive coding (e.g., a Job Demands-Resources lens).
- **`methodology-advisor`** — Methodology specifies the qualitative tradition; this skill executes within it.
- **`transcript-coder` subagent** — For large corpora (more than ~10 transcripts) or for batch cleaning/anonymization, the parent skill spawns the transcript-coder subagent.
- **`manuscript-drafter`** — The themes report feeds directly into manuscript-drafter's Findings section, preserving voice and quote attribution.

## Honest caveats

- **NLP outputs are exploratory.** Topic modeling, sentiment classification, and LLM-assisted coding are scaffolds; outputs need validation against hand-coded subsets before being treated as analytic findings. The skill enforces this.
- **The interpretive labor is yours.** The skill enforces an audit trail and applies codes consistently, but theme construction is interpretive — your judgment, not the model's, defines the themes.
- **Reflexivity** statements are scaffolded; you write the substantive content. The model can't know your positionality.
- **Inter-rater reliability targets** are defaults (κ ≥ 0.80 strong, 0.60-0.79 substantial); your discipline's conventions may differ.
- **Discourse analysis** is supported with standard conventions but is shallower than the other traditions; treat it as scaffolded if your study centers on linguistic analysis.
- **Computational text analysis** with large NLP pipelines (transformer fine-tuning, custom embeddings) is supported conceptually but execution depends on your environment's compute. Heavy work delegates to the data-cruncher subagent.
