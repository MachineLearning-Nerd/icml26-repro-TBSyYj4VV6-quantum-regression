# Claim 1 source audit

Source: arXiv `2509.24757v1`, SHA-256
`bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549`.

The formal statement is Theorem 10 (`thm:quantum-glm-sparsification`,
source lines 537–540), not the simplified table entry. It quantifies over every
`epsilon > 0` and every `s_max > s_min >= 0`; it assumes row sparsity `r <= n`,
query access to `A` and an `(L, theta, c)`-proper loss family, and promises a
classical nonnegative weight vector with high probability. “High probability”
is defined at lines 258–260 as at least `1 - O(1/n)`.

Algorithm 2 (lines 513–532) fixes
`M = Theta~(n/epsilon^2)`, calls `MultiSample(Z, M)`, then executes an explicit
loop from 1 through `M` to construct the returned weights. The paper’s restated
MultiSample theorem (lines 1074–1077) requires `1 <= k <= n`, where that
theorem’s `n` is the length of the sampled vector—`m` in Algorithm 2. The proof
counts the MultiSample cost but omits the explicit `M`-iteration processing
term (lines 1111–1117).

The source later notes for linear regression that a genuinely smaller
sparsifier requires `epsilon = Omega(sqrt(n/m))` (lines 1150–1153). That
restriction makes `M <= m`, but it is absent from Theorem 10 and Algorithm 2’s
formal preconditions. This audit therefore tests the exact written
quantifiers, while the threshold case is retained as a negative control.
