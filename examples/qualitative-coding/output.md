# Qualitative Findings: Mentorship in the First Year of Fully-Remote Work

> **Synthetic example.** Two short transcripts. Output illustrates format only.

## Methods (brief)

- Tradition: reflexive thematic analysis (Braun & Clarke 2019).
- Approach: inductive.
- N=2 participants for this synthetic example (real study would target N=15-20 for saturation).
- Coding software: by hand for this small example.
- IRR: solo coder; not computed.
- Researcher positionality (synthetic): the coder works in tech, was hired in 2022, has a relevant prior to the topic. Captured fully in real use.

## Codebook (v1)

| Code | Definition | Inclusion | Exclusion | Example |
|---|---|---|---|---|
| `formal_mentor_absent` | Participant describes an assigned formal mentor relationship as not functioning, infrequent, or awkward | Assigned-mentor relationships explicitly described as weak/absent | Cases where assigned mentor is described positively | P02:1-3 |
| `informal_mentor_via_async_channel` | Mentorship received from non-assigned colleagues via async / written channels (Slack, PRs, docs) | Statements about learning from non-assigned senior colleagues asynchronously | Synchronous mentor relationships | P01:8-11 |
| `mentorship_as_career_advice` | Participant defines or describes mentorship as career-direction advice (stretch assignments, stakeholder handling) | Career-advice references | Tacit-knowledge / standards-learning references | P01:5-7 |
| `mentorship_as_tacit_knowledge` | Participant describes mentorship as learning unwritten rules / team standards | Standards/norms-learning references | Career-advice references | P02:5-9 |
| `no_sponsorship_in_room` | Participant explicitly notes absence of senior advocate in advancement / promotion decisions | Mentions of not having someone in advancement decisions | Mentorship-quality references | P02:11-15 |
| `geographic_inversion` | Remote inverts geographic access — gain access to more people async, lose proximity-based hallway contact | Statements about gaining/losing access via remote | General mentorship references | P01:14-18 |

## Coded data (excerpt)

```json
[
  {
    "transcript_id": "P01",
    "lines": "5-7",
    "text": "My manager was great about scheduling weekly one-on-ones, but those felt like check-ins, not mentorship.",
    "codes": ["mentorship_as_career_advice"],
    "memo": "Participant draws a sharp distinction between procedural check-ins (assigned) and mentorship (career advice)."
  },
  {
    "transcript_id": "P01",
    "lines": "8-11",
    "text": "The actual mentorship I got came from this informal Slack channel...",
    "codes": ["informal_mentor_via_async_channel"],
    "memo": "Async channel as substrate for unassigned mentorship. Note 'didn't feel like I was bothering them' framing."
  },
  {
    "transcript_id": "P02",
    "lines": "11-15",
    "text": "I didn't have the sense that anyone was pushing for me specifically. My manager was nice but they weren't an advocate.",
    "codes": ["no_sponsorship_in_room"],
    "memo": "Strong disconfirming case for any account that conflates mentorship with sponsorship — P02 has the former, lacks the latter."
  }
]
```

## Themes

### Theme 1: Mentorship vs sponsorship — participants distinguish them

Both participants describe receiving *something* (informal mentorship, async support) while explicitly noting the absence of sponsorship — someone advocating for them in decisions they aren't in the room for. P02 names this directly; P01 implies it. This is consistent with the sponsorship-vs-mentorship distinction in the pre-pandemic literature (Hewlett 2013), now showing up in remote-work testimony.

> *"I didn't have the sense that anyone was pushing for me specifically. My manager was nice but they weren't an advocate."* (P02:11-15)

### Theme 2: Async channels substitute for hallway contact — partially

Both participants describe Slack channels and PR reviews as the locus of actual mentorship. P01 emphasizes the *broader access* this provides (multiple time zones, more senior people available); P02 emphasizes *unwritten standards* surfaced through PR review. This is an emerging account of how mentorship reconstitutes remotely — it doesn't disappear, it relocates to asynchronous, written channels.

> *"That's where the real mentorship happened."* (P02:3-4, on PRs)

### Theme 3: Geographic inversion

P01's observation is theoretically interesting: remote work inverts geographic access. In a physical office, you mentor with the people on your floor; remote, you mentor with whoever happens to be active in your async channels — which can span time zones. The trade is incidental contact (lost) for breadth of access (gained). Whether this trade is net positive depends on what the mentee needs.

## Cross-cutting observations

- Both participants distinguish *mentorship* (knowledge transfer) from *sponsorship* (advocacy). This distinction is theoretically central and merits explicit operationalization in any survey instrument that follows.
- Disconfirming case: P01 is more positive about the remote setup; P02 more negative. The two are not in contradiction — they differ in what they prioritized (broad access vs in-room advocacy) — but a larger sample would clarify whether this is a personality-level or context-level difference.

## Reflexivity statement (template)

The coder works in tech, has direct experience with first-year remote work in the timeframe under study, and may share assumptions with participants about what mentorship "should" look like. The analysis explicitly checks claims against participants' own framings rather than the coder's expectations.

## Audit trail

- Codebook v1: this document.
- Coding decisions log: maintained alongside coded data; each ambiguous coding decision recorded with rationale.
- Memos: see "memo" field in coded data.

## Limitations

- N=2 transcripts in this synthetic example; real analysis would target saturation (typically N=15-20 for thematic analysis on a focused question).
- Both participants are tech-industry workers; transferability to other knowledge industries is open.
