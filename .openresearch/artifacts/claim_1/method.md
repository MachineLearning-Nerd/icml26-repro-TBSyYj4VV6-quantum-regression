# Method

The verifier instantiates a source-valid family:

- `n=2`, `m=16`, `r=1`;
- eight copies of each coordinate row;
- `f_i(t)=t^2`, so `sqrt(f_i(t))=|t|` is exactly
  `(L=1, theta=1, c=1)`-proper;
- `s_min=1`, `s_max=2`;
- `epsilon_q=2^-q`.

For each horizon it computes the normalized sample count
`M=n/epsilon^2`, the named primitive’s required input condition `M<=m`,
and the displayed runtime terms. An exponent certificate independently checks
that, for fixed `m,n,r` and `epsilon -> 0`, the explicit loop is
`Omega(epsilon^-2)` while the only epsilon-dependent claimed term is
`O~(epsilon^-1)`. No choice of suppressed polylogarithmic factor closes a
one-power gap.

The negative control sets `epsilon=sqrt(n/m)`. Then `M=m` and, for `r=1`,
`M=sqrt(mn)/epsilon`; the verifier must report no contradiction.

This is a source-contract audit of the exact named algorithm, not a hardware
benchmark and not a claim that every conceivable quantum sparsification
algorithm is impossible.

The supplemental statevector route reconstructs Hamoudi's good/bad circuit
state, executes amplitude-amplification reflections, measures samples, and
compares the empirical distribution with the exact target in four cells up to
`N=2048,K=256`. It then makes the exact target call at three larger
assumption-satisfying witnesses. All have `M=4m` and are rejected by the
cited `K<=N` contract; the `M=m` boundary control constructs successfully.
