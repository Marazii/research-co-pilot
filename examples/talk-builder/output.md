# Talk: Our Paper at Hypothetical NLP 2026

> **Synthetic example.** 7-min talk + 5-min Q&A, contributed slot.

**Length:** 7 min talk + 5 min Q&A
**Venue:** Hypothetical NLP 2026, contributed talk
**Audience:** NLP specialists, ~30 in room
**Speaker:** [user, first author]
**Slide platform:** Marp (see `talk.md`)

## Take-home message (one sentence)

> Our method outperforms the prior SOTA on the target benchmark while requiring 4× less compute — and the gain comes from a single architectural choice, not from scale.

## Arc (beat-by-beat with timing)

| Beat | Time (s) | Slides | Audience knows by end | Audience feels |
|---|---|---|---|---|
| 1. Hook — concrete pain | 45 | 1-2 | The reviewer-fatigue problem is concrete + costly | Curious |
| 2. The question | 30 | 3 | Specific question this paper answers | Oriented |
| 3. What's known | 45 | 4 | Two prior approaches + their limits | Familiar |
| 4. Our approach in one sentence | 30 | 5 | The architectural choice | Anticipating |
| 5. Method (selective) | 60 | 6-7 | The key mechanism (skip parameter-count tables) | Engaged |
| 6. Headline result | 75 | 8-9 | SOTA gain + 4× compute reduction | Persuaded |
| 7. The surprise | 45 | 10 | Where the gain comes from (single component) | Surprised |
| 8. Limitation | 30 | 11 | Honest constraint of the result | Trusting |
| 9. Take-home + what's next | 30 | 12 | The single sentence + 1 follow-up question | Memorable |
| 10. Acknowledgments + Q&A primer | 15 | 13 | Whose work this is + how to start Q&A | Ready |

**Total:** 405 seconds = 6.75 min talk + 5 min Q&A. ~15 seconds of slack.

## Per-slide content

### Slide 1 — Hook
**Time:** 30s | **Beat 1** | **Visual:** One image — a wall of automated review feedback that contradicts itself. **On-slide text:** *"Every paper. Every conference."* | **Speaker says:** "Show of hands — who got an automated review last cycle that contradicted itself? *[pause]* Half the room. That's the problem this paper is about." | **Transition:** "Specifically..."

### Slide 2 — Hook continued
**Time:** 15s | **Beat 1** | **Visual:** Quick stat: 40% of automated reviews contain self-contradiction (synthetic stat for example). | **On-slide text:** *40% contradict themselves.* | **Speaker says:** "The contradictions cost us — author time, reviewer trust, downstream meta-analyses. This is the gap we set out to close." | **Transition:** "Here's our question."

### Slide 3 — The question
**Time:** 30s | **Beat 2** | **Visual:** Single sentence. | **On-slide text:** *Can self-contradictions in automated review be detected at decode time?* | **Speaker says:** "Specifically: not after the fact, not by a separate verifier — at decode time, while the review is being generated." | **Transition:** "First, what's been tried."

### Slide 4 — What's known
**Time:** 45s | **Beat 3** | **Visual:** Two-cell comparison: prior approaches and their limits. | **On-slide text:** *Re-ranking · Verifier ensembles.* | **Speaker says:** "Two prior threads: re-ranking generated candidates (Smith 2024), and verifier-ensemble post-hoc filtering (Patel 2025). Both work; both cost compute. The question for us was: can we do it earlier and cheaper?" | **Transition:** "Our approach is..."

### Slide 5 — Approach in one sentence
**Time:** 30s | **Beat 4** | **Visual:** Single architectural diagram. | **On-slide text:** *Self-contradiction logits, decoded inline.* | **Speaker says:** "A single architectural change — a self-contradiction head decoded inline with the main token stream. No verifier, no re-ranking, no extra inference pass." | **Transition:** "Let me show you how it works..."

### Slide 6 — Method
**Time:** 30s | **Beat 5** | **Visual:** Architecture diagram with the new head highlighted. | **On-slide text:** *[architectural sketch, callout on the new head]* | **Speaker says:** "Standard transformer decoder. The change is here *[laser pointer]* — a second head trained on contradiction-labeled data, decoded jointly. Crucially: same forward pass." | **Transition:** "And here's how we trained it..."

### Slide 7 — Method (training)
**Time:** 30s | **Beat 5** | **Visual:** Training-data flow diagram. | **On-slide text:** *180K labeled contradictions, contrastive loss.* | **Speaker says:** "Trained on 180K contradiction pairs from the [synthetic dataset] benchmark, using contrastive loss. Skip the loss-derivation details — they're in the paper." | **Transition:** "Now the results..."

### Slide 8 — Headline result
**Time:** 45s | **Beat 6** | **Visual:** Bar chart: contradiction-detection F1 across baselines + ours. | **On-slide text:** *F1 0.87 (prior SOTA 0.79).* | **Speaker says:** "We hit F1 0.87 on the contradiction benchmark. Prior SOTA was 0.79. The 8-point gain is significant but it's not the headline." | **Transition:** "The headline is..."

