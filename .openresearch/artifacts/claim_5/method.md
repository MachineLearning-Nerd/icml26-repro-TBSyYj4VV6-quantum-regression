# Claim 5 method

The current verifier fixes a valid gamma_1/Huber family with
`m=16,n=2,r=1`, follows the source's explicit Theorem 10 application, and
checks that `M=Theta~(n/epsilon^2)` eventually leaves the cited sampler's
domain under the corollary's all-epsilon quantifier. The boundary control is
`epsilon=sqrt(n/m)`.

Preserved historical routes were: reconstruct the proper-loss/QGLMSparsify/solver proof chain;
solve a one-dimensional Huber instance from a sensitivity-sampled coreset;
run 20-seed first-hit sweeps over three `m` values and seven independently
selected horizons with uniform controls; and exhaustively search a scalar grid
for a proper-loss violation.

The finite solver used an 801-point calibration grid and a separate 1401-point
solution grid. It is explicitly not a quantum implementation.

The supplemental route replaces the sampling step with the cited statevector
quantum circuit. It builds exact scalar sensitivity values for 2,048 Huber
observations, measures 256 indices, solves on an independently fixed
801-point grid, and evaluates the chosen point on the full loss.
