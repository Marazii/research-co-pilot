# Frequently asked questions

## Will it fabricate citations?

No — that's the headline failure mode the plugin is designed to refuse. Every skill that interacts with citations enforces a hard rule against invented DOIs / authors / years. The `literature-review` skill verifies sources before citing them. The `manuscript-drafter` skill cites only from the user's provided bibliography and marks anything else as `[CITATION NEEDED]` (known claim, source missing) or `[LITERATURE NEEDED]` (new idea the skill introduced that needs grounding). The `peer-review` skill flags unsupported citations in any document it reviews. If you find a fabricated citation, that's a bug — please open an issue with the reproduction.

## Can I use it on HIPAA / IRB-protected / GDPR-regulated data?

Treat this plugin like any AI tool that processes content you send to it: the content reaches the Claude API. The plugin itself adds no extra privacy layer. Specifically:

- It is **not a HIPAA-compliant service**. Don't process Protected Health Information through it unless your institution's policies allow Claude API use for that data class.
- It is **not a substitute for IRB / REC / HREC review**. The `ethics-committee` skill simulates a pre-submission audit to surface issues; only an actual institutional committee can grant approval.
- Skills like `qualitative-coding` include an explicit anonymization step before transcripts reach the model. If you're working with sensitive qualitative data, run the anonymization pass first and verify before continuing.
- For GDPR contexts: review Anthropic's data-handling policies for the Claude API in your jurisdiction. The plugin doesn't change those.

When in doubt: ask your data protection officer or IRB before running protected data through any AI tool.

## What languages are supported?

The plugin is designed to work across languages, with Hebrew explicitly supported (the `manuscript-drafter` skill has Hebrew academic register markers built in). Other languages work to the extent that the underlying model handles them — most major European, Latin American, and East Asian languages do well. The plugin's interface (slash commands, README) is English; the *content* skills produce is in the user's working language.

If you're working in a less-resourced language and notice the skill defaulting to English, open an issue with a sample — the workflow can usually be adjusted.

## Why does the README version badge show v0.X but I see v0.Y in the marketplace?

The README and `plugin.json` are updated when a tag is pushed; the marketplace cache refreshes on demand. To force a sync:

```bash
claude plugin marketplace update research-co-pilot-marketplace
claude plugin update research-co-pilot@research-co-pilot-marketplace
```

Then restart Claude Code. If the versions still don't match after restart, that's a bug — open an issue with the output of `claude plugin marketplace list` and `claude plugin list`.

## How do I update to the latest version?

```bash
claude plugin marketplace update research-co-pilot-marketplace
claude plugin update research-co-pilot@research-co-pilot-marketplace
```

Then restart Claude Code. For claude.ai users: re-download the affected skill zip from the latest GitHub Release and re-upload via Settings → Capabilities → Skills.

## Can I add a skill for my discipline?

Yes, but please open a *New skill proposal* issue before submitting a PR — the bar for new skills is higher than for fixes or docs. See [CONTRIBUTING.md § Adding a new skill](../CONTRIBUTING.md#adding-a-new-skill-the-long-version) for the full process. Discipline-specific extensions to existing skills (e.g., adding CONSORT support to `manuscript-drafter`, or COREQ to `qualitative-coding`) are usually preferable to new skills and don't require an upfront proposal — open a PR directly.

## How is this different from Elicit / Consensus / Scite / ResearchRabbit?

Those are SaaS products with their own UI, login, and subscription model. They live in your browser. research-co-pilot lives in *your tooling* (Claude Code in your terminal, claude.ai in the same session you use for everything else). It composes with the artifacts you already have on disk (Word docs, PDFs, BibTeX files, transcripts) and produces artifacts that stay with you. No login, no subscription separate from your Claude one, no SaaS lock-in. You can fork the plugin, modify a skill, and run your version.

The trade-off: it doesn't have a curated paper database. The `literature-review` skill searches the web, the user's provided files, and standard academic indexes (Google Scholar, PubMed, arXiv, OSF, Semantic Scholar) — it doesn't have its own corpus. For database-grade citation graphs, Scite / Consensus / Elicit may be better tools to use *alongside* this plugin.

## Does it run locally or call APIs?

Skills run in Claude (the underlying LLM is hosted by Anthropic), so prompts and content reach Anthropic's servers. Inside that, some skills also issue web searches (e.g., `literature-review` for source verification) — those calls go to the relevant search APIs, with snippets of your input. Skills that execute Python (`data-analysis`, `peer-review` on PDF / PPTX, `qualitative-coding` for NLP) run that Python in the relevant sandbox (Claude Code uses your local shell; claude.ai uses its analysis-tool sandbox).

Nothing is uploaded to a third-party server *by the plugin itself*. The plugin is markdown skill files; it doesn't introduce new network endpoints. Whatever the model does in service of running a skill, however, depends on the underlying Claude environment.

## What if I find a bug?

Open a [bug report issue](../../issues/new?template=bug.md). The template walks you through the reproduction details. If it's security-relevant, follow the [SECURITY.md](../SECURITY.md) disclosure process instead.

## How do I cite the plugin formally in my methods section?

Use the `CITATION.cff` at the repo root — GitHub renders a "Cite this repository" button that produces APA, BibTeX, and other formats. Once the v0.10.0 final tag ships, the plugin will also have a Zenodo-minted DOI for permanent reference.

For now, a generic citation:

> Arazi, M. (2026). *research-co-pilot: a Claude co-pilot for the entire research lifecycle* (Version 0.10.0) [Computer software]. https://github.com/Marazii/research-co-pilot

## What's the license?

MIT (see [LICENSE](../LICENSE)). Free for academic and commercial use. Attribution required when redistributing.

## Is there telemetry?

No. The plugin does not collect, log, transmit, or store usage data. The author has no way of seeing what skills you've used or what content you've processed. Anthropic's standard Claude API policies apply to whatever you send to the model (read those separately on their site); the plugin doesn't add anything on top.

## What does "research co-pilot" mean — why not "research assistant"?

Naming choice. "Assistant" implies a hierarchical, subservient helper that does what you ask. "Co-pilot" implies a peer who flies with you, sometimes pushes back, and brings their own discipline. The plugin's skills are designed to refuse common AI mistakes even when the user asks for them — pushing back on weak methodology, refusing to fabricate citations, flagging when a claim isn't grounded. That's co-pilot behavior, not assistant behavior. (Yes, this is reflected in the naming convention across the manifests and README.)

## Where can I see what's coming next?

The [CHANGELOG.md](../CHANGELOG.md) records every shipped version. Active development plans are in the GitHub issues. For broader direction, see the most recent PRD under `docs/prd-vX.Y.Z.md` (when present).

## How do I uninstall?

```bash
claude plugin uninstall research-co-pilot@research-co-pilot-marketplace
claude plugin marketplace remove research-co-pilot-marketplace
```

For claude.ai: go to Settings → Capabilities → Skills and remove each uploaded skill. No residual files outside those locations.
