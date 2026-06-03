# The skill network

How the 14 research-co-pilot skills work together as an orchestrated network rather than 14 isolated tools.

The model is simple: **skills are nodes, shared artifacts are edges, and `/research` is the conductor.** A skill reads the artifacts produced upstream, does its one job well, writes a predictable artifact, and points at what comes next. No skill needs to know *how* another runs — only *where its output lands*.

This document is the single source of truth for the network. Each skill's `SKILL.md` carries a short `## Handoffs` section and links here for the full picture.

---

## The research lifecycle (DAG)

```
research-brainstorm
  └→ literature-review
       └→ methodology-advisor ──→ ethics-committee        (audit before data)
            ├→ survey-design          (if an instrument is needed)
            └→ [DATA COLLECTION — human gate, pipeline pauses]
                 ├→ data-analysis ──→ stats-validator (subagent, optional second look)
                 └→ qualitative-coding
                      └→ manuscript-drafter ──→ citation-formatter
                           ├→ peer-review            (pre-submission audit)
                           │    └→ reviewer-response  (after an R&R comes back)
                           └→ talk-builder           (conference talk from the paper)

grant-writer          ← draws on research-brainstorm + methodology-advisor (funding; parallel track)
replication-designer  ← draws on a target paper; can seed a fresh lit-review → methodology cycle
```

Read top to bottom as the typical order of a project. The branches are real forks: you analyze quantitatively *and/or* qualitatively; you go to peer-review *and/or* talk-builder; grant-writing runs in parallel whenever funding is in play.

### Subagents (Claude Code only — the isolation workers)

Some stages spawn a subagent to do heavy work without flooding the main conversation. These are not separate lifecycle stages; they are how a stage scales:

| Stage | Spawns | For |
|---|---|---|
| literature-review | `source-finder` | reading many sources in parallel |
| data-analysis | `data-cruncher` | many model variants / simulations / sensitivity grids |
| qualitative-coding | `transcript-coder` | bulk cleaning + coding across many transcripts |
| manuscript-drafter | `manuscript-drafter` (subagent) | long-form drafting in isolation |
| data-analysis / peer-review | `stats-validator` | independent second look on an analysis |

On claude.ai there are no subagents; the parent skill does the work inline in the analysis sandbox.

---

## The shared workspace (`.research/`)

When skills run as a connected project, they coordinate through a workspace directory rather than the user re-supplying paths at every step.

```
.research/
  manifest.json              # index of artifacts + project state
  lit_review_<topic>.md      # produced by literature-review
  methodology_<study>.md     # produced by methodology-advisor
  analysis_<topic>.md        # produced by data-analysis
  ...                        # each skill's existing output filename, under .research/
```

