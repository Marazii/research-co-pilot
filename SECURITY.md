# Security Policy

## Reporting a vulnerability

If you find a security issue in this plugin — for example, a skill that mishandles user-provided files, a script that runs unintended commands, or anything that could compromise a user's data — please report it privately.

**Preferred channel:** open a [GitHub security advisory](https://github.com/Marazii/research-co-pilot/security/advisories/new) on this repository. GitHub keeps the report confidential until disclosure.

**Alternative:** open a regular GitHub issue **without sensitive details** and ask for a private contact.

Please don't post exploit details in public issues, pull requests, or discussions until a fix is released.

I aim to acknowledge reports within 7 days and to publish a fix or workaround within 30 days where feasible. If the issue affects an upstream dependency rather than this repo's own code, I'll route it appropriately and let you know.

## Scope

In scope:
- Skill, subagent, or slash-command files in this repo (`skills/`, `agents/`, `commands/`).
- Helper scripts (`scripts/`).
- Plugin / marketplace manifests (`.claude-plugin/`).

Out of scope:
- Vulnerabilities in Claude Code or claude.ai themselves — please report those to Anthropic directly.
- Vulnerabilities in third-party tools that skills happen to mention (e.g., a CVE in `pandas`).

## What to consider before pasting sensitive data into a skill

The skills in this plugin are designed to refuse common AI failure modes, not to provide privacy or compliance guarantees. A few things to keep in mind:

- **Web search.** Skills like `literature-review`, `methodology-advisor`, and `citation-formatter` may issue web searches that send fragments of your input to external search APIs. Don't paste secrets, identifying participant data, or unpublished findings into a skill that will then search the web for them.
- **Document files.** When you upload a file to claude.ai or read a file in Claude Code, that content reaches the model. Anonymize qualitative transcripts and clinical records before processing — see the `qualitative-coding` skill's anonymization step.
- **HIPAA / GDPR / IRB-protected data.** This plugin is not a HIPAA-compliant service and is not a substitute for your institution's data-handling policies. Check with your IRB / data protection officer before running protected data through any AI tool.
- **API logs.** Anthropic's data retention and abuse-monitoring policies apply to anything sent to their API. Review their published policies before deciding what's appropriate.

The `ethics-committee` skill includes a more thorough discussion of these considerations as part of its workflow.
