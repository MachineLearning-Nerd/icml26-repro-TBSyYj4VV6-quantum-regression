# Current verification — Claim 2

**Reviewer verdict: BLOCKED. Confidence: LOW.**

> Exact claim tested: Corollary 23 universally guarantees, with high
> probability and for query access to `A,b`, `r≤n`, and every `epsilon>0`, a
> `(1+epsilon)` linear-regression solution in
> `O~(r sqrt(mn)/epsilon + n^3)` time.

## Four verification routes

1. The proof chain was reconstructed as Theorem 19 quantum leverage scores →
   spectral sampling → classical solve. No machine-checkable certificate was
   available.
2. A finite classical simulation computed the exact target leverage
   distribution, constructed a weighted sparsifier, and solved regression.
   At `m=2048,n=8,k=256`, the objective ratio was `1.0000041750`.
3. Formula-independent horizons `8,16,…,512` were swept over seeds `0..19`
   and `m={512,2048,8192}`. The first 80%-success horizon was `k=256` for all
   three. Uniform sampling was 0/20 at `k=512`.
4. An assumption-satisfying scalar search checked 20 cases and found no
   impossible guarantee. This is not a falsification.

The finite simulation directly tests sampling and solving, but does not
execute quantum leverage estimation or measure its runtime. A universal
complexity theorem cannot be verified from finite scaling.

Download: [contract](../../evidence/claim_2/claim_contract.json),
[all four routes](../../evidence/claim_2/routes.json),
[checker](../../evidence/claim_2/independent_checker.json),
[control](../../evidence/claim_2/negative_control.json), and
[CPU record](../../evidence/claim_2/runtime_cpu.json). Code:
[routes](../../code/remaining_claim_routes.py) and
[independent checker](../../code/remaining_claim_checker.py).

## Reproduce

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Accepted run `7d8f2bf0-adb1-4e49-940f-df81da9cf5a5`, commit `e15aace`,
HF `cpu-upgrade`, estimated 8 cores, actual allocation 64 CPUs, 6.951 seconds
scientific runtime (21-second job), NumPy 2.3.2, seeds `0..19`. The checker
exits nonzero if a route, control, scope, or verdict is missing.

## Remaining blocker

No executable named quantum subroutine or proof certificate was found; no
valid counterexample was found. The honest verdict is BLOCKED.
