# Current verification — Claim 1

**Reviewer verdict: FALSIFIED.**

> Exact claim tested: Theorem 10’s proposed `QGLMSparsify` algorithm constructs
> an epsilon-approximate GLM sparsifier for every `epsilon>0` in
> `O~((n^omega+n r^2+r sqrt(mn)/epsilon) log(s_max/s_min))` time.

This page supersedes the historical arithmetic-only verifier. Source:
arXiv `2509.24757v1`, SHA-256
`bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549`;
anchors: Algorithm 2 lines 513–532, Theorem 10 lines 537–540,
`MultiSample` lines 1074–1077, and the runtime proof lines 1111–1117.

## Assumption audit

The counterexample family uses `n=2`, `m=16`, `r=1`, eight copies of each
coordinate row, `f_i(t)=t^2`, `s_min=1`, and `s_max=2`.
Because `sqrt(f_i(t))=|t|`, the loss family is exactly proper with
`(L,theta,c)=(1,1,1)`. Each `epsilon=2^-q` is positive and therefore inside
the formal theorem domain.

## Direct contradiction

Algorithm 2 sets `M=Theta~(n/epsilon^2)`, passes `M` as `k` to
`MultiSample`, and loops over all `M` samples. The paper’s own restatement of
`MultiSample` requires `k<=m`. For every audited cell below, the invocation is
outside that domain. With fixed dimensions the explicit processing lower bound
is `Omega(epsilon^-2)`, but the claimed runtime is only
`O~(epsilon^-1)`.

| q | epsilon | M | M<=m | M / displayed runtime terms |
|---:|---:|---:|:---:|---:|
| 2 | 0.25 | 32 | false | 0.981 |
| 4 | 0.0625 | 512 | false | 5.094 |
| 6 | 0.015625 | 8,192 | false | 22.019 |
| 8 | 0.00390625 | 131,072 | false | 89.889 |
| 10 | 0.0009765625 | 2,097,152 | false | 361.415 |
| 12 | 0.000244140625 | 33,554,432 | false | 1,447.530 |

Independent checker output: `power_gap_confirmed=true`,
`domain_violation_count=11`, `negative_control_rejects_false_positive=true`,
`passed=true`.

Download: [claim contract](../../evidence/claim_1/claim_contract.json),
[raw 11-cell audit](../../evidence/claim_1/runtime_audit.json),
[checker output](../../evidence/claim_1/independent_checker.json), and
[negative control](../../evidence/claim_1/negative_control.json). Executable
sources: [verifier](../../code/claim1_runtime_audit.py) and
[independent checker](../../code/claim1_independent_checker.py).

## Negative control

At the omitted threshold `epsilon=sqrt(n/m)=0.353553…`, normalized `M=m=16`
and `M=r sqrt(mn)/epsilon`. The verifier reports no contradiction. This
control shows the audit is detecting the missing theorem precondition rather
than rejecting the intended non-dense regime unconditionally.

## Reproduce

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Run `193efcb5-712d-4815-8e2e-138765a00292`, commit
`f9d7de4910bf187ca442c00f0c0c725c93313300`, deterministic/no seeds, local
single-process CPU, 5 seconds. The verifier and independent checker exit
nonzero if the contradiction or control evidence changes.

Environment: Python `3.12.*`, [pyproject](../../code/pyproject.toml), and
[exact uv lock](../../code/uv.lock). [CPU record](../../evidence/claim_1/runtime_cpu.json).

## Limit

This falsifies the exact named algorithm/runtime contract, not the existence of
every conceivable quantum sparsification algorithm. Adding the missing
`epsilon=Omega(sqrt(n/m))` restriction or a dense-return branch would be a
different, repaired claim.
