# Claim 4 method

The current verifier uses `m=16,n=2,r=1,lambda=1`, tracks the augmented
sampling length `m+n=18`, and checks the inherited sampler-domain and runtime
power contradictions. The boundary control uses
`epsilon=sqrt(n/(m+n))`.

The preserved historical routes were: source proof-chain reconstruction; a finite augmented
system with exact leverage sampling and Ridge solve; 20-seed first-hit spectral
sweeps at three values of `m` with uniform controls; and a scalar
counterexample search that separately checked the augmentation.

The command and locked environment are identical to Claim 2. The tested
regularization was `lambda=0.5`; this value was not derived from the theorem’s
runtime formula.
