# The research vault

The vault is the project's **knowledge layer** — the canonical facts, bibliography, decisions, open questions, glossary, entities, and voice profile that every skill reads at intake and updates at output. It sits on top of the v0.11.0 [skill network](./skill-network.md): the `manifest.json` is the *file index*; the vault is the *knowledge store*.

The point: **state knowledge once, read it everywhere, catch drift automatically.** Without the vault, the sample size is stated independently in the methodology, the analysis, and the manuscript abstract — and silently diverges. With the vault, "N = 247" lives in one place that every artifact reads, and a contradiction is flagged the moment it appears.

This document is the single source of truth for the vault. Each `SKILL.md` carries vault read/update lines in its `## Handoffs` section and links here.

---

## Hard rule: the vault never holds PII

**The vault stores pseudonyms and non-identifying attributes only.** The real-name → pseudonym key stays off-system, exactly as `qualitative-coding` already requires. `entities.md` may say "P03 — ICU nurse, 8 years' tenure"; it must never contain a real name, email, phone number, address, or any direct identifier. `/vault audit` actively scans for PII patterns and flags them 🔴. This rule does not bend.

---

## On disk

```
.research/
  manifest.json              # file index + facts block + vault registry
  vault/
    facts.md                 # human-readable project facts (mirror of manifest.facts) with notes + provenance
    bibliography.md          # canonical verified reference list — the single source of truth for citations
    decisions.md             # append-only log: date · skill · decision · rationale
    open-questions.md        # consolidated [… NEEDED] markers + design questions, each with status
    glossary.md              # canonical terms, operationalizations, abbreviations
    voice-profile.md         # extracted once by manuscript-drafter; reused downstream
    entities.md              # participants (PSEUDONYMS ONLY), sites, instruments, datasets, variables
  <artifact files>           # lit_review_*.md, methodology_*.md, … (the network's artifacts)
```

The vault is **opt-in**: a skill invoked standalone with explicit inputs and no `.research/` behaves exactly as before. The vault is a convenience for connected projects, never a requirement.

---

## The facts block (in `manifest.json`)

The structured half of the hybrid. `manifest.json` gains a `facts` block and a `vault` registry (additive to the v0.11.0 schema):

```json
{
  "project": "remote-work-mentorship",
  "language": "en",
  "stage": "drafting",
  "created": "2026-06-03",
  "facts": {
    "sample_size":          {"value": 247, "source": "methodology-advisor", "status": "final"},
    "sample_size_analyzed": {"value": 240, "source": "data-analysis", "status": "final", "note": "after 7 attention-check exclusions"},
    "irb_number":           {"value": "IRB-2026-0142", "source": "ethics-committee", "status": "final"},
    "preregistration":      {"value": "https://osf.io/xyz", "source": "methodology-advisor"},
    "target_journal":       {"value": "J. Hypothetical Studies"},
    "time_range":           {"value": "2024-08 to 2026-02"},
    "funding":              {"value": "NSF #1234567"}
  },
  "vault": {
    "bibliography":  ".research/vault/bibliography.md",
    "decisions":     ".research/vault/decisions.md",
    "open_questions":".research/vault/open-questions.md",
    "glossary":      ".research/vault/glossary.md",
    "voice_profile": ".research/vault/voice-profile.md",
    "entities":      ".research/vault/entities.md"
  },
  "artifacts": [ "...as in skill-network.md..." ]
}
```

Each fact is a typed value with **provenance** (`source` = the skill that set it) and **status** (`draft` / `final`), plus an optional `note`. Drift-checking diffs these against artifact contents.

**The distinct-facts principle.** `sample_size` (247, recruited) and `sample_size_analyzed` (240, after exclusions) are *both true* and *both kept*, as separate keys with notes — not a silent overwrite of one by the other. This is how the vault preserves the real story instead of flattening it into a contradiction. When a skill would write a value that differs from an existing fact, the resolution is usually "these are two distinct facts," recorded as such.

`facts.md` is the human-readable mirror of this block (same values, room for longer notes and provenance prose). Keep them in sync; the JSON block is what the audit keys on.

---

## The vault notes (markdown)

Each note has a fixed, simple shape so skills can append predictably.

### `bibliography.md` — the canonical reference list

The single source of truth for citations. Every source gets a stable **cite-key**; skills cite *by key* and never re-fabricate or re-format from scratch.

```markdown
## [smith2021]
- **Citation:** Smith, A., & Jones, R. (2021). Title of article. *Journal*, 12(3), 142–158.
- **DOI:** 10.xxxx/...   **Verified:** yes (literature-review, 2026-06-03)
- **Used in:** lit_review_remote_work.md, manuscript_discussion.md
```

- `literature-review` seeds it. `manuscript-drafter` cites by key. `citation-formatter` renders any style *from this list* (it is the input, not a parallel list). `grant-writer` and `reviewer-response` draw from it.
- A `[CITATION NEEDED]` is a claim whose source isn't yet here; a `[LITERATURE NEEDED]` is a new idea needing grounding. Both are tracked in `open-questions.md` until resolved into a verified entry here.

### `decisions.md` — append-only decision log

```markdown
- 2026-06-03 · data-analysis · Used a mixed-effects model (random intercept for school) instead of OLS · clustered data: students within classrooms within schools.
- 2026-06-03 · data-analysis · Excluded 7 participants who failed both attention checks · pre-specified in the analysis plan; documented for the methods + reviewer-response.
- 2026-05-30 · methodology-advisor · Chose difference-in-differences over cross-sectional regression · a feature rollout provides a credible counterfactual.
```

Never edited, only appended. This is the reproducibility spine — the methods section, the reviewer-response, and the pre-registration all draw from it.

