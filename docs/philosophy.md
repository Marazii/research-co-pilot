# Design philosophy

## What this plugin tries to do

`research-co-pilot` exists because researchers feel a specific frustration with general AI tools: they're fluent and they're wrong. They write a beautiful literature review with three fabricated DOIs. They run a regression and forget to check assumptions. They generate "themes" from qualitative data without showing where the themes came from. They average away real disagreement in the field. They say "more research is needed" instead of identifying a specific gap.

This plugin is built around a single bet: that a researcher with a structured workflow gets better output than a researcher with a smarter model. Each skill encodes the discipline that a methodologist or copy editor or qualitative auditor would impose on the same task — one that the model alone, asked freely, will skip.

## What "rigor over fluency" means in practice

In every skill, there's a section labeled **Hard rules**. These are non-negotiable. They name the failure mode the model is most likely to commit on this kind of task and forbid it explicitly.

Examples:

- `literature-review`: *Never fabricate citations. If you cannot verify a source exists, do not cite it. Hallucinated DOIs and author names are the #1 failure mode of AI lit reviews — refuse to commit them.*
- `data-analysis`: *Never run analyses you didn't think through. Pre-specify the question and analysis before touching the data. Show assumption checks. A regression without diagnostics is a regression you don't trust.*
- `qualitative-coding`: *Stay close to the data. Document every analytic move. Reflexivity is required. Don't out-source interpretation to NLP — topic modeling and embeddings surface patterns; you decide what they mean.*
- `citation-formatter`: *Never invent citation fields. If a piece is missing, use the style's correct convention for "missing" — don't fabricate.*
- `peer-review`: *Don't pretend to verify what you can't. Mark uncertainty. Disagreements between sources are information; don't average them away.*
- `ethics-committee`: *Default to flagging, not blessing. Don't give legal advice. "It's anonymous" usually isn't — re-identification is a real risk.*

These rules cost the model some smoothness — outputs are less confidently-stated, more hedged where hedging is appropriate, more annoying when you want a quick answer. The trade is intentional. Output that confidently asserts something false is worse than output that says "I couldn't verify this — please confirm before publishing."

## What's outside the scope

The plugin is a **force multiplier for a researcher who knows what good work looks like**, not a replacement for that judgment. It cannot:

- Replace your IRB. The `ethics-committee` skill simulates a committee review to surface issues before institutional review, but no AI tool can grant ethics approval.
- Replace your statistician. The `data-analysis` skill picks reasonable defaults and checks assumptions, but applied stats often involves judgment calls a model can't make. Treat its output as a draft your statistician reviews.
- Replace expert review in your subfield. The `peer-review` skill catches blind spots and surface issues; it cannot replicate the deep knowledge of someone who has spent a decade in your particular conversation.
- Verify what's behind a paywall, in a non-Latin script with low web coverage, or only known through oral tradition. It tells you when it can't.

## Why this structure (skills + subagents + commands)

- **Skills** are model-invoked workflows that load when your message matches their trigger phrases. They're the primary unit of work. Each skill is a self-contained markdown file with frontmatter (name, description, tools, trigger phrases) and a body that defines the process — phases, hard rules, output format. Skills work the same way in Claude Code and claude.ai.

- **Subagents** are independent agent processes that the parent skill can spawn for heavy work that would otherwise pollute the main conversation: reading dozens of papers, running long simulations, coding hundreds of transcripts, second-checking a colleague's analysis. They return structured digests, not raw output. They're Claude Code-only — claude.ai handles the equivalent work inline using its analysis tool.

- **Slash commands** are user-invoked entry points. They're a thin wrapper that hands off to a skill. They exist because researchers often know what step they're on (`/lit-review`, `/methodology`, `/code-themes`) and want direct access without having to phrase a request the model will route correctly.

The pattern is: a researcher invokes a slash command (or describes their need); the skill takes over and runs its workflow; if the work is heavy or independent, the skill spawns a subagent; final output goes to a markdown file (Claude Code) or downloadable artifact (claude.ai).

## What I tried to avoid

- **Skill bloat.** Each skill should do one thing well. There's a temptation to put everything-research-related into a single megaskill; that produces vague triggers and weak workflows. The plugin is split into ~12 skills, each named after a recognizable research activity.
- **Tool prescription.** Skills don't dictate "use scikit-learn" or "use NVivo"; they recommend reasonable defaults and adapt to what the user has. The discipline is in the workflow, not the tool choice.
- **Magic.** No hidden behavior, no autonomous side effects. Every output is reproducible from the saved script + the input + the skill body. Every analytic decision is logged.
- **AI-shaped output.** Generic "in conclusion, more research is needed" prose. Vague themes. Confident claims with no source. Every hard rule is one of these patterns, named explicitly so the model has a chance to refuse.

## What I'd change next

The current design optimizes for individual researchers. A future version might add:

- Lab- or team-level features (shared codebooks, multi-coder reliability workflows that span more than one user, shared methodology decision logs).
- Tighter integration with reference managers (Zotero, Paperpile) and qualitative software (NVivo, Dedoose, Atlas.ti).
- Domain-specific extensions (CONSORT for clinical trials, COREQ for qualitative health research, PRISMA-P for systematic-review protocols, ARRIVE for animal research).
- A "reproducibility audit" workflow that reads a published paper + its repo and reports how much of it can actually be re-run.

If something here is useful or missing, file an issue.

— Maya Arazi
