# Human-in-the-loop record


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_hitl_2026_07_31", "created_at": "2026-07-31T10:10:00+00:00", "title": "Human-in-the-loop record"}
-->
This page documents where the autonomous agent loop was **wrong or
incomplete on its own**, and what the human operator changed. Each entry names
the intervention, the agent state before it, and the artifact that exists only
because of it. The claim verdicts themselves were produced by the agent; the
interventions below changed *what was investigated* and *what counted as a
valid conclusion*.

## Intervention 1 — "some claims depend on CPU; we can't just falsify those"

**Agent state before.** The agent had a working falsification pipeline and was
treating every unexecuted component as fair game for a negative result. Its
own earlier framing described all six claims as falsified "at their exact
stated scope" without distinguishing *why* each part was unverifiable.

**Human intervention.** The operator objected that some components are
unverifiable *because no classical CPU can execute them*, not because they are
wrong, and that a CPU-only experiment therefore cannot license a falsification
of those parts.

**What changed.** This produced the evidence taxonomy now used throughout the
logbook — MATH / CPU-EXEC / **QUANTUM-DEP** / LITERATURE — and the explicit
rule that a QUANTUM-DEP component (Hamoudi's `Theta(sqrt(KN))` sampler,
Apers-Gribling leverage estimation, Li et al. sum estimation) is
**not CPU-falsifiable**: it is a peer-reviewed cited theorem whose *output law*
we can test on CPU but whose *runtime* we cannot. Every falsification in this
logbook is now scoped to classical logic — an unrestricted quantifier, a
priority word, a display typo, an uncited solver — and never to quantum content.
Without this correction the logbook would have implied CPU evidence against
quantum runtimes, which would have been unsound.

## Intervention 2 — "give the alternative claim that IS provable"

**Agent state before.** Six falsified claims and nothing else. A correct but
purely negative result.

**Human intervention.** The operator asked for, in effect, the constructive
dual: for each falsified claim, the nearest claim that is true and useful,
stated precisely enough to be proven.

**What changed.** The entire [repaired-claims appendix](#/repaired-claims):
R1-R6, each with a formal statement, a proof, and the exact defect it removes.
This is where the finding "the paper's core contribution survives; only four
words fail" comes from — a conclusion the negative-only pipeline never would
have reached.

## Intervention 3 — "prove they are correct; use the web and mathematics"

**Agent state before.** The repaired claims existed as prose assertions.

**Human intervention.** The operator required that the alternatives be *proven*
rather than asserted, with the cited literature checked directly.

**What changed.** Two artifacts: the exact-arithmetic
[proof checker](../../code/repaired_claims_checker.py) (9/9 lemmas, rational
arithmetic, no floats in the algebraic claims), and a primary-source audit of
every cited theorem against its actual source. The audit changed a conclusion:
the 2023 pathwise-Lasso paper turned out to carry an *observations*-speedup
variant, not only a feature-count speedup — which is why R3 drops the priority
claim entirely instead of merely narrowing its scope. An agent working from
the target paper's own summary of related work would have narrowed the scope
and been wrong.

## Intervention 4 — publication governance

**Agent state before.** The agent was prepared to keep publishing revisions.

**Human intervention.** The operator halted publication mid-session ("don't
publish"), then re-authorized it deliberately.

**What changed.** A publication discipline that the concurrent-edit history
proves was necessary: every subsequent commit went out under an
expected-parent-SHA guard. That guard caught three concurrent publishes from a
parallel session and forced additive merges instead of overwrites — preserving
another session's statevector evidence rather than clobbering it. The
recorded incidents are in the campaign log: a dropped logbook node re-registered
as an appendix, and a stdout/evidence byte-mismatch caused by a re-run on
different BLAS hardware, both repaired rather than papered over.

## Intervention 5 — "the alternatives need to show what they do"

**Agent state before.** The repaired claims were correct but unreadable — a
wall of statements with no way to see the mechanism.

**Human intervention.** The operator rejected the page as evidence-free and
asked for each alternative to show *why* it was needed and *what* it delivers.

**What changed.** The six figures on the repaired-claims page, each generated
from the executed data rather than drawn by hand: the regime map with
measured-vs-predicted crossings, the min-form crossover with its exact onset,
the corrected-display comparison with the priority timeline, per-seed ridge
ratios, the Huber identity overlay, and the convexity split with its exact
`p = 1/2` chord witness.

## Honest scope of this record

The agent did the reproduction work: reading the source, building the
verifiers, running the executions, drafting the claims, and publishing. What
the human supplied was **epistemic direction** — one methodological correction
that prevented an unsound class of falsification, one demand for a constructive
result, one demand for proof and primary sources, one governance halt, and one
demand for visible evidence. Four of the five changed the scientific content of
this logbook, not merely its presentation.
