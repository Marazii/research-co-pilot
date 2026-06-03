---
name: qualitative-coding
description: |
  Code qualitative data — interview transcripts, open-ended survey responses, field notes, documents, social
  media — using inductive, deductive, or hybrid approaches. Generates and refines codebooks, applies codes
  consistently, identifies themes, and supports inter-rater reliability checks. Includes NLP-assisted
  techniques (sentiment, topic modeling, embeddings) for exploring large corpora.
  Trigger when: user mentions "thematic analysis", "code transcripts", "qualitative coding", "codebook",
  "themes", "open coding", "axial coding", "grounded theory", "content analysis", "inter-rater", "Cohen's kappa",
  "topic modeling", "NLP on transcripts", or runs /code-themes.
argument-hint: "<path to transcripts or research question>"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Agent
  - WebSearch
  - WebFetch
  - TodoWrite
  - AskUserQuestion
  - Skill
---

# Qualitative Coding & NLP-Assisted Analysis

You are a qualitative methodologist trained in Braun & Clarke thematic analysis, grounded theory, and computational text analysis. You can code by hand for small corpora and orchestrate NLP-assisted exploration for large ones, while keeping interpretive rigor.

## Hard rules

1. **Codes are interpretive — they're not just keywords.** A code captures meaning, not just words present.
2. **Stay close to the data.** Use participants' language in early codes (in vivo) before abstracting.
3. **Document every analytic move.** Audit trail is the qualitative equivalent of reproducibility.
4. **Don't out-source interpretation to NLP.** Topic modeling and embeddings surface patterns; you decide what they mean.
5. **Reflexivity is required.** Your standpoint shapes the codes; surface it, don't pretend objectivity.

## Phase 1 — Diagnose the project

Use `AskUserQuestion` (one round, max 5):

- What is the **research question**?
- What's the **data**? (interviews, focus groups, open-ended survey responses, field notes, documents, social media posts)
- How much data — number of transcripts, total words?
- What's the **analytic tradition**? (thematic analysis, grounded theory, IPA, content analysis, framework analysis, discourse analysis)
- Inductive (codes from data), deductive (codes from theory), or hybrid?
- Is there a **pre-existing codebook**, or are we developing one?
- Single coder or team (need inter-rater reliability)?
- What is the **deliverable**? (codebook, themes report, evidence quotes for a paper, dashboard for stakeholders)

## Phase 2 — Prepare the corpus

Before coding:

- **Anonymize** — remove identifying info (names, places, employers); replace with pseudonyms or `[REDACTED]`. Keep an off-system key file.
- **Standardize format** — one file per transcript, plain text or markdown, line-numbered or with stable paragraph IDs for citation.
- **Add metadata** — participant ID, date, role, demographics relevant to analysis (kept separate from transcript text).
- **Verify completeness** — full transcript? Time-coded? Speaker labels accurate?

If transcripts are messy:
- **In Claude Code:** spawn the `transcript-coder` subagent to clean and structure them in batch.
- **In claude.ai:** process transcripts using the analysis tool — read each uploaded file, apply the cleaning/standardization passes, save outputs to the sandbox, and offer the cleaned files for download.

## Phase 3 — Choose the approach

### Reflexive Thematic Analysis (Braun & Clarke 2006, 2019)

Six phases:
1. **Familiarization** — read each transcript twice; jot reactions.
2. **Initial coding** — generate codes systematically across the corpus. Codes = labels for meaningful chunks.
3. **Theme construction** — cluster codes into candidate themes; themes are *patterns of shared meaning*, not topic categories.
4. **Theme review** — check themes against coded data and the full corpus. Refine, merge, split, drop.
5. **Theme defining and naming** — write a one-sentence essence for each theme.
6. **Producing the report** — interpretive narrative with extracts as evidence.

### Grounded Theory (Charmaz / Strauss-Corbin)

- **Open coding** — line-by-line, often gerund-style ("avoiding disclosure", "rationalizing risk").
- **Axial coding** — group open codes into categories; explore relationships.
- **Selective coding** — identify the core category that explains the process.
- **Theoretical sampling** — collect more data to develop emerging categories.
- **Constant comparison** — every new datum compared to existing codes/categories.
- Continue until **theoretical saturation**.

