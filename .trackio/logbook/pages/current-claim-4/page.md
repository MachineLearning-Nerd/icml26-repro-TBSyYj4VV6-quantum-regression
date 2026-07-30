# Current verification — Claim 4

**Reviewer verdict: BLOCKED. Confidence: LOW.**

> Exact claim tested: Corollary 25, for `lambda>0` and `epsilon>0`, solves
> Ridge with high probability in `O~(r sqrt(mn)/epsilon+n^3)` quantum time by
> applying Corollary 23 to `[A;sqrt(lambda)I],[b;0]`.

Four routes were completed: exact proof-chain reconstruction; a finite
augmented-system sampling and solve; 20-seed first-hit sweeps at
`m={512,2048,8192}`; and a dedicated scalar counterexample search.

At `lambda=0.5,m=2048,k=256`, the sampled solution’s full-objective ratio was
`1.0002072182`. Leverage sampling first met the spectral criterion at `k=256`
for all sizes; uniform sampling was 0/20 at `k=512`. The augmentation remained
valid in the falsification route, so no counterexample was established.

Download: [contract](../../evidence/claim_4/claim_contract.json),
[routes](../../evidence/claim_4/routes.json),
[checker](../../evidence/claim_4/independent_checker.json),
[control](../../evidence/claim_4/negative_control.json), and
[CPU record](../../evidence/claim_4/runtime_cpu.json). Executable code:
[routes](../../code/remaining_claim_routes.py) and
[checker](../../code/remaining_claim_checker.py).

The fixed command, pinned environment, run, allocation, seeds, and fail-closed
behavior are identical to Claim 2. This finite classical check cannot verify
the inherited quantum leverage-score runtime. Verdict: BLOCKED.
