# Peer Review Skill

A skill for Claude that turns it into a rigorous academic peer reviewer.

## Author

Designed by Maya Arazi. Maya specified the requirements, made the design calls (workflow modes, voice, hard rules, division of labor between structured review and inline annotations, anti-sycophancy posture), and refined the skill across an extended back-and-forth. Implementation by Claude (Anthropic).

## What it is

A peer-review skill that produces the kind of academic feedback a seasoned professor would give: rigorous, methodical, substantive, neither cruel nor deferential. It supports multiple review styles for different needs:

- A single-reviewer evaluative review for finished work (papers, homework).
- A committee panel of 3 to 5 reviewers with deliberate diversity, including an adversarial member by default.
- A fact-check audit for AI-assisted writing (verifies citations, detects hallucinations).
- A plagiarism audit (detects lifted text, paraphrased arguments, uncredited concepts).
- A thinking-partner mode for unfinished drafts.
- An iterate mode for back-and-forth dialogue after any review, including structured revision-diff comparison when the author returns with a revised version.

For Word documents, the skill produces an annotated copy with inline comments and tracked changes alongside the structured review, mirroring how a real professor returns a marked-up paper.

The skill auto-detects:
- Language (Hebrew or English; Hebrew defaults to feminine grammatical form for the addressee).
- Academic domain (any field; not constrained to a fixed list).
- Genre (empirical study, lit review, theoretical paper, public-facing essay, dissertation chapter, etc.).
- Content types present in the work (prose, figures, tables, equations, code, algorithms).

## What it does

For a typical invocation, the skill produces:

1. A **structured review** delivered in chat, organized as:
   - TLDR (verdict, top strength, top issue, in 2 to 4 sentences)
   - Header (mode, language, genre, domain, content-type inventory, reviewer's confidence calibration)
   - Summary of central claims (faithful reconstruction of the work in the reviewer's words)
   - Primary strengths (numbered, in priority order)
   - Major issues (numbered, in priority order, with location, what is wrong, why it matters, concrete revision suggestion)
   - Minor issues (compact list, ordered by impact)
   - From good to brilliant (what would lift the work from competent to outstanding)
   - Verdict (Accept / Minor revisions / Major revisions / Reject for papers; grade band for homework)

2. An **annotated docx** (when a Word document is provided), with:
   - Inline comments at substantive trouble spots, framed conversationally for argument engagement and surgically for surface flags.
   - Engagement with the user's existing comments (replies threaded as conversation, not silent override).
   - Tracked changes for line-edit work (typos, awkward phrasing, terminological tightening).

Volume of comments and edits is derived from the quality of the work, not from a target. A perfect paper gets no annotations; a paper needing work on every sentence gets annotations on every sentence.

## How it works

### Architecture

The skill is structured as a main `SKILL.md` file plus three reference files in a `references/` directory.

```
peer-review/
├── SKILL.md                 # The spine: workflow, modes, hard rules
└── references/
    ├── domain-lenses.md     # Universal template + 14 worked examples
    ├── genre-lenses.md      # 14 academic genres with criteria
    └── content-types.md     # Non-prose content evaluation
```

The reference files are loaded on demand: domain lenses when the work's domain is identified, genre lenses when the genre is identified, content-types when non-prose elements are present.

### Workflow

The skill operates in steps:

1. **Identify mode** along three axes: verdict register (paper or homework), workflow (default single reviewer, or one of: committee, fact-check, plagiarism-check, draft), and genre (auto-detected). Long works trigger a focus prompt before reading.
2. **Detect language**.
3. **Identify domain(s) and articulate rigor criteria** for the relevant field, using the universal template in domain-lenses.md.
4. **Read like a reviewer**, not a skimmer: reconstruct claims, identify load-bearing arguments and evidence, surface hidden assumptions, check internal consistency, inventory non-prose content, identify the reviewer's own limits in the context of this specific work.
5. **Produce the structured review** in the canonical format.
6. **Annotate the source document** (for docx inputs) with inline comments and tracked changes; verify before delivery that all annotations actually render in Word.
7-10. **Alternative workflows** if invoked: committee panel, fact-check audit, plagiarism audit, draft mode for unfinished work.
11. **Iterate** in back-and-forth dialogue after the review, with anti-sycophancy enforcement and revision-diff capability.

### Voice and posture

The reviewer's voice is "seasoned professor": direct, substantive, specific. Charitable but not deferential. Pedagogical in homework mode, peer-collegial in paper mode. Never sneering, never gushing. The reviewer steelmans the author's argument before attacking it, and only attacks where attack is warranted.

### Anti-sycophancy

The skill has a hard rule against caving to social pressure in iterate mode. It updates positions only on substantive grounds (factual error, missed consideration, defeating reframe, defeating citation), not because the user expressed displeasure, repeated their objection more forcefully, invoked authority, or said "you're being too harsh." This rule applies with extra force when reviewing work that is itself about sycophancy, but it applies in all cases.

## What it's for, and what it isn't

### Purposes

- Substantive peer review of papers being prepared for submission.
- Homework grading and feedback by instructors.
- Self-review before submission, including pre-submission citation audits.
- Direction-finding on early drafts before they harden.
- Continuing engagement with a prior review (defending, refining, or reconsidering positions).
- Stress-testing arguments via committee mode with an adversarial voice.
- Audit of AI-assisted writing for hallucinations and made-up sources.

### Not for

- **Ghostwriting reviews.** The skill is meant to produce feedback for the author, not reviews to be submitted under someone else's name to a journal or institutional review process.
- **Validation or encouragement.** The skill will praise what is good but will not produce reviews calibrated to make the author feel better. If you want validation, use a different tool.
- **Replacing actual domain experts.** For very specialized technical content (formal proofs in advanced mathematics, niche subdisciplinary debates, code in unfamiliar languages, methods at the edge of standard practice), the skill is honest about the limits of its competence and recommends a domain expert. It does not pretend to uniform expertise.
- **Final authority on contested matters.** The skill renders verdicts and direction assessments; it does not pretend these are uncontroversial. Reasonable reviewers disagree; the skill's view is one view.
- **Institutional plagiarism detection at full corpus scale.** The plagiarism-check mode uses web search plus an open-access cascade (arXiv, biorxiv, Unpaywall, OpenAlex, CORE, etc.) and supports user-supplied source content for sources the skill cannot reach. This covers the open-access landscape and any specific source the user can share, but does not match the full subscription-corpus coverage of Turnitin and iThenticate (which include, e.g., the cumulative database of submitted student papers across thousands of institutions). For high-stakes submissions, complement this skill with such tools.
- **Reviewing non-textual work.** The skill is built for text-based academic work. It cannot review visual art, performance, music, or other media where the medium itself is the argument.

## How to use

### Basic invocation

The simplest form:

```
/peer-review
```

Then submit the work (paste text, attach a .docx, attach a PDF) and the skill auto-detects what it can: paper vs. homework, language, genre, domain.

### Common combinations

| Invocation | Use when |
|------------|----------|
| `/peer-review --paper` | Reviewing a journal-bound paper. |
| `/peer-review --homework` | Grading or reviewing a student submission. |
| `/peer-review --committee` | Panel review with deliberate diversity, including an adversarial voice. |
| `/peer-review --paper --committee` | Pre-submission stress-test with multiple expert perspectives. |
| `/peer-review --fact-check` | Audit citations, sources, and factual claims (especially for AI-assisted writing). |
| `/peer-review --plagiarism-check` | Audit for lifted content from existing sources. |
| `/peer-review --fact-check --paper` | Pre-submission verification followed by substantive review on the verified content. |
| `/peer-review --draft` | Generative thinking-partner feedback on unfinished work. No verdict; direction-level guidance. |
| `/peer-review --iterate` | Continue dialogue after a prior review (only valid after a previous review in the conversation). |

Flags compose freely. Verdict register (paper, homework) and workflow (default, committee, fact-check, plagiarism-check, draft) are independent axes. Iterate is an interaction layer that applies after any of these.

### Submitting work

The skill accepts:
- Plain text pasted into the conversation.
- Markdown files.
- Word documents (.docx). When provided, the skill produces an annotated copy in addition to the structured review.
- PDF files. Substantive review works on PDFs; for inline annotations, the user can convert to docx first.

### Reading the review

The TLDR at the top is designed to be readable in 30 seconds. The Header states the reviewer's confidence calibration explicitly: where the reviewer is operating outside its sharpest range, this is named, not concealed.

Sections are listed in priority order. The reader should be able to stop after the first item in any section (Strengths, Major issues, Brilliance) and still have the most important point.

### Iterate mode

After receiving a review, you can:

- **Defend a position**: explain why a flagged issue isn't actually an issue. The reviewer responds substantively. If your argument is good, the reviewer updates its position; if not, it pushes back.
- **Ask for elaboration**: "Expand on major issue 3" or "what would 'engaging the epistemic dependence literature' actually look like?"
- **Share a rewritten passage**: get a focused mini-review of just that section.
- **Submit a revised draft**: the reviewer compares against the prior version and assesses whether prior feedback was addressed (revision-diff).
- **Address committee members individually**: "Reviewer A, defend your point about confounds."

## Best practices

- **Include relevant context.** "This is for a philosophy of mind workshop with a 20-minute presentation slot," "this is a draft for a journal that requires pre-registration," "this is homework for an intro statistics course." The skill calibrates to context when context is provided.
- **For long work, specify focus.** When the work is over ~8000 words, the skill will ask. Answer concretely: which sections need deep attention, which can be skimmed. A skimmed deep review is worse than a focused deep review.
- **For unfinished work, opt into draft mode explicitly.** The default is to treat every submission as a final draft. If you want thinking-partner feedback rather than evaluation, use `--draft` or describe the work as unfinished. The skill will ask if it sees obvious stub markers but you didn't say.
- **Don't soften the reviewer's feedback when paraphrasing it to others.** The skill is calibrated to be substantively honest. Paraphrasing toward gentler language sometimes undermines the substance.
- **Use iterate mode actively.** The initial review is a starting point. The most useful work often happens in the back-and-forth: defending good ideas, conceding when wrong, refining what was misframed.
- **For AI-assisted writing, run fact-check before sharing.** Hallucinated citations are common in LLM-generated text. The fact-check workflow catches them.
- **For high-stakes submissions, run committee mode.** A panel will catch what a single reviewer misses, and the disagreements between members are themselves informative.
- **Supply source content for paywalled or private sources.** When fact-check or plagiarism-check flags a source as METADATA VERIFIED / CONTENT NOT ACCESSED, the skill cannot reach the full text directly but the verification can be completed if you supply the source material. Paste the abstract, attach the PDF, or share the relevant passage in iterate mode. This is also the way to check a draft against a colleague's confidential manuscript or a paywalled book without an OA copy.

## Customization

### Custom persona

Override the generic seasoned-professor voice with a specific persona: "review this as Prof. Y" or "review this as a hostile peer reviewer at Nature." The skill honors the persona while keeping the structural rigor of the protocol intact.

### Custom committee composition

Specify committee members by description: "one philosopher of mind, one ML researcher, one feminist epistemologist." The skill instantiates members matching the description. By default an adversarial member is added; opt out with `--no-adversary` or double up with `--double-adversary` for stress-test-heavy work.

### Severity calibration

Severity is set per committee member. To bias toward harshness, request "two harsh members and one moderate." To bias toward generosity, request the inverse. The Adversary is harsh by definition (its job is to break the argument).

### Modifying the SKILL.md

For users who want to permanently change defaults, edit the SKILL.md file directly. Common modifications:
- Change the default committee size from 3 to a different number.
- Adjust the long-work threshold (~8000 words) up or down.
- Change the verdict register vocabulary for non-journal contexts.
- Add domains or genres to the reference files.

The skill is designed to be readable and editable; its rules are explicit rather than implicit.

## Limitations

### Search-based verification

Both fact-check and plagiarism-check rely on web search and web fetch, supplemented by an open-access cascade and a user-supplied content workflow for cases the skill cannot reach directly.

**Open-access cascade.** Before flagging any source UNVERIFIABLE, the skill systematically checks for legal open-access copies across arXiv, biorxiv, medrxiv, ChemRxiv, PsyArXiv, SocArXiv, SSRN, RePEc, Unpaywall, OpenAlex, CORE, OpenAIRE, Semantic Scholar, Google Scholar's "All N versions" feature, author personal pages, and institutional repositories. Many "paywalled" papers have legitimate free copies; the cascade ensures the skill finds them rather than declaring sources unreachable when they aren't.

**User-supplied content workflow.** When a source genuinely cannot be reached (paywalled with no OA copy, not digitized, in a private corpus, in a colleague's confidential manuscript), the skill flags the entry as METADATA VERIFIED / CONTENT NOT ACCESSED rather than UNVERIFIABLE, and explicitly invites the user to supply the source material. The user can paste the abstract, the relevant passage, the full PDF, or a trusted summary. The skill then re-runs verification against the supplied content and updates the status. For plagiarism-check, the user can supply candidate source material (e.g., a colleague's manuscript) for the skill to check against. Verification based on user-supplied content is reported as such, and the skill cannot independently verify that supplied content is genuinely from the cited source; it rests on the user's good faith.

What the skill still cannot do:

- **Bypass paywalls without user help.** The skill does not have institutional access to publisher databases. For sources outside the open-access cascade, it depends on the user supplying material if content-fidelity verification is needed.
- **Match institutional plagiarism tools.** Turnitin, iThenticate, and similar tools have access to subscription corpora the skill does not. For high-stakes submissions, complement with such tools. The skill's plagiarism-check covers the open-access landscape and user-supplied sources well, but cannot match institutional coverage of, e.g., the full corpus of submitted student papers across universities.
- **Verify genuinely unreachable content (without user help).** A paper that exists but is paywalled, has no OA copy, and the user does not supply will remain METADATA VERIFIED / CONTENT NOT ACCESSED. The skill is explicit about this rather than guessing.
- **Confirm the provenance of user-supplied content.** If a user supplies fabricated text claiming it is from a cited source, the skill cannot detect the deception. The verification rests on the user's good faith, and this is stated in the report.

### Domain depth varies

The skill is competent across a wide range of academic fields, but the actual depth of competence varies. It is honest about this: the Header in every review states the reviewer's confidence calibration for the specific work in front of it. For very specialized technical content, the skill recommends a domain expert and does not pretend uniform expertise.

### Genre coverage is illustrative, not exhaustive

The reference file lists 14 genres with criteria. For genres not explicitly listed (e.g., a Festschrift, a manifesto, a research log, a poster paper), the skill applies the closest fit and notes the limitation in the Header.

### Hebrew defaults to feminine grammatical form

The skill addresses Hebrew speakers in feminine grammatical form by default, reflecting the original designer's preference. For users wanting masculine grammatical form, this can be specified at invocation ("address me in masculine form") or changed in SKILL.md.

### Em-dash typography

The skill is hard-ruled against using em-dashes (—) in output, on the grounds that em-dashes are a common LLM-output marker and the skill's outputs should not look auto-generated. Commas, parentheses, hyphens, and semicolons are used instead. Users who prefer em-dashes can override this rule at invocation, or edit the SKILL.md.

### No verification of figures or images

The skill can describe and evaluate figures, tables, and equations when they are textually represented (caption text, equation source, table data). For figures provided as raster images embedded in a docx or PDF, the skill works from the visible content but cannot run statistical analysis on raw data behind the figure. For papers where the rigor of the figure depends on the underlying data and analysis, the skill flags this as a limitation in the Header.

### The skill is one reviewer's view

The verdict and direction assessments rendered by the skill are one calibrated view, not the final word. Reasonable reviewers disagree, and the skill is explicit when its judgment is operating outside its sharpest range. The output is designed to inform the author's own judgment, not replace it.

## Files

```
peer-review/
├── README.md                # This file
├── SKILL.md                 # Main skill specification
└── references/
    ├── domain-lenses.md     # Universal template + worked examples for academic fields
    ├── genre-lenses.md      # Evaluation criteria for 14 academic genres
    └── content-types.md     # Evaluation criteria for figures, tables, equations, code, etc.
```