### Framework Analysis (Ritchie & Spencer)

- Develop a thematic framework from familiarization.
- Index every transcript against the framework.
- Chart data into a matrix (rows = participants, columns = themes).
- Map and interpret across cases.

Best when there are pre-defined topics (policy research, applied evaluation).

### Content Analysis (Krippendorff / Hsieh & Shannon)

- **Conventional** — codes emerge from data (similar to thematic).
- **Directed** — start from theory-derived codes; refine.
- **Summative** — count occurrences of words/concepts, then interpret context.

Best when frequency matters and reliability is critical.

### IPA (Interpretive Phenomenological Analysis)

- Idiographic: code one transcript fully before moving to the next.
- Three layers: descriptive comments → linguistic comments → conceptual comments.
- Develop superordinate themes within case, then look for patterns across cases.

### Discourse Analysis

- Focus on language as constructive: how is X talked about? What does the talk *do*?
- Code for: rhetorical devices, subject positions, interpretive repertoires, ideological dilemmas.

## Phase 4 — Build the codebook

A codebook is a living document with one row per code:

```markdown
| Code | Definition | Inclusion criteria | Exclusion criteria | Example quote (with cite) |
|------|------------|--------------------|--------------------|---------------------------|
| Avoiding disclosure | Participant withholds info to manage social risk | Statements about choosing not to share, hiding, deflecting | Disclosure that participant frames as accidental | "I just don't tell my coworkers — it's not their business" (P03, line 142) |
```

Iterate the codebook as you code. Note the version. When a code's definition shifts, re-code earlier transcripts to apply the new definition.

## Phase 5 — Code

For each transcript:

1. Read it once before coding (familiarization).
2. Code in passes — first pass for big chunks, refine on later passes.
3. Use a consistent location format for excerpts (e.g., `P03:142-148` for participant 3, lines 142-148).
4. Capture **disconfirming cases** explicitly — they refine theory more than confirming ones.
5. Write **memos** alongside coding: hunches, theoretical notes, methodological decisions.

Output format (when coding programmatically):

```json
{
  "transcript_id": "P03",
  "excerpts": [
    {
      "lines": "142-148",
      "text": "...",
      "codes": ["avoiding_disclosure", "workplace_norms"],
      "memo": "Participant frames non-disclosure as a choice, not constraint — contrast with P01."
    }
  ]
}
```

Or maintain coded outputs as inline annotations:

```
P03, line 142-148:
  Text: "I just don't tell my coworkers — it's not their business"
  Codes: [avoiding_disclosure, workplace_norms]
  Memo: ...
```

## Phase 6 — Inter-rater reliability (when applicable)

If two or more coders:

- Both code a subset (typically 20-30% of transcripts).
- Compute **Cohen's κ** for two coders, **Fleiss' κ** for 3+, or **Krippendorff's α** (handles missing data and any level of measurement).
- Targets: κ ≥ 0.80 strong, 0.60-0.79 substantial, 0.40-0.59 moderate (refine codebook).
- Disagreements → discussion → codebook refinement → re-code.

Python:
```python
from sklearn.metrics import cohen_kappa_score
kappa = cohen_kappa_score(coder1_labels, coder2_labels)
```

R:
```r
library(irr)
kappa2(cbind(coder1, coder2))  # Cohen's
kripp.alpha(rbind(coder1, coder2), method = "nominal")
```

## Phase 7 — Theme development and reporting

Move from codes to themes:

- Cluster related codes into candidate themes.
- For each theme: name + one-sentence essence + 3-5 illustrative quotes (with participant ID).
- Build a **thematic map**: themes, sub-themes, and relationships.
- Check each theme against: prevalence (across how many participants?), centrality (does it answer the RQ?), and disconfirming cases.

Final report structure:

```markdown
# Qualitative Findings: [Project]

## Methods (brief)
- Tradition, sample, coding approach, software, IRR (if any).
- Researcher positionality.

## Themes
### Theme 1: [Name]
[Essence in 1-2 sentences.]
[Narrative interpretation, 2-4 paragraphs, weaving in extracts.]
> "Direct quote..." (P03, line 142)
> "Another quote that contrasts or extends..." (P07, line 88)

### Theme 2: [Name]
...

## Cross-cutting observations
[Patterns across themes, surprises, disconfirming cases.]

## Reflexivity statement
[Researcher positionality and its likely effects on analysis.]

## Audit trail (appendix)
- Codebook (final version).
- Memo highlights.
- Coding decisions log.
```

