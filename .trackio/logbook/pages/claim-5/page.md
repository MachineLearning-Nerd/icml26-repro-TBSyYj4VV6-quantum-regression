# Claim 5 — Huber regression

**Verdict: BLOCKED. Confidence: LOW.**

> Huber regression is handled through the `gamma_p` loss framework in
> `O~(r*sqrt(mn)/epsilon+poly(n,1/epsilon))` quantum time
> (Corollary 12).

The source quantifies over `p in (0,2]`; `p=1` specializes to Huber. Four
routes reconstructed the loss/proof chain, solved a finite Huber coreset,
swept formula-independent horizons, and searched for a proper-loss
counterexample.

The finite solution's objective ratio was `1.0020256149`. Informed sampling
first met the criterion at `k=16,8,8` as `m` increased; uniform controls
required `k=256,128,16`. These results verify the specialization and provide
finite corroboration only. They do not execute or certify QGLMSparsify/QMLSO.

Evidence: [contract](../../evidence/claim_5/claim_contract.json),
[four routes](../../evidence/claim_5/routes.json),
[independent checker](../../evidence/claim_5/independent_checker.json),
[negative control](../../evidence/claim_5/negative_control.json), and
[CPU record](../../evidence/claim_5/runtime_cpu.json).

No valid falsification was found, so the universal runtime remains BLOCKED.
