# talk-builder

> Turns one or more papers into an academic talk — outline, per-slide content, speaker notes, opening hook, single take-home message, backup slides for Q&A, rehearsal plan. Adapts to length (3-min lightning through 90-min defense), audience, format, and discipline conventions. Produces deck-platform-agnostic outline plus optional Marp / Quarto / reveal.js / Beamer stubs.

**Triggered by:** `/talk`, plus *"turn this paper into a 12-min conference talk"*, *"job talk outline"*, *"thesis defense slides"*, *"keynote outline"*, *"lightning talk"*, *"invited talk"*, *"elevator pitch of my paper"*.

**Inputs needed:**

- The paper(s) — path to PDF / markdown / draft, or DOI / citation. One paper, multiple, or a thesis chapter.
- Talk length in minutes (including or excluding Q&A — be explicit).
- Format and venue — contributed / lightning / invited / plenary / keynote / symposium / workshop / defense / job talk / public lecture / course lecture.
- Audience description (specialists / general field / cross-disciplinary / clinical / public; approximate size).
- Goal — communicate a finding / sell a research program / defend a dissertation / recruit / win an award.
- Slide platform you'll use (optional but useful).

**Output:**

- `talk_<short_title>_<minutes>min.md` with: take-home message (one sentence) / beat-by-beat arc with timing / per-slide content (visual, on-slide text, speaker script, anticipated reaction, transition) / opening hook / closing / **3-5 backup slides for anticipated Q&A** / rehearsal plan (5 passes) / delivery notes / acknowledgments / paper / code links.
- Optional deck stub in Marp / Quarto / reveal.js / Beamer based on platform preference.

**Introduced in:** [v0.4.0](../../CHANGELOG.md#040--2026-05-10).

**Spec:** [SKILL.md](./SKILL.md)

## When to use this

Use this skill when you have a paper and need to turn it into a talk, when preparing a thesis defense or job talk (the high-stakes case), when adapting the same paper for multiple venues (a 12-min ACL talk vs. a 45-min job talk for the same paper need different framings), when responding to "can you give a 5-minute version" with something better than reading-the-abstract, and when you want backup slides ready for the difficult Q&A questions you don't want.

It refuses the most common talk-design failure modes: paper-recited-aloud, slides-as-teleprompter, no take-home, no hook, no backup for the dreaded questions.

## Example

**Input:** *"Turn `./paper.pdf` into a 12-minute contributed talk for ACL 2026. Audience: NLP specialists in the same subfield. I'm first author. Slide platform: Marp."*

**Output:** `talk_paper_12min.md` with:

1. **Take-home message** (one sentence): the single thing the audience should remember.
2. **Arc** — 10 beats, sum to 11 minutes (1 minute slack), per-beat audience-knowledge-gain and audience-feeling specified.
3. **12 slides**, each with: ≤6 words on screen, the one visual that carries the slide, 3-6 sentences of speaker script, anticipated specialist reaction, verbal transition to the next slide.
4. **Opening hook** (60 seconds): concrete example variant.
5. **3 backup slides** (B1-B3): the most likely difficult questions (did you compare to method X? what about confound Y? is the code available?) each pre-answered.
6. **Rehearsal plan** (5 passes: solo timing, solo recorded, friendly audience, hostile audience, final timing the day before).
7. **Marp stub** as `talk.md` you can open in Marp and present from.

See [`examples/talk-builder/`](../../examples/talk-builder/) for a worked sample including the Marp stub.

## Composes well with

*Part of the [skill network](../../docs/skill-network.md) — the lifecycle DAG and the `research/<project>/` vault live there. The pairings below are the human-readable view of this skill's `## Handoffs` section in its SKILL.md.*

- **`manuscript-drafter`** — The paper is usually the input; both skills should reference the same take-home message.
- **`peer-review`** in `--presentation` mode — submit your drafted slides to peer-review for a pre-conference critique.
- **`literature-review`** — For invited talks and keynotes that need to frame your work in the field's broader narrative, lit-review identifies the through-line.

## Honest caveats

- **The paper is not the talk.** The skill enforces cuts; if your instinct is "I need to cover everything in the paper" the output will feel sparse. That's the point.
- **Visual quality is yours to produce.** The skill specifies the figure, equation, or image that should carry each slide; it doesn't generate the visuals. For published-paper talks, reuse figures from the paper.
- **Discipline conventions matter** — a humanities argument-first opening at NeurIPS reads as confused; a CS live demo at AAA reads as flippant. The skill matches the discipline you specify; if you pick a non-matching pairing it will warn you.
- **Multi-paper talks** (job talks, keynotes) use the "single throughline" principle. The skill resists giving every paper equal time — the paper that most advances the throughline gets the most time.
- **Accessibility** guidance (color-blind palettes, font sizes, captioning) is built into the output but you implement it in your deck.
