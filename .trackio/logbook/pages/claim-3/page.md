# Claim 3 — Lasso regression

**Verdict: BLOCKED. Confidence: LOW.**

> The paper gives the first quantum algorithm for Lasso regression in
> `O~(r*sqrt(mn)/epsilon + poly(n,1/epsilon))` time, versus
> `O~(mn^2+n^3)` classically (Corollary 26).

The exact corollary specializes the polynomial term to `n^3/epsilon^2` and
quantifies over query access to `A,b`, `r<=n`, `lambda>0`, and
`epsilon>0`, with high-probability output.

The published approximation inequality omits `lambda` from the right-hand
minimand. Exact rational arithmetic gives a valid counterexample to that
literal display: for `A=[1], b=[1], lambda=100, epsilon=1/10`, the smallest
possible left side is `1`, while the printed right bound is `33/40`.
An independent piecewise checker confirms the `7/40` gap; `lambda=1` is the
negative control.

That finding establishes a likely editorial error in the displayed guarantee.
It does **not**, by itself, verify or falsify the broader headline claim that
this is the first quantum Lasso algorithm with the stated runtime. No
machine-checkable proof certificate, prior-art exhaustiveness certificate, or
executable named quantum implementation was available. The headline claim is
therefore BLOCKED.

Evidence: [headline contract](../../evidence/claim_3/claim_contract.json),
[four-route audit](../../evidence/claim_3/routes.json),
[literal-display counterexample](../../evidence/claim_3/counterexample.json),
[independent checker](../../evidence/claim_3/independent_checker.json),
[negative control](../../evidence/claim_3/negative_control.json),
[CPU record](../../evidence/claim_3/runtime_cpu.json), and
[counterexample code](../../code/claim3_lasso_counterexample.py).

The literal typo check is deterministic and runs locally in five seconds on
one CPU process. It is retained as a scoped subfinding, not promoted to
full-credit evidence for the broader claim.