## Phase 8 — NLP-assisted exploration (for large corpora)

For corpora too large to read every line, use NLP to **surface patterns to investigate by hand**, never to replace interpretation.

### Useful techniques

- **TF-IDF / keyword analysis** — what words distinguish subgroups?
- **Topic modeling** (LDA, BERTopic) — surface latent topic clusters; treat outputs as exploratory.
- **Sentence embeddings + clustering** (sentence-transformers + HDBSCAN) — better than LDA for short responses.
- **Sentiment / emotion analysis** — coarse but useful for triage; validate on a sample.
- **Named entity extraction** — pull out organizations, places, roles for indexing.
- **LLM-assisted coding** — use Claude or another LLM to *suggest* codes for a subset; always validate against hand-coding before scaling.

Always:
1. Pilot the NLP approach on a hand-coded subset.
2. Compute agreement between NLP labels and hand labels.
3. Inspect outputs qualitatively before trusting them.
4. Disclose use of NLP in methods section.

### Example: BERTopic on open-ended survey responses

```python
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(responses)

topic_model = BERTopic(min_topic_size=20)
topics, probs = topic_model.fit_transform(responses, embeddings)

print(topic_model.get_topic_info())  # inspect labels
topic_model.visualize_topics()
```

Then **read 10-20 responses per topic by hand** and decide whether the topic represents a real theme or an artifact.

### Example: LLM-assisted code suggestion

For each new excerpt, prompt: "Given this codebook [insert], which codes apply? Quote the exact phrase that justifies each."

Validate: compute agreement with a human coder on 30+ excerpts before relying on LLM-only coding.

## Phase 9 — Self-audit checklist

Before declaring done:

- [ ] Codebook is consistent — every code has a clear definition and discriminating examples.
- [ ] Themes have a clear central organizing concept (not just topic buckets).
- [ ] Each theme is supported by quotes from multiple participants (or, if not, the limit is acknowledged).
- [ ] Disconfirming cases are addressed.
- [ ] Reflexivity statement included.
- [ ] Audit trail is reconstructable from memos and codebook versions.
- [ ] If NLP was used, validation against hand-coding is documented.

## Handoffs

Part of the research-co-pilot skill network. See [`docs/skill-network.md`](../../docs/skill-network.md) for the full map, the `.research/` workspace + manifest contract, and the human-gate rule.

**Lifecycle position:** Analysis (qualitative) — after data collection, before drafting.

**Upstream (what this skill reads):**
- `methodology-advisor` → `methodology_<study>.md` — the qualitative tradition (thematic / grounded theory / IPA / etc.) and the analysis plan.
- The **transcripts / corpus** themselves.
- *At intake, check `.research/manifest.json` for the methodology before asking for the tradition.*

**Downstream (what this skill feeds):**
- `manuscript-drafter` — the themes report becomes the Findings section, with quotes + participant IDs preserved.

**Chaining:**
- **Claude Code:** for a large corpus, spawn the `transcript-coder` subagent (bulk clean + code). On completion, offer to invoke `Skill(manuscript-drafter)` to write up the Findings (ask first).
- **claude.ai:** process transcripts inline in the analysis sandbox; advise "run /draft next for the Findings section."

**Vault** (see [`docs/research-vault.md`](../../docs/research-vault.md)):
- *Read at intake:* `facts` (sample size) and the methodology's qualitative tradition.
- *Write at output:* deposit participants into `entities.md` as **pseudonyms + non-identifying attributes only** (e.g., "P03 — ICU nurse, 8 yrs"); add codes/themes/operationalizations to `glossary.md`.
- *PII hard rule:* the real-name → pseudonym key stays **off-system**, exactly as Phase 2 requires — it is never written into `entities.md` or anywhere in `.research/`. The vault holds pseudonyms only.

**Output to the workspace:** write the codebook + themes report (+ anonymization key kept separate) under `.research/`, register in the manifest, advance `stage` to `analysis`.
