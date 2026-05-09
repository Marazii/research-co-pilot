# research-co-pilot

A Claude assistant for the entire research lifecycle — from picking a question through final peer review. Designed for academic researchers (graduate students, postdocs, faculty) and applied researchers (UX, policy, public health, data science) who want a rigorous collaborator that respects methodological standards instead of generating plausible-looking output.

Works in two places:

- **Claude Code** (CLI / IDE) — installs as a plugin with skills, slash commands, and subagents.
- **Claude.ai** (web / desktop) — install individual skills as Claude Skills.

Same skills, same behavior, two surfaces.

---

## What it helps with

| Stage of research | Skill | Trigger examples |
|---|---|---|
| Finding a question | **research-brainstorm** | "help me find a thesis topic in X", "brainstorm research ideas" |
| Reviewing the field | **literature-review** | "what does the research say about X", "do a lit review on Y" |
| Designing the study | **methodology-advisor** | "should I use an RCT or quasi-experiment?", "what sample size do I need?" |
| Designing instruments | **survey-design** | "is this question biased?", "find a validated scale for X" |
| Analyzing quantitative data | **data-analysis** | "clean this dataset", "fit a regression", "run a power analysis" |
| Analyzing qualitative data | **qualitative-coding** | "code these transcripts", "build a codebook", "find themes" |
| Writing it up | **citation-formatter** | "format these in APA", "fix my bibliography" |
| Getting feedback | **peer-review** | "review my paper", "fact-check this draft" |

Every skill is grounded in research methods literature and refuses common AI failure modes — no fabricated citations, no p-hacking, no glossed-over disagreement between sources, no qualitative "themes" without an audit trail.

---

## Why use this instead of plain Claude

Plain Claude is great at fluency, weak at rigor. Researchers feel this most when:

- It invents DOIs and authors that don't exist.
- It runs statistical tests without checking assumptions.
- It generates "themes" from qualitative data without showing where they came from.
- It writes literature reviews that average away real disagreement in the field.
- It says "more research is needed" instead of identifying specific gaps.

Each skill in this plugin is a structured workflow that catches these failures: source verification before citation, assumption diagnostics before reporting effects, codebook + memos for every theme, surfacing of conflicting findings, specific rather than generic gaps. The skills are written in the voice of a methodologist who has supervised dissertations, reviewed for journals, and published in mixed methods.

---

## Installation — Claude Code

You need Claude Code installed and a working terminal.

**One-command install** (recommended):

```bash
# Add this repo as a Claude Code marketplace
/plugin marketplace add https://github.com/marazii/research-co-pilot

# Install the plugin from that marketplace
/plugin install research-co-pilot@research-co-pilot-marketplace
```

After install, run `/research` for the menu, or invoke any specific skill by name (e.g. `/lit-review climate adaptation in coastal cities`).

**Local install** (for development or to use without GitHub):

```bash
git clone https://github.com/marazii/research-co-pilot.git
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
/plugin install research-co-pilot@research-co-pilot-local
```

---

## Installation — Claude.ai

Each skill is uploaded to claude.ai individually as a Claude Skill. Pre-built upload bundles ship in [`dist/`](dist/).

