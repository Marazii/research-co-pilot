# research-co-pilot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Marazii/research-co-pilot/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/version-0.10.0-blue.svg)](https://github.com/Marazii/research-co-pilot/blob/main/CHANGELOG.md)
[![CI](https://github.com/Marazii/research-co-pilot/actions/workflows/validate.yml/badge.svg)](https://github.com/Marazii/research-co-pilot/actions/workflows/validate.yml)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-8b5cf6.svg)](#installation--claude-code)
[![Claude.ai](https://img.shields.io/badge/Claude.ai-skills-d97757.svg)](#installation--claudeai)
[![Cite](https://img.shields.io/badge/cite-CITATION.cff-green.svg)](./CITATION.cff)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.PLACEHOLDER-CONCEPT.svg)](https://doi.org/10.5281/zenodo.PLACEHOLDER-CONCEPT)

<!--
  The DOI badge resolves to the Zenodo concept DOI for this repo, which
  always points to the latest release. The placeholder is auto-replaced by
  the update-citation-doi.yml workflow after v0.10.0 mints. If you see
  PLACEHOLDER-CONCEPT here, the workflow hasn't run yet — see CONTRIBUTING.md
  § Release process for the manual fallback.
-->


A Claude co-pilot for the entire research lifecycle — from picking a question through final peer review. Designed for academic researchers (graduate students, postdocs, faculty) and applied researchers (UX, policy, public health, data science) who want a rigorous collaborator that respects methodological standards instead of generating plausible-looking output.

Works in two places:

- **Claude Code** (CLI / IDE) — installs as a plugin with skills, slash commands, and subagents.
- **Claude.ai** (web / desktop) — install individual skills as Claude Skills.

Same skills, same behavior, two surfaces.

---

## What it helps with

| Stage of research | Skill | Trigger examples |
|---|---|---|
| Finding a question | [**research-brainstorm**](./skills/research-brainstorm/README.md) | "help me find a thesis topic in X", "brainstorm research ideas" |
| Reviewing the field | [**literature-review**](./skills/literature-review/README.md) | "what does the research say about X", "do a lit review on Y" |
| Designing the study | [**methodology-advisor**](./skills/methodology-advisor/README.md) | "should I use an RCT or quasi-experiment?", "what sample size do I need?" |
| Stress-testing the ethics | [**ethics-committee**](./skills/ethics-committee/README.md) | "is this study ethical?", "review my IRB application", "draft an ethics statement" |
| Designing instruments | [**survey-design**](./skills/survey-design/README.md) | "is this question biased?", "find a validated scale for X" |
| Analyzing quantitative data | [**data-analysis**](./skills/data-analysis/README.md) | "clean this dataset", "fit a regression", "run a power analysis" |
| Analyzing qualitative data | [**qualitative-coding**](./skills/qualitative-coding/README.md) | "code these transcripts", "build a codebook", "find themes" |
| Drafting the manuscript | [**manuscript-drafter**](./skills/manuscript-drafter/README.md) | "write the intro", "draft the discussion", "write the abstract" |
| Replicating someone else's study | [**replication-designer**](./skills/replication-designer/README.md) | "design a replication of X", "is this finding robust?" |
| Funding the work | [**grant-writer**](./skills/grant-writer/README.md) | "draft my specific aims", "NSF broader impacts", "ERC synopsis" |
| Presenting it | [**talk-builder**](./skills/talk-builder/README.md) | "turn this paper into a 12-min conference talk", "job talk outline", "thesis defense slides" |
| Responding to reviewers | [**reviewer-response**](./skills/reviewer-response/README.md) | "draft my R1 response", "rebuttal letter", "address reviewer comments" |
| Formatting references | [**citation-formatter**](./skills/citation-formatter/README.md) | "format these in APA", "fix my bibliography" |
| Getting feedback | [**peer-review**](./skills/peer-review/README.md) | "review my paper", "fact-check this draft", "review my slides" |

Every skill is grounded in research methods literature and refuses common AI failure modes — no fabricated citations, no p-hacking, no glossed-over disagreement between sources, no qualitative "themes" without an audit trail, no embellished findings, no voice-mismatched drafts.

Each skill name above links to its **per-skill README** with a synthetic example, the trigger phrases, composition with other skills, and honest caveats. The [`examples/`](./examples/) folder contains a worked sample for each shipped skill.

---

## Why use this instead of plain Claude

Plain Claude is great at fluency, weak at rigor. Researchers feel this most when:

- It invents DOIs and authors that don't exist.
- It runs statistical tests without checking assumptions.
- It generates "themes" from qualitative data without showing where they came from.
- It writes literature reviews that average away real disagreement in the field.
- It says "more research is needed" instead of identifying specific gaps.
- It drafts manuscript prose that doesn't match the author's existing voice.

Each skill in this plugin is a structured workflow that catches these failures: source verification before citation, assumption diagnostics before reporting effects, codebook + memos for every theme, surfacing of conflicting findings, specific rather than generic gaps, mandatory voice extraction before drafting. The skills are written in the voice of a methodologist who has supervised dissertations, reviewed for journals, and published in mixed methods.

For a longer discussion of the design philosophy, see [`docs/philosophy.md`](./docs/philosophy.md). For common questions about safety, citation, language coverage, and how this compares to SaaS research-AI products, see [`docs/faq.md`](./docs/faq.md).

---

## Installation — Claude Code

You need Claude Code installed and a working terminal.

**One-command install** (recommended):

```bash
# Add this repo as a Claude Code marketplace
claude plugin marketplace add Marazii/research-co-pilot

# Install the plugin from that marketplace
claude plugin install research-co-pilot@research-co-pilot-marketplace
```

After install, run `/research` for the menu, or invoke any specific skill by name (e.g. `/lit-review climate adaptation in coastal cities`).

**Updating an existing install:**

```bash
claude plugin marketplace update research-co-pilot-marketplace
claude plugin update research-co-pilot@research-co-pilot-marketplace
```

Then restart Claude Code.

**Local install** (for development or to use without GitHub):

```bash
git clone https://github.com/Marazii/research-co-pilot.git
cd research-co-pilot

# Add your local clone as a marketplace
# Edit ~/.claude/settings.json and add:
{
  "plugins": {
    "marketplaces": {
      "research-co-pilot-local": {
        "type": "local",
        "path": "/absolute/path/to/the/parent/of/research-co-pilot"
      }
    }
  }
}

# Then in Claude Code:
claude plugin install research-co-pilot@research-co-pilot-local
```

---

## Installation — Claude.ai

Each skill is uploaded to claude.ai individually as a Claude Skill. Pre-built upload bundles ship as **GitHub Release assets** — stable URLs that don't change when commits land on `main`.

1. Go to the [**latest release**](https://github.com/Marazii/research-co-pilot/releases/latest) and download the `.zip` for each skill you want.

   Direct downloads always pointing at the latest stable release:

   ```
   https://github.com/Marazii/research-co-pilot/releases/latest/download/literature-review.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/methodology-advisor.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/ethics-committee.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/data-analysis.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/qualitative-coding.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/research-brainstorm.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/manuscript-drafter.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/replication-designer.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/grant-writer.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/talk-builder.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/reviewer-response.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/citation-formatter.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/survey-design.zip
   https://github.com/Marazii/research-co-pilot/releases/latest/download/peer-review.zip
   ```

2. In claude.ai, open **Settings → Capabilities → Skills** (Pro/Team/Enterprise plans), or open your workspace's **Skills library** (Team/Enterprise).

3. Click **Upload skill** and select a `.zip`. Repeat per skill.

Once uploaded, claude.ai loads the skill automatically when your message matches its trigger phrases (e.g. "do a literature review on…" loads `literature-review`).

> Subagents and slash commands are Claude Code-only and don't apply in claude.ai. The skills handle their work directly when run there.

---

## Visibility & assets

Screenshots, demo GIFs, and the social-preview image live under [`docs/`](./docs/):

- [`docs/philosophy.md`](./docs/philosophy.md) — design choices and what the plugin won't do.
- [`docs/faq.md`](./docs/faq.md) — common questions about citations, regulated data, language coverage, comparison to SaaS products.
- [`docs/screenshots/`](./docs/screenshots/) — high-DPI screenshots of typical outputs (annotated PDFs, methodology with the AI/ML extensions table, etc.).
- [`docs/demo.gif`](./docs/demo.gif) — ~30-second screencast of a typical flow.

*(Some visibility assets are added during the v0.10.0-rc.1 → v0.10.0 final cycle and may not all be present yet.)*

---

## Usage examples

### "I'm a year into my PhD and I have no idea what to study."

```
/brainstorm I work on misinformation and trust in news, broadly. I have access to
panel survey data and can run online experiments. Constraint: must be defensible
in a quant-focused department.
```

The skill generates 15-25 candidate questions across descriptive, causal, predictive, and contrarian framings; scores them on interest / answerability / novelty / feasibility; sharpens the top 3 into full study sketches with predicted findings, risks, and follow-up studies. See [`examples/research-brainstorm/`](./examples/research-brainstorm/) for a worked sample.

### "I need to write a literature review for my thesis."

```
/lit-review the effect of remote work on early-career mentorship in knowledge industries
```

The skill searches, reads, fact-checks, and synthesizes — organizing by idea (not by source), surfacing where studies disagree, marking each claim with a confidence tag, producing a complete review with appraisal table. See [`examples/literature-review/`](./examples/literature-review/) for a worked sample.

### "Reviewer 2 said my analysis is wrong."

```
/analyze ./data/study2_clean.csv — they want me to handle the clustered structure
(students within classrooms within schools). Currently I just have OLS.
```

The skill walks through the data, fits the appropriate mixed-effects model, runs diagnostics, compares specifications, and writes up the result with effect sizes, CIs, and an honest discussion of what changes from the original. See [`examples/data-analysis/`](./examples/data-analysis/) for a worked sample.

### "I have 18 interview transcripts and need themes for a paper."

```
/code-themes ./transcripts/
```

The skill anonymizes, develops a codebook (inductively, deductively, or hybrid — you choose), codes systematically, runs inter-rater reliability if you have a second coder, develops themes with disconfirming-case checks, and writes the qualitative findings section with quoted excerpts and a reflexivity statement. See [`examples/qualitative-coding/`](./examples/qualitative-coding/) for a worked sample.

### "I got an R&R and need to draft the response letter."

```
/respond review_round1.md manuscript_v1.md  (R1 from J. Hypothetical Studies)
```

The skill categorizes every reviewer point (concession / partial / pushback / clarification / out-of-scope / minor), drafts the response per point with the reviewer's verbatim quote, drafts the corresponding manuscript revisions (delegating long-form prose to `manuscript-drafter` to preserve voice), assembles a one-page cover letter that surfaces points of disagreement up front, and self-audits that every claimed revision actually appears in the revised manuscript.

### "Extend my Discussion chapter — match the rest of the thesis."

```
/draft Discussion section, target ~1500 words.
Inputs: existing_draft.md, methodology.md, qual_findings.md, references.bib.
Language: Hebrew.
```

The skill extracts a voice profile from the existing manuscript (sentence length, person/voice, hedge intensity, signature phrases, connectors, citation style, Hebrew register markers), drafts new prose to match, enforces a per-section word budget, scans for non-academic register, and grounds every new idea in your bibliography (or flags it as `[LITERATURE NEEDED]` with concrete search guidance). See [`examples/manuscript-drafter/`](./examples/manuscript-drafter/) for a worked sample showing the v0.8.0 overhaul.

---

## What's in the box

```
research-co-pilot/
├── .claude-plugin/
│   ├── plugin.json           # Claude Code plugin manifest
│   └── marketplace.json      # one-command install from GitHub
├── .github/
│   ├── workflows/            # CI: validate / build-dist / release
│   ├── ISSUE_TEMPLATE/       # bug / feature / new-skill-proposal
│   └── PULL_REQUEST_TEMPLATE.md
├── skills/                   # Portable: work in Claude Code AND claude.ai
│   ├── literature-review/
│   ├── methodology-advisor/
│   ├── ethics-committee/
│   ├── data-analysis/
│   ├── qualitative-coding/
│   ├── research-brainstorm/
│   ├── manuscript-drafter/
│   ├── replication-designer/
│   ├── grant-writer/
│   ├── talk-builder/
│   ├── reviewer-response/
│   ├── citation-formatter/
│   ├── survey-design/
│   └── peer-review/
│       └── (each skill has SKILL.md + README.md + optional reference files)
├── agents/                   # Subagents (Claude Code only)
│   ├── source-finder.md      # parallel reading of many academic sources
│   ├── data-cruncher.md      # heavy compute in isolation
│   ├── transcript-coder.md   # bulk qualitative processing
│   ├── manuscript-drafter.md # long-form drafting in isolation
│   └── stats-validator.md    # independent second-look on a colleague's analysis
├── commands/                 # Slash commands (Claude Code only)
│   ├── research.md           # /research — entry-point router
│   └── (one per skill: /lit-review, /methodology, /ethics, /analyze,
│        /code-themes, /brainstorm, /draft, /replicate, /grant, /talk,
│        /respond, /cite, /survey, /peer-review)
├── examples/                 # Synthetic minimal example per skill
├── docs/                     # philosophy, faq, screenshots, demo
├── scripts/
│   └── build-zips.sh         # rebuild dist/ after editing skills
├── CHANGELOG.md
├── CITATION.cff              # academic citation metadata
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE                   # MIT
└── README.md
```

### Skills (work in both surfaces)

| Skill | What it does |
|-------|-------------|
| [`literature-review`](./skills/literature-review/README.md) | Fact-checked synthesis of a body of work. Verifies citations, organizes by idea, surfaces disagreement, marks confidence on every claim, identifies specific gaps. Supports narrative, systematic, scoping, rapid, and thematic reviews. |
| [`methodology-advisor`](./skills/methodology-advisor/README.md) | Quant + qual research design — picking the right design for the question, sampling strategy, power and sample size, validity threats, IRB/ethics, pre-registration. Includes mandatory creative AI / ML / Big Data extensions section that forces the researcher to consider non-conventional methods. |
| [`ethics-committee`](./skills/ethics-committee/README.md) | Simulates an IRB / REC / HREC pre-submission review. Audits informed consent, risk-benefit, vulnerable populations, data privacy, deception, payment, AI/LLM use, social media data, equity in recruitment. Produces a decision letter with required revisions. Optional 3-reviewer panel mode. Not a substitute for institutional approval. |
| [`data-analysis`](./skills/data-analysis/README.md) | End-to-end quantitative work in Python or R: cleaning, EDA, statistical testing, modeling (regression, mixed-effects, predictive, time series, survival), assumption diagnostics, sensitivity analyses, visualization, reproducible scripts. |
| [`qualitative-coding`](./skills/qualitative-coding/README.md) | Codebook development and application using thematic analysis, grounded theory, IPA, framework analysis, or content analysis. Inter-rater reliability (Cohen's κ, Krippendorff's α). NLP-assisted exploration for large corpora — with required validation against hand-coding. |
| [`research-brainstorm`](./skills/research-brainstorm/README.md) | Generates 15-25 research ideas via question-form variations, cross-field grafts, and contrarian moves. Scores them. Sharpens the top 3 into study sketches. Pushes past the obvious next study. |
| [`manuscript-drafter`](./skills/manuscript-drafter/README.md) | Drafts long-form manuscript sections from your methodology and analysis outputs. **Preserves the existing manuscript's voice** via mandatory voice-profile extraction. **Enforces hard per-section word budgets** with a compression pass. **Enforces academic register** via a banned-pattern audit. **Grounds every new idea in literature** (distinguishes `[CITATION NEEDED]` from `[LITERATURE NEEDED]`). Two-pass ideation → prose workflow. Drafts in the manuscript's language (English, Hebrew, etc.). |
| [`replication-designer`](./skills/replication-designer/README.md) | Designs direct, conceptual, generalization, or robustness replications. Extracts the original spec, justifies every deviation, computes adequate replication power, plans pre-registration, pre-specifies replication-success criteria, supports multi-site logistics. |
| [`grant-writer`](./skills/grant-writer/README.md) | Drafts proposal sections (Specific Aims, Significance, Innovation, Approach, Broader Impacts, DMP, lay summary, biosketch, budget justification) tuned to NIH (R01/R21/F31/K), NSF (Standard / CAREER / GRFP), ERC, Wellcome, Horizon Europe, or foundation grants. Won't overpromise. Honest about scheme fit. |
| [`talk-builder`](./skills/talk-builder/README.md) | Turns one or more papers into an academic talk — outline, per-slide content, speaker notes, opening hook, single take-home message, backup slides for Q&A, rehearsal plan. Adapts to length, audience, format, and discipline conventions. Deck-platform-agnostic outline plus optional Marp / Quarto / reveal.js / Beamer stubs. |
| [`reviewer-response`](./skills/reviewer-response/README.md) | Drafts rigorous, polite, point-by-point response to reviewer comments (R1 / R2 / R3) plus matching manuscript revisions. Categorizes each comment, drafts response + revision, assembles cover letter. Won't concede a point the data doesn't support. Composes naturally with `peer-review` and `manuscript-drafter`. |
| [`citation-formatter`](./skills/citation-formatter/README.md) | APA 7, MLA 9, Chicago (NB and AD), Harvard, Vancouver, IEEE, AMA, journal-specific. Verifies DOIs, handles edge cases (preprints, datasets, software, AI tools). Generates BibTeX/RIS. Document-wide consistency check. |
| [`survey-design`](./skills/survey-design/README.md) | Question wording, scale choice, ordering effects, response burden. Recommends validated instruments rather than inventing new ones. Includes a pilot plan (cognitive interviews + quantitative pilot). Translation guidance. |
| [`peer-review`](./skills/peer-review/README.md) | Multi-mode rigorous review: paper verdict, homework grading, committee panel, fact-check audit, plagiarism check, draft thinking-partner, presentation feedback, post-review iterate. **Returns a reviewed file with annotations anchored at the relevant locations** across `.docx` (inline comments + tracked changes), `.pdf` (sticky-note comments + highlights via PyMuPDF), `.pptx` (native PowerPoint comments on slides / shapes), `.tex` (`% REVIEWER:` line comments, optional `changes` package). |

### Subagents (Claude Code only — claude.ai has no equivalent)

| Agent | Use it when |
|-------|-------------|
| `source-finder` | Reading >5 academic sources in parallel without bloating the main conversation. Returns structured digests with verified citations. |
| `data-cruncher` | Heavy computation, many model variants, simulations, sensitivity grids — in isolation. Returns a tight results summary instead of raw output. |
| `transcript-coder` | Bulk cleaning, anonymization, and code-application across many transcripts. Returns coded JSON + a summary instead of full transcript text. |
| `manuscript-drafter` | Long-form drafting (whole sections or whole papers) in isolation so the parent doesn't get flooded with thousands of words. Returns a structured digest plus the draft as files. |
| `stats-validator` | Independent second-look on a colleague's analysis. Reads their script + data + report in fresh context (no narrative contamination), re-runs, sensitivity-checks, and returns a tight memo with confidence judgment. |

### Slash commands (Claude Code only)

`/research` is the entry point if you're not sure which skill you need — it routes by description. The other commands invoke the matching skill directly: `/lit-review`, `/methodology`, `/ethics`, `/analyze`, `/code-themes`, `/brainstorm`, `/draft`, `/grant`, `/replicate`, `/talk`, `/respond`, `/cite`, `/survey`, `/peer-review`.

---

## Output conventions

- **Claude Code:** primary deliverable written to a markdown file in your working directory (e.g. `lit_review_<topic>.md`, `analysis_<topic>.md`, `methodology_<study>.md`). Reproducible scripts saved alongside.
- **Claude.ai:** primary deliverable rendered as a downloadable artifact; code and data files saved in the analysis sandbox for download.

Either way, the deliverables are designed to be portable — markdown + scripts you can drop into Overleaf, Google Docs, R Markdown, Quarto, or your repo.

---

## Customizing

Each skill's `SKILL.md` is the single source of truth for its behavior. Edit it to:

- Change trigger phrases (frontmatter `description`).
- Add discipline-specific guidance (e.g. CONSORT for clinical trials, COREQ for qualitative).
- Adjust the output format to match your lab's or journal's expectations.

After editing skills, rebuild the claude.ai bundles:

```bash
./scripts/build-zips.sh
```

Then re-upload the changed `dist/*.zip` files to claude.ai (or push to a tag and CI builds + uploads to the Release automatically).

---

## Contributing

Contributions are welcome with a high bar. Start with [`CONTRIBUTING.md`](./CONTRIBUTING.md) — it documents:

- What the project is (and is not).
- The PR-level bar (validation, CHANGELOG, version bump, dist rebuild, per-skill README + example updates).
- The path for new skills (open a `New skill proposal` issue first; PRs without prior discussion are declined).
- What gets declined and why.

By contributing you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md) (Contributor Covenant 2.1). Security issues should follow the [SECURITY.md](./SECURITY.md) disclosure process.

---

## Citing

If you use this plugin in your research, please cite it. The repository's [`CITATION.cff`](./CITATION.cff) renders as a "Cite this repository" widget on GitHub, producing APA, BibTeX, and other formats. A Zenodo-minted DOI will be available from the v0.10.0 final release onward.

---

## Philosophy

For a longer write-up of the design choices — why each skill encodes specific hard rules, what "rigor over fluency" means in practice, and what the plugin won't do — see [`docs/philosophy.md`](./docs/philosophy.md).

---

## Caveats and honest limits

- **Citations:** the literature-review skill verifies what it can, but published research changes. Treat the output as a strong first pass that you read and confirm — never paste it into a manuscript without checking.
- **Statistics:** the data-analysis skill picks reasonable defaults and checks assumptions, but applied stats often involves judgment calls a model can't make. Treat its output as a draft analysis your statistician reviews.
- **Qualitative coding:** AI-assisted coding is exploratory. Use it to surface candidates, then validate against hand-coded subsets before relying on labels at scale.
- **Peer review:** useful for catching blind spots and surface issues. Cannot replace expert review in your specific subfield.
- **Ethics and IRB:** the methodology and ethics-committee skills flag IRB-relevant considerations but are not a substitute for your institution's review process.
- **Voice preservation:** the manuscript-drafter and reviewer-response skills extract voice from your existing prose. Without an existing manuscript, voice cannot be enforced.

In short: this is a force multiplier for a researcher who knows what good work looks like — not a replacement for that judgment.

---

## License

MIT — see [LICENSE](LICENSE).

---

## Credits

Built by Maya Arazi — all skills (including `peer-review`), subagents, and slash commands. Methodological frameworks reference standard research methods literature (Braun & Clarke, Charmaz, Shadish-Cook-Campbell, Dillman, Lincoln & Guba, and many others) — all citations belong to their original authors.
