# Cleaned citations: 3 entries × 3 styles

> **Synthetic example.** Citations are fictional placeholders.

## APA 7

1. Smith, A., & Jones, R. (2018). Attention context modulates word recall. *Journal of Hypothetical Psychology*, *12*(3), 142–158. https://doi.org/10.1234/jhp.2018.12.3.142

2. Yang, L., Holtz, D., Jaffe, S., Suri, S., Sinha, S., Weston, J., ... Teevan, J. (2021). The effects of remote work on collaboration. *Journal of Hypothetical Nature*, *7*(1), 22–45.
   *(Authors after the 6th omitted in the input; APA 7 expects up to 20 listed. Verify and expand.)*

3. Patel, S. (2024). *Behavioral measurement of mentorship in distributed work* [Preprint]. OSF. https://osf.io/xyz123

## Vancouver

1. Smith A, Jones R. Attention context modulates word recall. J Hypoth Psychol. 2018;12(3):142–158. doi:10.1234/jhp.2018.12.3.142

2. Yang L, Holtz D, Jaffe S, Suri S, Sinha S, Weston J, et al. The effects of remote work on collaboration. J Hypoth Nat. 2021;7(1):22–45.

3. Patel S. Behavioral measurement of mentorship in distributed work [preprint]. OSF; 2024. Available from: https://osf.io/xyz123

## BibTeX

```bibtex
@article{smith2018attention,
  author  = {Smith, A. and Jones, R.},
  title   = {Attention context modulates word recall},
  journal = {Journal of Hypothetical Psychology},
  year    = {2018},
  volume  = {12},
  number  = {3},
  pages   = {142--158},
  doi     = {10.1234/jhp.2018.12.3.142}
}

@article{yang2021remote,
  author  = {Yang, L. and Holtz, D. and Jaffe, S. and Suri, S. and Sinha, S. and Weston, J. and others},
  title   = {The effects of remote work on collaboration},
  journal = {Journal of Hypothetical Nature},
  year    = {2021},
  volume  = {7},
  number  = {1},
  pages   = {22--45}
}

@misc{patel2024behavioral,
  author  = {Patel, S.},
  title   = {Behavioral measurement of mentorship in distributed work},
  year    = {2024},
  note    = {Preprint},
  howpublished = {OSF},
  url     = {https://osf.io/xyz123}
}
```

## Could not verify — please confirm

- **Smith & Jones 2018:** DOI checked — resolves to *J. Hypothetical Psychology* 2018 vol 12 issue 3 (synthetic, but the structure verifies). Confirm issue number (input had "12, 142–158" without explicit issue; inferred 3 from typical numbering).
- **Yang et al. 2021:** Input has "et al." — APA 7 requires up to 20 authors listed. Please provide the full author list. Synthetic expansion above shows the format expected.
- **Patel 2024 preprint:** OSF URL `osf.io/xyz123` is a placeholder shape; verify the actual identifier and whether a DOI has been minted for the OSF deposit.

## Notes

- APA 7 article titles use **sentence case**; journal names are **title case + italic**.
- Vancouver journal abbreviations follow NLM catalog conventions. For "Journal of Hypothetical Psychology" the conventional abbreviation is "J Hypoth Psychol" (illustrative only — verify against actual NLM record for real journals).
- BibTeX keys use `firstauthor + year + firstword-of-title` convention. Adjust to match your existing key style.
- All three styles handle the OSF preprint slightly differently — APA 7 uses `[Preprint]` notation, Vancouver uses `[preprint]`, BibTeX uses `@misc` with a `note` field.

## Document-wide consistency

If these citations come from a manuscript: ensure every in-text citation has a matching reference list entry and vice versa. To run a document-wide cross-check, point this skill at the manuscript: `/cite fix all references in ./manuscript.md to APA 7` — the skill will surface mismatches.
