---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- Marp slide deck stub for the example talk.
     Render with: marp talk.md -o talk.pdf  (or .pptx, .html)
     Synthetic example. Replace with your paper's actual content. -->

# Self-Contradiction Detection at Decode Time

*A short title for the talk*

[user] · Hypothetical NLP 2026

<!-- speaker notes: 7-min talk + 5-min Q&A.
     Slow open. Make eye contact before the first sentence. -->

---

# *Every paper. Every conference.*

<!-- speaker: Show of hands — who got an automated review last cycle that contradicted itself?
     [pause for hands]
     Half the room. That's the problem this paper is about. -->

---

# *40% contradict themselves.*

<!-- speaker: The contradictions cost us — author time, reviewer trust, downstream meta-analyses.
     This is the gap we set out to close. -->

---

# *Can self-contradictions be detected at decode time?*

<!-- speaker: Specifically — not after the fact, not by a separate verifier — at decode time,
     while the review is being generated. -->

---

# Prior work

- Re-ranking (Smith 2024)
- Verifier ensembles (Patel 2025)

<!-- speaker: Two prior threads. Both work. Both cost compute.
     The question for us was: can we do it earlier and cheaper? -->

---

# Self-contradiction logits, decoded inline

*[architecture diagram]*

<!-- speaker: A single architectural change — a self-contradiction head decoded inline
     with the main token stream. No verifier, no re-ranking, no extra inference pass. -->

---

# Architecture

*[diagram with new head highlighted]*

<!-- speaker: Standard transformer decoder. The change is here.
     A second head trained on contradiction-labeled data, decoded jointly.
     Crucially: same forward pass. -->

---

# Training

180K labeled contradiction pairs · contrastive loss

<!-- speaker: Trained on 180K pairs from [dataset] using contrastive loss.
     Loss derivation details are in the paper. -->

---

# F1: 0.87 (prior SOTA 0.79)

*[bar chart]*

<!-- speaker: We hit F1 0.87 on the contradiction benchmark.
     Prior SOTA was 0.79. The 8-point gain is significant but it's not the headline. -->

---

# 4× less inference compute

*[compute comparison chart]*

<!-- speaker: We do it with 4× less inference compute than the prior SOTA.
     Because we don't run a verifier, don't re-rank, don't do a second pass.
     Same forward pass, joint decoding. -->

---

# 95% of the gain — one component

*[ablation table]*

<!-- speaker: When we ablated, 95% of the gain came from the self-contradiction head's
     contrastive training objective, not the inline decoding.
     Inline decoding gives us the speed; contrastive training gives us the accuracy.
     This decomposition matters for follow-up work. -->

---

# Limitation

Domain-specific labels: not yet transferred.

<!-- speaker: We've shown this in the academic-review domain.
     We haven't yet shown transfer to other domains.
     That's the open question, and the next paper. -->

---

# SOTA + 4× cheaper, from one architectural choice

*Next: cross-domain transfer. Find me at the poster session.*

<!-- speaker: One sentence — same as the take-home.
     Next paper: cross-domain transfer.
     If you work on contradiction-style problems in other domains, find me at the poster session. -->

---

# Thanks

[co-authors] · [funders] · github.com/user/paper

<!-- speaker: Thanks to my collaborators and funders.
     Code at the link. Happy to take questions. -->

---

<!--
Backup slides start here — navigate to them in Q&A if needed.
Marp will treat these as additional pages; they're after the official end.
-->

# B1: Comparison to verifier ensemble X

*[comparison table with X included]*

<!-- speaker: We did compare. X scores slightly higher F1 (0.88) at 8× our inference cost.
     Compute-accuracy tradeoff is in our favor for production. -->

---

# B2: Transfer to non-academic domains?

Not yet — preliminary legal-document results suggest generalization.

---

# B3: Code available?

github.com/user/paper · MIT · pretrained checkpoints · 180K pairs

---

# B4: Sensitivity to label noise?

Robust to ~20% noise. Drops sharply above 30%. Annotator κ=0.78.

---

# B5: Why InfoNCE specifically?

Tested InfoNCE, NT-Xent, hinge. InfoNCE wins by 1.5 F1 + faster training. §3.4.
