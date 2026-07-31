# Claim 2 — Linear regression

**Verdict: BLOCKED. Confidence: LOW.**

> The quantum linear-regression algorithm runs in
> `O~(r*sqrt(mn)/epsilon+n^3)` time versus `O~(mr+n^3)` classically
> (Corollary 23).

The exact contract includes query access to `A,b`, `r<=n`, every
`epsilon>0`, a high-probability `(1+epsilon)` solution, and the displayed
runtime. Four distinct routes were completed:

1. proof-chain reconstruction;
2. a finite exact-leverage sampling and solve;
3. formula-independent first-hit sweeps over horizons, three `m` values, and
   seeds `0..19`;
4. an assumption-satisfying scalar falsification search.

At `m=2048,n=8,k=256`, the objective ratio was `1.0000041750`. The first
80%-success horizon was `k=256` at all three tested `m` values; uniform
sampling was `0/20` at `k=512`. These are scoped classical corroborations,
not measurements of the quantum leverage estimator. No proof certificate or
valid counterexample was found.

Evidence: [contract](../../evidence/claim_2/claim_contract.json),
[four routes](../../evidence/claim_2/routes.json),
[independent checker](../../evidence/claim_2/independent_checker.json),
[negative control](../../evidence/claim_2/negative_control.json),
[CPU record](../../evidence/claim_2/runtime_cpu.json), and
[route code](../../code/remaining_claim_routes.py).

Accepted compute: [HF cpu-upgrade job](https://huggingface.co/jobs/DineshAI/6a6b8c7fb36a6516e96a2fed),
estimated 8 cores, actual allocation 64 CPUs, 6.951 seconds scientific
runtime. The claim remains BLOCKED because a finite classical run cannot
verify a universal quantum complexity theorem.
