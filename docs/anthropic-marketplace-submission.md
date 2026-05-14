# Anthropic Official Marketplace — submission packet

Copy-paste packet for the in-app submission form at one of:

- <https://claude.ai/settings/plugins/submit>
- <https://platform.claude.com/plugins/submit>

(Both forms feed the same `anthropics/claude-plugins-official` review queue.) The form is behind Claude account auth and isn't a GitHub PR. Fill in the fields below.

---

## Field 1 — Plugin name

```
research-co-pilot
```

## Field 2 — Short description (typically ~150-250 chars)

```
A research co-pilot for Claude Code and claude.ai. 14 skills covering the academic research lifecycle: literature review, methodology design, ethics review, data analysis, qualitative coding, manuscript drafting, replication, grants, talks, peer review.
```

## Field 3 — Long description / about (typically several paragraphs)

```
research-co-pilot is a Claude plugin designed for academic and applied researchers who need rigorous methodological assistance — not generic AI fluency. It ships 14 skills that span the full research lifecycle, each grounded in research methods literature and engineered to refuse the failure modes general AI tools commit:

- Won't fabricate citations (literature-review verifies sources against the web + user-provided files)
- Won't p-hack (data-analysis pre-specifies tests, checks assumptions, reports effect sizes + CIs)
- Won't generate themes without an audit trail (qualitative-coding produces a codebook + memos + line-anchored excerpts)
- Won't average away disagreement in the literature (every claim tagged [strong]/[mixed]/[weak])
- Won't embellish findings (manuscript-drafter cites only from your bibliography; flags claims that need a source as [CITATION NEEDED]; preserves your manuscript's voice)
- Won't propose ML where N is too small or invent preliminary data (methodology-advisor mandates creative AI/ML/Big Data extensions section that pushes researchers past the conventional method, while honestly assessing fit, data needs, validation, and ethical concerns)

The plugin also includes 5 subagents (source-finder, data-cruncher, transcript-coder, manuscript-drafter, stats-validator) for heavy work that would otherwise pollute the parent conversation, and 15 slash commands as user-invoked entry points.

The peer-review skill returns reviewed files with annotations anchored at the relevant locations across .docx (inline comments + tracked changes), .pdf (sticky notes + highlights via PyMuPDF), .pptx (native PowerPoint comments on slides/shapes), and .tex (% REVIEWER: line comments, optional `changes` package).

The plugin works in both Claude Code (as a plugin with skills + subagents + slash commands) and claude.ai (skills uploaded individually as Claude Skills via Release assets). Hebrew academic register is first-class supported alongside English.

It's named "co-pilot" because the relationship is peer-collaborative, not subservient — the skills push back when methodology doesn't fit a question, refuse to ground a claim that the data doesn't support, and flag where the researcher's judgment is required.

MIT licensed. CITATION.cff included. CI on every push (claude plugin validate + SKILL.md description char-count checks). Zenodo-mintable DOI on each stable release.
```

## Field 4 — GitHub repository URL

```
https://github.com/Marazii/research-co-pilot
```

## Field 5 — Plugin install command (for Claude Code)

```
claude plugin marketplace add Marazii/research-co-pilot
claude plugin install research-co-pilot@research-co-pilot-marketplace
```

## Field 6 — Category / tags (multi-select likely)

Suggested categories (pick whatever the form offers that fits):

- **Research / Academia**
- **Writing**
- **Data analysis**
- **Productivity**
- **Documentation**

Suggested tags / topics (already applied to the GitHub repo):

```
research  academic  literature-review  methodology  ethics-review
data-analysis  qualitative-research  manuscript-drafting  peer-review
grant-writing  claude-plugin  agent-skills  llm  prompt-engineering
open-science  reproducible-research  research-methods  scientific-writing  ai-research
```

## Field 7 — Author info