The filenames are exactly the ones each skill already produces (see each skill's Output phase). The only new convention is: **write them under `.research/`, and register them in the manifest.**

### Manifest schema

`.research/manifest.json` is a plain JSON file. Skills read and write it with ordinary file tools — no script required.

```json
{
  "project": "remote-work-mentorship",
  "language": "en",
  "stage": "drafting",
  "created": "2026-05-15",
  "artifacts": [
    {"skill": "literature-review",   "file": ".research/lit_review_remote_work.md", "status": "final"},
    {"skill": "methodology-advisor", "file": ".research/methodology_remote_work.md", "status": "final"},
    {"skill": "data-analysis",       "file": ".research/analysis_remote_work.md",    "status": "draft"}
  ]
}
```

- `stage` is one of: `ideation`, `review`, `design`, `ethics`, `instrument`, `data-collection`, `analysis`, `drafting`, `citations`, `pre-submission`, `submitted`, `revision`, `dissemination`. The conductor uses it to resume.
- `status` per artifact: `draft` or `final`.
- `language` lets downstream skills (especially manuscript-drafter) match the project's language without re-detecting.

### The knowledge layer: `facts` + `vault` (the research vault)

The manifest is the **file index**. On top of it sits the **research vault** — the project's knowledge layer (canonical facts, one bibliography, the decisions log, open questions, glossary, voice profile, entities). The manifest gains two additive blocks:

```json
{
  "...": "...base fields above...",
  "facts": {
    "sample_size":          {"value": 247, "source": "methodology-advisor", "status": "final"},
    "sample_size_analyzed": {"value": 240, "source": "data-analysis", "status": "final", "note": "after 7 attention-check exclusions"},
    "irb_number":           {"value": "IRB-2026-0142", "source": "ethics-committee", "status": "final"},
    "preregistration":      {"value": "https://osf.io/xyz", "source": "methodology-advisor"},
    "target_journal":       {"value": "J. Hypothetical Studies"}
  },
  "vault": {
    "bibliography":  ".research/vault/bibliography.md",
    "decisions":     ".research/vault/decisions.md",
    "open_questions":".research/vault/open-questions.md",
    "glossary":      ".research/vault/glossary.md",
    "voice_profile": ".research/vault/voice-profile.md",
    "entities":      ".research/vault/entities.md"
  }
}
```

Each fact carries **provenance** (`source`) and `status`, so drift-checking can diff facts against artifacts and attribute contradictions. The vault keeps legitimately-distinct facts (recruited N vs analyzed N) as separate keys with notes — never a silent overwrite. **The vault never holds PII** (pseudonyms only). Full contract — note formats, the read/update protocol, flag-on-write, and the `/vault audit` checks — is in [`docs/research-vault.md`](./research-vault.md).

### Two hard rules for the workspace

1. **Files are the source of truth; the manifest is advisory.** At intake, a skill reconciles the manifest against the actual files. If the manifest lists a file that does not exist, trust the filesystem and correct the manifest — never hallucinate the missing artifact's contents.
2. **The workspace is opt-in.** A skill invoked standalone with explicit paths and no `.research/` behaves exactly as it always has. The manifest is a convenience for connected projects, never a requirement.

---

## How a skill uses the network

### At intake

1. Check for `.research/manifest.json`.
2. If present, read it to discover the upstream artifacts this skill needs (see the skill's Upstream list) — instead of asking the user for paths.
3. **Read the vault.** Use `facts` (don't re-ask for sample size, journal, IRB#, language); cite from the canonical `bibliography.md` by key; use `glossary.md` terms; apply `voice-profile.md` where you write prose; consult `entities.md` and open `open-questions.md`.
4. Reconcile against the filesystem (rule 1 above).
5. If a needed upstream artifact is missing, follow the Chaining protocol below.

### At output

1. Write the primary deliverable to `.research/<conventional-filename>`.
2. Register or update its entry in the manifest (`skill`, `file`, `status`).
3. **Update the vault.** Deposit new facts (with provenance); append decisions with rationale; add verified citations to `bibliography.md`; register/resolve `[… NEEDED]` markers in `open-questions.md`; update `glossary.md`. **Flag-on-write:** before writing a fact or citation that *conflicts* with the vault, stop and surface it (it's usually a distinct fact, occasionally a correction) — never silently overwrite.
4. Advance `stage` if this skill completes a lifecycle stage.
5. Surface the natural next step(s) from the skill's Downstream list.

Full detail (note formats, the six `/vault audit` checks, the PII hard rule): [`docs/research-vault.md`](./research-vault.md).

---

## Cross-skill invocation (the Chaining protocol)

When a skill needs an upstream artifact that does not exist, or when it finishes and a downstream step is the obvious next move, it offers to chain. Behavior differs by surface but the *intent* is identical.

### Claude Code

- Skills carry `Skill` in their `allowed-tools`, so they can invoke another skill via the `Skill` tool — e.g. `Skill(methodology-advisor)`.
- **The human gate is mandatory.** A skill never invokes another skill silently. It states what is missing (or what comes next), and asks the user to confirm before chaining. Example:
  > "I don't see an analysis report in `.research/` — the Results section needs one. Want me to run `data-analysis` first? (I can invoke it now, or you can point me at an existing analysis file.)"
- Heavy stages may run in an isolated subagent via `context: fork` where appropriate.

### claude.ai

- There is no `Skill` tool, no subagents, no slash commands, no cross-session filesystem.
- The skill degrades to advisory prose:
  > "The Results section needs an analysis report. Run the `data-analysis` skill first (or describe your results inline and I'll proceed in one pass)."
- Within a single conversation, Claude can load the other skill's approach inline if the user wants to keep going without switching.

### The one rule that never bends

**Never invoke another skill without an explicit human go-ahead.** The network offers; the researcher decides. This is the "co-pilot, not assistant" principle made concrete — no surprise side effects, no auto-running a multi-hour analysis because a draft looked ready for one.

---

## Portability degradation table

| Mechanism | Claude Code | claude.ai |
|---|---|---|
| Shared workspace | `.research/` persists across sessions | sandbox filesystem within a session; re-upload artifacts across sessions; paste the manifest |
| Active invocation | `Skill(name)` tool, human-gated | "run /X next" → Claude loads X's approach inline if asked |
| Stage isolation | subagent / `context: fork` | inline in the analysis sandbox |
| Conductor | `/research` pipeline mode invokes stages | `/research` skill walks the stages sequentially in one conversation |

---

## The conductor (`/research`)

`/research` has two modes:

- **Router (single request):** keyword-routes one request to the single best skill. This is the default and is unchanged from earlier versions.
- **Pipeline (whole project):** triggered by "start a new project on X", "run the full pipeline", "take this from question to draft". The conductor reads/creates the manifest, walks the DAG, invokes each stage (Claude Code) or instructs the next sequential run (claude.ai), pauses at human gates (data collection, IRB approval, submission/R&R), skips stages whose artifacts already exist, and resumes from the manifest `stage` on re-entry.

See [`commands/research.md`](../commands/research.md) for the conductor's exact behavior.

---

## Per-skill handoff summary

The authoritative Upstream/Downstream lists live in each skill's `SKILL.md` `## Handoffs` section. Quick map:

| Skill | Reads from (upstream) | Hands to (downstream) |
|---|---|---|
| research-brainstorm | — (entry point) | literature-review, methodology-advisor, grant-writer |
| literature-review | research-brainstorm | methodology-advisor, manuscript-drafter, grant-writer |
| methodology-advisor | literature-review, research-brainstorm | ethics-committee, survey-design, data-analysis, qualitative-coding, manuscript-drafter, grant-writer |
| ethics-committee | methodology-advisor | (gate) → data collection; replication-designer |
| survey-design | methodology-advisor | data-analysis (once fielded) |
| data-analysis | methodology-advisor, survey-design | manuscript-drafter, stats-validator |
| qualitative-coding | methodology-advisor | manuscript-drafter |
| manuscript-drafter | methodology-advisor, data-analysis, qualitative-coding, literature-review | citation-formatter, peer-review, talk-builder, reviewer-response |
| citation-formatter | manuscript-drafter, literature-review | manuscript-drafter (back), peer-review |
| peer-review | manuscript-drafter | reviewer-response, manuscript-drafter (back for revisions) |
| reviewer-response | peer-review, manuscript-drafter | manuscript-drafter (revisions), citation-formatter |
| talk-builder | manuscript-drafter, literature-review | — (terminal: the talk) |
| grant-writer | research-brainstorm, methodology-advisor, literature-review | citation-formatter |
| replication-designer | a target paper (external) | methodology-advisor, ethics-committee |

---

## Design rationale (why this shape)

- **Artifacts over calls.** Coordinating through files keeps the skills decoupled. literature-review doesn't import methodology-advisor; it just leaves a file where methodology-advisor knows to look. This survives both surfaces and is debuggable (the artifacts are readable markdown).
- **Advisory manifest.** A manifest that could silently diverge from reality would be worse than none. Files win; the manifest is a fast index, reconciled at intake.
- **Human gates everywhere.** Research has expensive, irreversible steps (collecting data, submitting a paper). Auto-chaining across those would be reckless. The network proposes; the researcher disposes.
- **One contract, thin per-skill footprint.** This document holds the detail so each `SKILL.md` adds only ~20 lines and never bloats its description.
