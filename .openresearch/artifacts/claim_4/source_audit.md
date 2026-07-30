# Claim 4 source audit

Corollary 25 is at lines 1160–1163 of the pinned source. It reduces Ridge to
linear regression by appending `sqrt(lambda) I` to `A` and zeros to `b`, then
inherits Corollary 23. The exact objective identity is valid, but it does not
independently establish Corollary 23’s quantum leverage-score runtime.
