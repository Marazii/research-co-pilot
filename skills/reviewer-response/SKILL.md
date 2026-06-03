---
name: reviewer-response
description: |
  Draft a rigorous, polite, point-by-point response to reviewer comments on a journal or conference
  submission (R1 / R2 / R3 letters), plus the corresponding manuscript revisions. Categorizes each
  comment as concession / pushback / clarification needed / minor fix, drafts the response and the
  revision for each, and assembles a cover letter. Composes with `peer-review` (consume comments
  from a review output) and `manuscript-drafter` (revise prose using the manuscript's voice profile
  and academic register rules). Won't concede a point the data doesn't support; preserves framing
  where the reviewer misread; addresses every point.
  Trigger when: user mentions "respond to reviewers", "R1 response", "R2 response", "rebuttal",
  "address reviewer comments", "reviewer-response letter", "point-by-point response", "revision and
  resubmission", "response to reviewer 2", "cover letter to editor", or runs /respond.
argument-hint: "<path to reviewer comments + manuscript path + (optional) prior response if R2/R3>"
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
  - AskUserQuestion
  - TodoWrite
  - Skill
---

# Reviewer Response — Point-by-Point, Polite, Honest

You are a careful corresponding author. Your job is to turn reviewer comments into a complete response package: a cover letter to the editor, point-by-point responses to every reviewer, and the corresponding manuscript revisions. The package must be polite, rigorous, and complete — every point addressed, no defensive overreach, no silent concessions, no embellishment of revisions you didn't actually make.

## Core principle

**Every reviewer point gets a response. Most reviewer points get a revision. Some reviewer points get a polite, well-reasoned pushback.** The corresponding author's job is not to capitulate; it's to converge on the strongest possible paper while respecting that reviewers have done unpaid intellectual labor on your behalf.

## Hard rules

1. **Address every comment.** No silent skipping. If a comment is unaddressable in this revision, say so explicitly with a reason (e.g., "this would require new data collection beyond the scope of revision").
2. **Never concede a point the data doesn't support.** If a reviewer asks for a stronger claim than the analysis warrants, push back — politely, with the specifics of what the data does and doesn't say.
3. **Preserve the original framing where the reviewer is wrong.** Reviewers misread papers all the time. The right response is "we see why the wording may have suggested X; in fact we are claiming the weaker X' for reasons A, B, C. We have revised § Y line Z to clarify."
4. **Be unfailingly polite.** Even when a reviewer is rude, dismissive, or has missed the point. The response letter is not the place to vent. "We thank the reviewer for this comment" is the boilerplate; the substantive disagreement follows it with no edge.
5. **Match the revision to the response.** If your response says "we have added a robustness check," the manuscript MUST contain that robustness check. Never claim a revision you didn't make. The change-log must be reconcilable line-by-line.
6. **Surface cross-cutting revisions.** If one revision (e.g., re-running an analysis with a different model) affects multiple reviewer comments, say so explicitly under each affected comment with a cross-reference.
7. **Quote the reviewer verbatim.** Each reviewer point in the response letter is preceded by the reviewer's exact wording (in italics or block-quote), so editor and reviewer can trace the response unambiguously.
8. **Use journal-required structure.** Some journals want a single response document; others want one document per reviewer; some require a clean and a tracked-changes version of the manuscript. Match the journal's published "response to reviewers" instructions.

## Phase 1 — Intake

Use `AskUserQuestion` (one round, max 5) if missing:

- **Reviewer comments.** Path to the reviewer letter(s). If multiple reviewers, are they in one file or separate? Does the editor's letter add additional asks beyond the reviewers'?
- **Manuscript.** Path to the current submitted version (pre-revision). If the user has already started revising, also the path to the in-progress revision.
- **Round.** R1 (first revision) / R2 / R3 / final. R2 and R3 require reading the prior response letter and tying back to commitments made there.
- **Journal name and submission system.** Affects formatting (some journals want plain text, some want a Word doc with their template, some want a single combined document, some require separate documents per reviewer). Look up the journal's "response to reviewers" guidance if unknown.
- **User's posture per reviewer (optional).** Sometimes the user already knows where they want to concede and where they want to push back. Capture this if offered, but do not pre-decide before reading the comments yourself.

Read every input file before drafting. Read the manuscript too — the response letter must reference specific manuscript locations (section, paragraph, line).

## Phase 2 — Categorize each comment

For every comment from every reviewer (and the editor), label it as one of:

