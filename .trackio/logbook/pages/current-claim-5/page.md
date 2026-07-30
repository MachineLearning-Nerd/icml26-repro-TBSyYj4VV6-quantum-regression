# Current verification — Claim 5

**Reviewer verdict: BLOCKED. Confidence: LOW.**

> Exact claim tested: the piecewise `gamma_p` framework specializes at `p=1`
> to Huber and yields a high-probability `(1+epsilon)` regression solution in
> `O~(r sqrt(mn)/epsilon + poly(n,1/epsilon))` quantum time.

Four routes were completed: loss/proof-chain reconstruction; a finite Huber
coreset and solve; independently calibrated first-hit sweeps; and a
proper-loss counterexample search. The finite solution’s objective ratio was
`1.0020256149`. Informed sampling first met the criterion at `k=16,8,8` for
increasing `m`; uniform controls required `k=256,128,16`. No proper-loss
violation was found.

Download: [contract](../../evidence/claim_5/claim_contract.json),
[routes](../../evidence/claim_5/routes.json),
[checker](../../evidence/claim_5/independent_checker.json),
[control](../../evidence/claim_5/negative_control.json), and
[CPU record](../../evidence/claim_5/runtime_cpu.json). Executable code:
[routes](../../code/remaining_claim_routes.py) and
[checker](../../code/remaining_claim_checker.py).

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Accepted run and compute are identical to Claim 2. Grid sensitivity
computation is classical and cannot establish the named QGLMSparsify/QMLSO
runtime. Verdict: BLOCKED.
