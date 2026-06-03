# citation-formatter

> Formats citations and bibliographies in any major academic style — APA 7, MLA 9, Chicago (NB and AD), Harvard, Vancouver, IEEE, AMA, and journal-specific. Converts between styles, builds reference lists from raw input, verifies DOIs, and generates BibTeX / RIS exports. Won't invent missing fields.

**Triggered by:** `/cite`, plus *"format this citation"*, *"convert to APA"*, *"bibliography in Chicago"*, *"reference list"*, *"BibTeX"*, *"fix my references"*, *"is this APA correct"*, *"Vancouver style"*, *"DOI verification"*.

**Inputs needed:**

- The citations to format (a raw list, a manuscript with citations to fix, a Zotero / Mendeley export, or just DOIs / URLs).
- Target style (APA 7, MLA 9, Chicago 17 NB or AD, Harvard, Vancouver, IEEE, AMA, ACM, Nature, or specific journal).
- Output format (inline citations, full reference list, BibTeX, RIS, EndNote XML).

**Output:**

- `references.md` (or in-place edit of the manuscript) with cleaned citations and reference list.
- BibTeX / RIS files when requested.
- For document-wide work: a consistency-check report listing in-text-vs-reference-list mismatches that were fixed and any entries that couldn't be verified.

**Introduced in:** [v0.1.0](../../CHANGELOG.md).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you're submitting tomorrow and your references are a mess, when switching a manuscript between journals with different citation conventions, when responding to a copy-editor's "fix these to journal style" comment, when building a BibTeX file from a Zotero export, when a reviewer caught a citation inconsistency in your manuscript, or when you want a document-wide cross-check that every in-text citation appears in the reference list and vice versa.

It is opinionated about not inventing missing fields. If a piece is missing (e.g., no page numbers for a web source), it uses the style's correct convention for "missing" — never fabricates.

## Example

**Input:** *"Fix all references in `./manuscript.md` to APA 7. Current state is mixed — some MLA, some Chicago, some just URLs."*

**Output:**

1. Every in-text citation extracted and audited.
2. Every reference-list entry re-formatted to APA 7 conventions (sentence-case article titles, italicized journal names, DOI as URL).
3. Document-wide cross-check: 3 in-text citations had no matching reference list entry — flagged with line numbers for user fix-up. 2 reference list entries had no in-text use — flagged.
4. Edge cases handled: 2 preprints (`[Preprint]` notation added), 1 dataset (`[Data set]` notation), 1 social-media post (with username, post date, truncated text), 1 personal communication (moved from reference list to in-text only per APA 7).
5. 1 DOI couldn't be verified → listed at the bottom as "could not verify — please confirm: <fields>".

See [`examples/citation-formatter/`](../../examples/citation-formatter/) for a worked sample.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`manuscript-drafter`** — manuscript-drafter produces drafts with `[CITATION NEEDED]` markers; citation-formatter cleans the bibliography after you fill them in.
- **`literature-review`** — lit-review's source list becomes the starter bibliography for citation-formatter.
- **`grant-writer`** — grant-writer often needs funder-specific citation styles; citation-formatter handles the conversion.

## Honest caveats

- **It verifies what it can.** DOIs are checked against CrossRef; metadata is cross-referenced; but published research changes (corrections, retractions). Treat the output as a strong first pass that you confirm.
- **Style-edition specificity matters.** APA 7 ≠ APA 6. MLA 9 ≠ MLA 8. Chicago 17 ≠ Chicago 16. The skill matches the version you specify.
- **Journal-specific styles** (e.g., Nature Communications, Cell Reports, Annual Review of Sociology) are matched by referencing their published author guidelines; for niche journals, point the skill at the guidelines URL.
- **AI-generated content citations** (ChatGPT, Claude outputs as tools) follow APA 7 conventions; this is an evolving area — verify against your target journal's policy.
- **Personal communications, social media, datasets, and preprints** are handled with current convention; for non-standard sources, the skill notes the citation pattern used.
- For comprehensive bibliography management (importing 200+ entries, deduplicating, organizing into collections), use a reference manager (Zotero, Mendeley) — this skill is for formatting and verifying, not for collection management.
