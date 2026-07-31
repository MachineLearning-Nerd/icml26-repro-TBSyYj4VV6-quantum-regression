# Claim 5 source audit

The piecewise `gamma_p` definition is at lines 263–270; Corollary 12 is at
552–554. At `p=1`, the loss equals Huber. Lines 546–547 explicitly obtain the
corollary by applying Theorem 10/QGLMSparsify.

That exact application sets `M=Theta~(n/epsilon^2)` and calls MultiSample,
whose cited theorem requires `M<=m`. Corollary 12 allows every `epsilon>0`
and omits the `epsilon=Omega(sqrt(n/m))` condition that the paper states at
line 329. Thus an assumption-satisfying fixed Huber family eventually leaves
the proposed algorithm's stated subroutine domain.
