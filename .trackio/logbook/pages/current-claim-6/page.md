# Current verification — Claim 6

**Reviewer verdict: BLOCKED. Confidence: LOW.**

> Exact claim tested: for every `p in (0,2]`, Corollary 11 guarantees with
> high probability a `(1+epsilon)` ell-p regression solution in
> `O~(r sqrt(mn)/epsilon + poly(n,1/epsilon))` quantum time.

Four routes were completed: exact source/reference-domain reconstruction;
finite sampled solves at `p=0.5` and `p=1.5`; a 20-seed first-hit sweep; and a
dedicated counterexample search over `p={0.25,0.5,1,1.5,2}`.

The `p=0.5` finite objective ratio was `1.0029825893`. The informed sampler
passed at the first tested horizon. A single-row-support control, which cannot
represent the full loss family, was 0/20 at every horizon. The earlier uniform
control is preserved as a rejected attempt because it passed this easy finite
instance. No subadditivity counterexample was found.

The primary solver reference (arXiv:2311.18145) states its ell-p regression
application for `p in (1,2]`, while this corollary claims `(0,2]`. This is a
proof-chain gap, not a falsification.

Download: [contract](../../evidence/claim_6/claim_contract.json),
[routes](../../evidence/claim_6/routes.json),
[checker](../../evidence/claim_6/independent_checker.json),
[control](../../evidence/claim_6/negative_control.json), and
[CPU record](../../evidence/claim_6/runtime_cpu.json). Executable code:
[routes](../../code/remaining_claim_routes.py) and
[checker](../../code/remaining_claim_checker.py).

The command, environment, accepted run, compute, and seeds are identical to
Claim 2. No quantum runtime certificate or valid counterexample was found.
Verdict: BLOCKED.