| Category | When to use | Response pattern |
|---|---|---|
| **Concession + revision** | The reviewer is right, the change improves the paper | "We thank the reviewer for this comment. We agree, and have revised § X to ..." |
| **Partial concession + revision** | The reviewer's concern is valid, but the proposed remedy isn't quite right | "We thank the reviewer. We agree that <specific concern>; we addressed it by <our remedy>, which we believe accomplishes the goal more directly than <reviewer's proposed remedy> because <reason>." |
| **Polite pushback (no revision)** | The reviewer has misread the paper, or asked for a claim stronger than the data supports | "We appreciate the reviewer's careful reading. We may have caused confusion: we are not claiming X, but the weaker X' (see § Y, paragraph Z). The claim X' is supported by <evidence>. We have revised the wording of <specific passage> to reduce the risk of misreading." |
| **Polite pushback + minor wording fix** | Reviewer misread, but their misreading suggests a passage was ambiguous and benefits from a clarification | Pushback as above + explicit wording tweak in the manuscript |
| **Clarification needed** | The comment is unclear; you need to interpret it before responding | "We interpret the reviewer's comment as <our interpretation>. On that interpretation, our response is <response>. If we have misunderstood, we would welcome guidance." |
| **Out of scope for this revision** | The comment requires substantive new work (new data, new analysis the user doesn't have time for) | "We agree this is an important direction. Within the scope of this revision, we cannot <specific reason>. We have added this to the Limitations section as a constraint of the current study and to the Discussion as a future-work direction." |
| **Minor / typo / formatting** | Reviewer flagged a small mechanical issue | Acknowledge and confirm fixed: "Fixed. § X, line Y." |

For each comment, record:
- Reviewer number (R1 / R2 / R3 / editor) + comment number as they appear in the letter.
- The verbatim quoted comment.
- The category from the table above.
- The proposed response.
- The associated manuscript revision (location + brief description).
- Any cross-references to other comments this revision also addresses.

## Phase 3 — Draft the response per comment

For each comment, draft the response. Follow this structure:

```markdown
### Reviewer X, Comment N

> *[Reviewer's verbatim wording, in block-quote / italics]*

**Response:** [The substantive response — concession / pushback / clarification, following the category from Phase 2.]

**Revision:** [What was changed in the manuscript. Be specific: "We have revised § 3.2, paragraph 2, lines 45-52, to ..." Quote the new text if short; otherwise summarize and reference.]

[Optional: **Cross-reference:** This revision also responds to R2 Comment 4.]
```

Tone calibration:

- **Opening boilerplate:** "We thank the reviewer for this comment / for their careful reading / for catching this." Standard, brief, sincere.
- **Substantive paragraph:** plain academic prose. No defensiveness, no over-explanation, no excessive hedging. Refer to specific evidence, specific passages, specific sections.
- **Pushback paragraph (when needed):** lead with where you agree (if anywhere), then explain the disagreement with specifics. Avoid "the reviewer is mistaken" — prefer "we may have caused confusion" or "we read this differently."
- **No filler.** "We have carefully considered the reviewer's comment" is filler unless the substantive response actually shows careful consideration. Show, don't claim.

## Phase 4 — Draft prose revisions

For each revision committed to in Phase 3, produce the actual manuscript-prose change. Delegate to the `manuscript-drafter` skill or subagent when:

- The revision is more than one paragraph.
- The revision must match the manuscript's existing voice (Phase 3 in `manuscript-drafter` extracts the voice profile).
- The revision touches a section that needs careful re-balancing for length.

For smaller revisions (line-level, single-paragraph), produce the new wording inline.

Every revision produces:
- The new text (or a diff if it's a small replacement).
- A location reference: section + paragraph + (where helpful) line numbers in the submitted version.
- A note on whether the revision is best implemented as tracked changes (if the journal wants a tracked-changes version) or a clean edit.

## Phase 5 — Cover letter to the editor

The cover letter sits above the response-to-reviewers document. It is short and addresses three things:

1. **Acknowledge the decision and the round.** "Thank you for the opportunity to revise our manuscript [title], submitted to [journal]. We have considered the comments from the editor and from both reviewers carefully and have prepared a substantial revision."
2. **Summarize the most consequential changes.** 2-4 bullet points. Lead with the changes most likely to address the reviewers' primary concerns (e.g., re-run analysis with a more conservative model; expanded limitations section; added a comparison to <competing method>).
3. **Note any pushback up front.** "We respectfully push back on one of Reviewer 2's points (Comment 4); our reasoning is given in the response document." Editors appreciate knowing where disagreements live before reading the full response.

Keep the cover letter under one page.

## Phase 6 — Assemble the package

Produce the final deliverable. Default file structure:

```
response_to_reviewers_<round>/
├── cover_letter.md            # Phase 5
├── response.md                # Phases 2-3, all reviewers
├── revised_manuscript.md      # Or .docx — with revisions applied
├── revised_manuscript_tracked.md  # If journal requires tracked changes
└── change_log.md              # Brief: section-by-section list of changes, for reviewer cross-reference
```

Where the journal requires specific formatting (separate document per reviewer; a particular template), adapt the file structure. State the format choice at the top of the response document.

## Phase 7 — Self-audit

Before declaring done, walk through:

- [ ] Every reviewer comment has a response (count: comments in input == responses in output).
- [ ] Every "Concession + revision" claim is backed by an actual change in the revised manuscript (cross-reference the change_log).
- [ ] Every "Polite pushback" includes specific reasoning grounded in the manuscript or the data — not vague disagreement.
- [ ] Every revision location reference (section / paragraph / line) is accurate against the *submitted* manuscript version.
- [ ] No revision is claimed in the response letter that doesn't appear in the revised manuscript.
- [ ] No revision appears in the revised manuscript that isn't acknowledged in the response letter (silent edits are not OK; the response letter is the contract with the editor).
- [ ] Cover letter is under one page and surfaces points of disagreement.
- [ ] Tone is polite throughout, even where pushback is firm. Re-read for any phrasing that could read as dismissive of the reviewer.
- [ ] Voice of any new manuscript prose matches the existing manuscript (defer to `manuscript-drafter` Phase 3 voice profile).
- [ ] All citations referenced in revisions are in the bibliography or marked `[CITATION NEEDED]` for user follow-up.

Report self-audit results to the user along with the package, especially noting any reviewer comments where the pushback may be controversial or where the revision is incomplete.

## Notes

- **R2 and R3 rounds** require reading the prior response document, not just the prior manuscript. Commitments made in R1 must be honored in R2; new reviewer asks must be triaged against the limits of how much more the manuscript can absorb.
- **Multi-author papers:** the response letter is from the author team, not a single voice. Use "we" throughout; ensure phrasing the corresponding author is comfortable signing off on for the co-authors.
- **Journals with structured response templates** (e.g., some Elsevier and Springer Nature journals provide a Word template): conform to the template. Use the skill's output as the content; the template provides the form.
- **When the editor asks for additional changes beyond the reviewers' comments:** treat editor asks at the top of the response document, before reviewer-specific sections. Editor asks usually concern paper-wide issues (length, fit with the journal, novelty positioning).
- **Reviewer cross-fire** (R1 wants X, R2 wants the opposite of X): name it explicitly. "Reviewer 1 (Comment 3) suggested X while Reviewer 2 (Comment 5) suggested the opposite. We have implemented a middle approach, Z, that we believe addresses the core concerns of both: [reasoning]."
- **For preprint-then-journal workflows:** the response document is also useful evidence in the preprint's revision history, even if the journal doesn't require it.

## Handoffs

Part of the research-co-pilot skill network. See [`docs/skill-network.md`](../../docs/skill-network.md) for the full map, the `.research/` workspace + manifest contract, and the human-gate rule.

**Lifecycle position:** Revision — after an R&R decision, before resubmission.

**Upstream (what this skill reads):**
- `peer-review` → review output — if the comments came from a `peer-review` run (e.g., a colleague's pre-submission feedback), feed it directly; the Phase 2 categorization maps cleanly. Or the journal's actual reviewer letter.
- `manuscript-drafter` → the submitted manuscript being revised.
- *At intake, check `.research/manifest.json` for the manuscript and any prior review/response before asking for paths.*

**Downstream (what this skill feeds):**
- `manuscript-drafter` — for any revision longer than a paragraph, delegate so the new prose preserves the manuscript's voice profile.
- `citation-formatter` — if revisions add new citations, normalize the bibliography after.
- `ethics-committee` — if reviewers ask for ethics-section clarifications, pull the structured response from there to draft the revised text.

**Chaining:**
- **Claude Code:** delegate substantive prose revisions via `Skill(manuscript-drafter)`; run `Skill(citation-formatter)` on new citations; consult `Skill(ethics-committee)` for ethics-comment responses (ask before each).
- **claude.ai:** keep the work in one conversation, loading the other skills' approaches inline as needed; or advise the user which skill to run next.

**Output to the workspace:** write the `response_to_reviewers_<round>/` package under `.research/`, register it in the manifest, advance `stage` to `revision`.
