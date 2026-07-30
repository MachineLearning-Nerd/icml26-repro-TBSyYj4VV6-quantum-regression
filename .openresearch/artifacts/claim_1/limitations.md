# Limitations and deviations

- The finding contradicts the written `QGLMSparsify` algorithm/runtime
  contract. It is not a lower bound against all possible quantum algorithms.
- `Theta~` constants are normalized to one only for the displayed finite
  sweep. The independent verdict uses the constant-independent asymptotic
  exponent and primitive-domain arguments.
- The paper could repair this route by adding the missing
  `epsilon=Omega(sqrt(n/m))` precondition, branching to a dense exact return
  outside that regime, and stating the associated runtime. That repaired
  theorem is not the quantified statement audited here.
- No quantum hardware is needed to check a violated subroutine precondition or
  an explicit pseudocode operation lower bound.