### Slide 9 — Headline result (cost)
**Time:** 30s | **Beat 6** | **Visual:** Compute comparison chart. | **On-slide text:** *4× less inference compute.* | **Speaker says:** "...we do it with 4× less inference compute than the prior SOTA. Because we don't run a verifier, we don't re-rank, we don't do a second pass. Same forward pass, joint decoding." | **Transition:** "But here's what's interesting."

### Slide 10 — The surprise
**Time:** 45s | **Beat 7** | **Visual:** Ablation table. | **On-slide text:** *95% of the gain from one component.* | **Speaker says:** "When we ablated the architecture, 95% of the gain came from one component: the self-contradiction head's contrastive training objective, not the inline decoding. Inline decoding gives us the speed; the contrastive training gives us the accuracy. This decomposition matters for follow-up work." | **Transition:** "Honestly — what we can't claim."

### Slide 11 — Limitation
**Time:** 30s | **Beat 8** | **Visual:** Single concise limitation statement. | **On-slide text:** *Domain-specific labels: not yet transferred.* | **Speaker says:** "We've shown this on contradiction labels in the academic-review domain. We haven't yet shown transfer to other domains. That's the open question, and it's also the next paper." | **Transition:** "To wrap up..."

### Slide 12 — Take-home + what's next
**Time:** 30s | **Beat 9** | **Visual:** Take-home sentence in large type. | **On-slide text:** *SOTA + 4× cheaper, from one architectural choice.* | **Speaker says:** "Our method outperforms the prior SOTA on the target benchmark while requiring 4× less compute — and the gain comes from a single architectural choice, not from scale. Next: cross-domain transfer. If you work on contradiction-style problems in other domains, find me at the poster session — I'd love to compare notes." | **Transition:** "Thank you — happy to take questions."

### Slide 13 — Acknowledgments + Q&A
**Time:** 15s | **Beat 10** | **Visual:** Collaborators + paper QR code + code link. | **On-slide text:** *github.com/user/paper · paper QR · co-authors* | **Speaker says:** "Thanks to my collaborators *[name them]* and our funders. Code at this link. Happy to take questions." | **Transition:** [end of talk]

## Opening hook (full text)

"Show of hands — who got an automated review last cycle that contradicted itself? *[pause for hands]* That's the problem this paper is about: 40% of automated reviews contain self-contradictions. Cost: author time, reviewer trust, downstream meta-analyses. We asked whether we could detect these contradictions earlier and cheaper. The answer is yes. Here's how."

## Closing

"Our method outperforms the prior SOTA on the target benchmark while requiring 4× less compute — and the gain comes from a single architectural choice, not from scale. Next: cross-domain transfer. Find me at the poster session if you work on contradictions in other domains. Thanks."

## Backup slides (3-5 for likely Q&A)

### B1 — "Did you compare to verifier ensemble X (recent NeurIPS 2025)?"
**Visual:** Comparison table including X. | **Content:** We did; X scores slightly higher F1 (0.88) but at 8× our inference cost. The compute-accuracy tradeoff is in our favor for production.

### B2 — "What about transfer to non-academic domains?"
**Visual:** Honest framing. | **Content:** Not yet — this is the next paper. Preliminary experiments on legal-document contradictions (n=2K) suggest the architecture generalizes; full study in progress.

### B3 — "Is the code available?"
**Visual:** Repo + license. | **Content:** Yes — github.com/user/paper, MIT license. Pretrained checkpoints + training scripts + the 180K-pair labeled dataset.

### B4 — "How sensitive is performance to the contradiction-pair labeling?"
**Visual:** Sensitivity analysis chart. | **Content:** Robust to ~20% label noise (paper's §5.3). Drops sharply above 30% noise. We used annotator agreement κ=0.78 in the source data.

### B5 — "What about the contrastive loss formulation specifically — why InfoNCE vs alternatives?"
**Visual:** Loss ablation. | **Content:** We tested InfoNCE, NT-Xent, and a hinge variant. InfoNCE wins by 1.5 F1 points and is faster to train. Details in §3.4.

## Rehearsal plan

1. **Pass 1 — solo, full-length, timer.** Confirm hitting 7-min mark; cut if over.
2. **Pass 2 — solo, recorded.** Watch for pacing, filler words ("um", "kind of"), trailing off.
3. **Pass 3 — to one friendly colleague.** Watch their face during the method slides — confusion = need to simplify.
4. **Pass 4 — to a hostile / skeptical colleague.** Have them ask B1-B5 from the backup deck.
5. **Pass 5 — final timing pass, the day before.** No content changes after this.

## Delivery notes

- **Pace:** Aim for 130 wpm. Slow down at the take-home (slide 12).
- **Pause** 1-2 sec after each slide transition. Reads as confidence.
- **Eye contact** with the room, not the laptop. Glance at slides for visual confirmation only.
- **Section room of ~30:** more conversational than plenary. OK to make eye contact with specific people.
- **Q&A:** repeat each question back for the audience. If you don't know an answer, "Good question — that's exactly what we're working on next" is honest and forward-looking.

## Acknowledgments

Co-authors: [names]. Funders: [agencies]. Reviewers of prior drafts: [names if applicable].

## Open / paper / code links

- Paper: [DOI when available]
- Code: github.com/[user]/[paper-repo]
- Data: OSF DOI [when minted]
- Slides: will post to repo after talk
