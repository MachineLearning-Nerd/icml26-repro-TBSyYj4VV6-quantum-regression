# Claim 2 evaluation

Verdict: **BLOCKED**. Confidence: **LOW**.

At `m=2048`, the sampled solution had full-data objective ratio
`1.0000041750`. Across all three matrix sizes, leverage sampling first reached
the calibrated spectral criterion at `k=256`; uniform sampling had 0/20
successes even at `k=512`. This directly checks a finite sampling-and-solve
mechanism, not the claimed quantum runtime.

The independent checker confirms exactly four routes, a discriminating
negative control, honest scoping, and no mislabeled falsification. Full credit
remains blocked by the absence of an executable quantum leverage-score
implementation or proof certificate.