### `open-questions.md` — consolidated markers

```markdown
- [ ] [CITATION NEEDED] — claim: "async channels span wider geographies than office proximity" · raised in: manuscript_discussion.md · owner: —
- [ ] [LITERATURE NEEDED] — claim: "sponsorship is harder to reconstitute remotely" · search: remote sponsorship, developmental networks · raised in: manuscript_discussion.md
- [x] [PRELIMINARY DATA NEEDED] — pilot effect size for the R01 aims · resolved 2026-06-02 (pilot n=24 added)
```

Every marker-emitting skill registers here; any skill can resolve. `/vault audit` lists the open ones and flags any that should block submission.

### `glossary.md` — canonical terms

```markdown
- **mentorship** — advice-giving and skill development (distinct from *sponsorship*). Operationalized via the Eby et al. (2008) scale.
- **sponsorship** — active advocacy in advancement decisions. Distinct from mentorship; see decisions log 2026-05-28.
- **HTE** — heterogeneous treatment effects.
```

Skills use the canonical form; `/vault audit` flags artifact term variants that drift from it.

### `voice-profile.md` — extracted once, reused

`manuscript-drafter` writes this (its Phase 3 voice profile). `talk-builder`, `grant-writer`, and `reviewer-response` *read* it so everything sounds like the same author. Format is the manuscript-drafter Phase 3 block (language, sentence length, person/voice, hedge intensity, signature phrases, connectors, citation style, punctuation, Hebrew register markers).

### `entities.md` — pseudonyms only

```markdown
## Participants
- P03 — ICU nurse, 8 yrs tenure, urban hospital   (pseudonym; real-name key off-system)
- P07 — ED charge nurse, 3 yrs tenure
## Instruments
- WOS — Workplace Outcome Suite (climate subscale)
## Variables
- post_test — 0–100 post-intervention score
```

**No PII.** See the hard rule at the top.

---

## The protocol (woven into each skill's `## Handoffs`)

### At intake — read the vault

1. Read `manifest.json` `facts` — **use them; do not re-ask** the user for the sample size, journal, IRB#, language, time range, etc.
2. Cite from `bibliography.md` by key — never re-fabricate or re-format.
3. Use `glossary.md` canonical terms; apply `voice-profile.md` (drafting / talk / grant / response); consult relevant `entities.md`; check open `open-questions.md`.
4. Reconcile against the filesystem — files are the source of truth; if a fact's artifact is gone, trust the file and correct the vault.

### At output — update the vault

1. Deposit new facts (with `source` + `status`); append decisions with rationale.
2. Add newly-verified citations to `bibliography.md`; register new `[… NEEDED]` markers and resolve any the skill closed.
3. Update `glossary.md`; `manuscript-drafter` writes `voice-profile.md` once.
4. Keep `facts.md` and the manifest `facts` block in sync.

### Flag-on-write — the rule that makes it rigorous

Before writing a fact or citation that **conflicts** with an existing vault value, STOP and surface it:

> "The vault records `sample_size` = 247 (from methodology-advisor). This analysis reports 240. Is 240 the post-exclusion analyzed N (a distinct fact), or a discrepancy to fix?"

Never silently overwrite a vault fact. Never silently emit a value into an artifact that contradicts the vault. Resolve first — usually by recording a distinct fact (the N-vs-analyzed-N pattern), occasionally by correcting an error. This fires only on genuine *conflict*, not on every write, so it doesn't nag.

---

## `/vault audit` — the six checks

Run on demand (`/vault audit`) or by the conductor before the pre-submission stage. Scans every artifact in `.research/` against the vault and writes `vault_audit_<date>.md` with severity-tagged findings.

1. **Fact consistency** — each fact vs. its appearances in artifacts (sample size, IRB#, journal, time range, prereg). Mismatch → 🔴 with file + location.
2. **Citation consistency** — every in-text citation resolves to a `bibliography.md` key; every entry is verified; no unresolved `[CITATION NEEDED]` / `[LITERATURE NEEDED]` at `pre-submission`+ → 🔴.
3. **Terminology** — artifact term variants that differ from the glossary → 🟡.
4. **Open questions** — list unresolved markers; flag any that should block submission → 🟡/🔴.
5. **Staleness** — facts/artifacts still `draft` at a late stage → 🟡.
6. **PII safety** — scan `entities.md` and `.research/` for apparent real-name PII (emails, full-name patterns) → 🔴.

Severity: 🔴 blocker · 🟡 review · 🟢 note.

---

## Portability

| Mechanism | Claude Code | claude.ai |
|---|---|---|
| Vault storage | `.research/vault/` persists across sessions | sandbox within a session; re-upload vault notes across sessions; paste the facts block |
| `/vault` command | available | the uploadable `vault` skill provides show/audit when invoked by name; no slash command |
| Audit scan | scans the filesystem | scans artifacts present in the conversation/sandbox |
| Flag-on-write | model-driven | model-driven (identical intent) |

---

## Design rationale

- **Hybrid, markdown-first.** Human-readable notes (git-friendly, hand-editable, no server) for the bulk; a small structured `facts` block for the scalars the audit must diff precisely. Best of both.
- **Files win; the vault is reconciled.** A knowledge store that could silently diverge from the artifacts would be worse than none. The vault is rebuilt-from-truth at intake and reconciled by the audit.
- **Distinct facts over overwrites.** Research knowledge is full of legitimately-different-but-related numbers. The vault preserves both and flags only genuine contradictions.
- **PII never centralizes.** A shared knowledge file is exactly where PII must not accumulate. Pseudonyms only; the audit enforces it.
- **One spec, thin per-skill footprint.** This document holds the detail; each `SKILL.md` adds only a few vault lines to its existing `## Handoffs`.