1. Download the `.zip` for each skill you want from [`dist/`](dist/) (or grab them all from the [latest release](https://github.com/marazii/research-co-pilot/releases)).
2. In claude.ai, open **Settings → Capabilities → Skills** (Pro/Team/Enterprise plans), or open your workspace's **Skills library** (Team/Enterprise).
3. Click **Upload skill** and select a `.zip`. Repeat for each skill.

Once uploaded, claude.ai loads the skill automatically when your message matches its trigger phrases (e.g. "do a literature review on…" loads `literature-review`).

> Subagents and slash commands are Claude Code-only and don't apply in claude.ai. The skills handle their work directly when run there.

---

## Usage examples

### "I'm a year into my PhD and I have no idea what to study."

```
/brainstorm I work on misinformation and trust in news, broadly. I have access to
panel survey data and can run online experiments. Constraint: must be defensible
in a quant-focused department.
```

The skill generates 15-25 candidate questions across descriptive, causal, predictive, and contrarian framings; scores them on interest / answerability / novelty / feasibility; sharpens the top 3 into full study sketches with predicted findings, risks, and follow-up studies.

### "I need to write a literature review for my thesis."

```
/lit-review the effect of remote work on early-career mentorship in knowledge industries
```

You'll be asked about scope (narrative vs systematic vs scoping), discipline, date range, and any sources you already have. The skill then searches, reads, fact-checks, and synthesizes — organizing by idea (not by source), surfacing where studies disagree, marking each claim with a confidence tag, and producing a complete review with appraisal table.

### "Reviewer 2 said my analysis is wrong."

```
/analyze ./data/study2_clean.csv — they want me to handle the clustered structure
(students within classrooms within schools). Currently I just have OLS.
```

The skill walks through the data, fits the appropriate mixed-effects model, runs diagnostics, compares specifications, and writes up the result with effect sizes, CIs, and an honest discussion of what changes from the original.

### "I have 18 interview transcripts and need themes for a paper."

```
/code-themes ./transcripts/
```

The skill anonymizes, develops a codebook (inductively, deductively, or hybrid — you choose), codes systematically, runs inter-rater reliability if you have a second coder, develops themes with disconfirming-case checks, and writes the qualitative findings section with quoted excerpts and a reflexivity statement.

### "I'm submitting tomorrow and my references are a mess."

```
/cite fix all references in ./manuscript.md to APA 7
```

The skill extracts every in-text citation, verifies DOIs, checks that the in-text and reference list match, applies APA 7 consistently, and reports any entries it couldn't verify so you can confirm them.

---

## What's in the box

```
research-co-pilot/
├── .claude-plugin/
│   ├── plugin.json           # Claude Code plugin manifest
│   └── marketplace.json      # one-command install from GitHub
├── skills/                   # Portable: work in Claude Code AND claude.ai
│   ├── literature-review/
│   ├── methodology-advisor/
│   ├── data-analysis/
│   ├── qualitative-coding/
│   ├── research-brainstorm/
│   ├── citation-formatter/
│   ├── survey-design/
│   └── peer-review/
├── agents/                   # Subagents (Claude Code only)
│   ├── source-finder.md      # parallel reading of many academic sources
│   ├── data-cruncher.md      # heavy compute in isolation
│   └── transcript-coder.md   # bulk qualitative processing
├── commands/                 # Slash commands (Claude Code only)
│   ├── research.md           # /research — entry-point router
│   └── ...                   # /lit-review, /methodology, /analyze, etc.
├── dist/                     # Built upload bundles for claude.ai
│   └── *.zip                 # one zip per skill, SKILL.md at archive root
├── scripts/
│   └── build-zips.sh         # rebuild dist/ after editing skills
├── LICENSE                   # MIT
└── README.md
```

### Skills (work in both surfaces)

| Skill | What it does |
|-------|-------------|
| `literature-review` | Fact-checked synthesis of a body of work. Verifies citations, organizes by idea, surfaces disagreement, marks confidence on every claim, identifies specific gaps. Supports narrative, systematic, scoping, rapid, and thematic reviews. |
| `methodology-advisor` | Quant + qual research design — picking the right design for the question, sampling strategy, power and sample size, validity threats, IRB/ethics, pre-registration. Pushes back when a chosen method doesn't fit the question. |
| `data-analysis` | End-to-end quantitative work in Python or R: cleaning, EDA, statistical testing, modeling (regression, mixed-effects, predictive, time series, survival), assumption diagnostics, sensitivity analyses, visualization, reproducible scripts. |
| `qualitative-coding` | Codebook development and application using thematic analysis, grounded theory, IPA, framework analysis, or content analysis. Inter-rater reliability (Cohen's κ, Krippendorff's α). NLP-assisted exploration for large corpora — with required validation against hand-coding. |
| `research-brainstorm` | Generates 15-25 research ideas via question-form variations, cross-field grafts, and contrarian moves. Scores them. Sharpens the top 3 into study sketches. Pushes past the obvious next study. |
| `citation-formatter` | APA 7, MLA 9, Chicago (NB and AD), Harvard, Vancouver, IEEE, AMA, journal-specific. Verifies DOIs, handles edge cases (preprints, datasets, software, AI tools). Generates BibTeX/RIS. Document-wide consistency check. |
| `survey-design` | Question wording, scale choice, ordering effects, response burden. Recommends validated instruments rather than inventing new ones. Includes a pilot plan (cognitive interviews + quantitative pilot). Translation guidance. |
| `peer-review` | Multi-mode rigorous review: paper verdict, homework grading, committee panel, fact-check audit, plagiarism check, draft thinking-partner, post-review iterate. Adapts to the work's academic domain. |

### Subagents (Claude Code only — claude.ai has no equivalent)

| Agent | When the parent skill spawns it |
|-------|--------------------------------|
| `source-finder` | Reading >5 academic sources in parallel without bloating the main conversation. Returns structured digests with verified citations. |
| `data-cruncher` | Heavy computation, many model variants, simulations, sensitivity grids — in isolation. Returns a tight results summary instead of raw output. |
| `transcript-coder` | Bulk cleaning, anonymization, and code-application across many transcripts. Returns coded JSON + a summary instead of full transcript text. |

### Slash commands (Claude Code only)

`/research` is the entry point if you're not sure which skill you need — it routes by description. The other commands invoke the matching skill directly: `/lit-review`, `/methodology`, `/analyze`, `/code-themes`, `/brainstorm`, `/cite`, `/survey`, `/peer-review`.

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

Then re-upload the changed `dist/*.zip` files to claude.ai.

---

## Contributing

Contributions welcome. Open an issue first if you're proposing a substantial change (new skill, restructuring an existing one). Smaller PRs (typo fixes, additional citation styles, additional qualitative traditions, additional statistical recipes) are fine to send directly.

If you add a new skill:
1. Create `skills/<your-skill>/SKILL.md` with frontmatter (`name`, `description` with trigger phrases, optional `allowed-tools`).
2. Add a slash command in `commands/<your-skill>.md` if it makes sense as a user-invoked entry point.
3. Run `./scripts/build-zips.sh` to add it to the `dist/`.
4. Update this README's table.

---

## Caveats and honest limits

- **Citations:** the literature-review skill verifies what it can, but published research changes. Treat the output as a strong first pass that you read and confirm — never paste it into a manuscript without checking.
- **Statistics:** the data-analysis skill picks reasonable defaults and checks assumptions, but applied stats often involves judgment calls a model can't make. Treat its output as a draft analysis your statistician reviews.
- **Qualitative coding:** AI-assisted coding is exploratory. Use it to surface candidates, then validate against hand-coded subsets before relying on labels at scale.
- **Peer review:** useful for catching blind spots and surface issues. Cannot replace expert review in your specific subfield.
- **Ethics and IRB:** the methodology skill flags IRB-relevant considerations but is not a substitute for your institution's review process.

In short: this is a force multiplier for a researcher who knows what good work looks like — not a replacement for that judgment.

---

## License

MIT — see [LICENSE](LICENSE).

---

## Credits

Built by Maya Arazi. Peer-review skill draws on prior work by the Anthropic Skills community. Methodological frameworks reference standard research methods literature (Braun & Clarke, Charmaz, Shadish-Cook-Campbell, Dillman, Lincoln & Guba, and many others) — all citations belong to their original authors.
