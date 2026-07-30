# Claim 2 method

Four materially different routes were executed:

1. Reconstruct the source proof chain and look for a machine-checkable
   certificate.
2. Compute exact classical leverage scores, sample and reweight rows, construct
   the sparsifier, and solve the finite regression problem.
3. Sweep independently selected horizons `8..512` over 20 seeds and
   `m ∈ {512,2048,8192}`. Record the first horizon reaching 80% success at
   spectral error at most 0.5; compare with uniform sampling.
4. Search source-valid scalar instances for an impossible approximation
   inequality.

The fixed command was
`uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py`.
Python 3.12 and NumPy 2.3.2 are pinned by `uv.lock`.