- **Author name:** Maya Arazi
- **GitHub:** [@Marazii](https://github.com/Marazii)
- **Affiliation (if asked):** Independent researcher
- **Contact email:** *(use the email associated with your GitHub / Claude account)*

## Field 8 — License

```
MIT
```

## Field 9 — Version

```
0.10.0
```

(The CHANGELOG at <https://github.com/Marazii/research-co-pilot/blob/main/CHANGELOG.md> tracks all versions.)

## Field 10 — Citation (if asked for academic context)

```
Arazi, M. (2026). research-co-pilot: a Claude co-pilot for the entire research lifecycle (Version 0.10.0) [Computer software]. https://github.com/Marazii/research-co-pilot
```

Zenodo DOI will be added to CITATION.cff automatically on the next release after the Zenodo GitHub integration is toggled on (see CONTRIBUTING.md § Release process).

## Field 11 — Demo / screenshots (if requested)

The repo currently has placeholder slots at `docs/screenshots/` and `docs/demo.gif`. If the form asks for demos and you haven't captured them yet, either:

- Skip the field (deferred to v0.10.1+ per the v0.10.0 PRD).
- Note: "Screenshots and demo GIF deferred to v0.10.1; happy to provide via follow-up email once captured."

## Field 12 — Eligibility / quality acknowledgments (if asked)

The plugin meets the criteria typically requested for external-plugin submissions:

- ✓ Hosted on a public GitHub repository
- ✓ MIT licensed
- ✓ CI on every push (`claude plugin validate .` returns zero errors and zero warnings)
- ✓ `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` in place
- ✓ Citation file (`CITATION.cff`) included
- ✓ Versioned releases via Git tags + GitHub Releases (latest: `v0.10.0`)
- ✓ Per-skill README files documenting each capability
- ✓ Synthetic examples in `examples/<skill>/` for every skill
- ✓ Active maintainer (this is the maintainer's primary public project at this time)
- ✓ No telemetry; no phone-home behavior; no proprietary dependencies
- ✓ Privacy / safety considerations documented in `docs/faq.md` (HIPAA, GDPR, IRB-protected data caveats)

## Field 13 — Anything else / notes to reviewers

```
The plugin shipped its first stable release (v0.10.0) today (2026-05-14) after rapid iteration with feedback from a senior researcher. Notable design decisions documented in docs/philosophy.md:

1. "Rigor over fluency" — every skill has explicit Hard Rules naming the AI failure modes it refuses, with mechanisms enforcing the refusal (description char-count limits, anchoring requirements, mandatory voice extraction before drafting, etc.).

2. "Co-pilot, not assistant" — the skills push back where methodology doesn't fit a question or data doesn't support a claim. This is encoded in the language of the SKILL.md files (e.g., grant-writer's "won't overpromise" hard rule; manuscript-drafter's "never embellish findings").

3. Multi-language support — Hebrew academic register is first-class (banned everyday Hebrew patterns, classical-vs-contemporary connectors, gendered-form preservation).

Happy to answer any questions during review. Email or GitHub issue both work.
```

---

## Suggested timing

The Anthropic marketplace review is typically a few business days to a couple of weeks. While waiting:

- Make sure Zenodo GitHub integration is toggled on (one-time, free) so the next release auto-mints a DOI — strengthens the academic-tool credibility.
- Consider capturing screenshots / demo GIF for `docs/` (deferred to v0.10.1+ but could ship before Anthropic finishes reviewing).

## If they ask for changes

Common review feedback (per the marketplace's stated criteria):

- **Security review** — point them at `SECURITY.md` and the `docs/faq.md` section on "Does it run locally or call APIs?"
- **Documentation completeness** — point them at the per-skill READMEs and the `examples/` folder.
- **Maintenance plan** — point them at `CONTRIBUTING.md` § Release process, which documents the full release flow including CI workflows.

## After approval

If accepted, the plugin will appear at `external_plugins/research-co-pilot/` in the `anthropics/claude-plugins-official` repository, and users can install it via the standard `/plugin install` flow without needing to add your marketplace first. Update the README's install instructions to point at the official marketplace as the recommended install path (with the personal marketplace as an alternative).
