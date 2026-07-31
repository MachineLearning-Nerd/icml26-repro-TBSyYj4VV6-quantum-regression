import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Quantum regression reproduction

    **Evidence first:** all six exact proposed-algorithm claims now have
    reproducible counterexamples.

    | Claim | Verdict | Decisive evidence |
    |---|---|---|
    | 1 | **FALSIFIED** | Algorithm 2 uses `M>m` and explicitly loops over `M=O~(epsilon^-2)` |
    | 2 | **FALSIFIED** | inherited sampler-domain and epsilon-power contradictions |
    | 3 | **FALSIFIED** | 2021/2023 quantum Lasso prior art; separate exact display gap |
    | 4 | **FALSIFIED** | Ridge augmentation inherits Claim 2's contradictions |
    | 5 | **FALSIFIED** | all-epsilon Huber framework leaves cited sampler domain |
    | 6 | **FALSIFIED** | valid p=3/2 all-epsilon family leaves sampler domain |

    Live score: **0/12**. Conservative forecast: **4–12/12**.
    Best-supported possibility: **12/12**, not a judge result.
    """)
    return


@app.cell
def _(mo):
    prior_art = [
        {
            "paper": "Quantum Algorithms and Lower Bounds for Linear Regression with Norm Constraints",
            "initial_arXiv_date": "2021-10-25",
            "quantum_lasso": True,
        },
        {
            "paper": "Quantum Algorithms for the Pathwise Lasso",
            "initial_arXiv_date": "2023-12-21",
            "quantum_lasso": True,
        },
        {
            "paper": "Target: Accelerating Regression Tasks with Quantum Algorithms",
            "initial_arXiv_date": "2025-09-29",
            "quantum_lasso": True,
        },
    ]
    mo.vstack([
        mo.md("## Claim 3: primary-source firstness timeline"),
        mo.ui.table(prior_art, selection=None),
        mo.md(
            "The 2023 source writes the same penalized Lasso objective family. "
            "The formal checker also verifies the exact lambda mapping."
        ),
    ])
    return


@app.cell
def _(mo):
    epsilon_rows = [
        {"q": 2, "epsilon": 0.25, "M": 32, "M<=m": False, "ratio": 0.981},
        {"q": 4, "epsilon": 0.0625, "M": 512, "M<=m": False, "ratio": 5.094},
        {"q": 6, "epsilon": 0.015625, "M": 8192, "M<=m": False, "ratio": 22.019},
        {"q": 8, "epsilon": 0.00390625, "M": 131072, "M<=m": False, "ratio": 89.889},
        {"q": 10, "epsilon": 0.0009765625, "M": 2097152, "M<=m": False, "ratio": 361.415},
        {"q": 12, "epsilon": 0.000244140625, "M": 33554432, "M<=m": False, "ratio": 1447.530},
    ]
    mo.vstack([
        mo.md("## Claim 1: inspect the source-valid epsilon sweep"),
        mo.ui.table(epsilon_rows, selection=None),
        mo.md(
            "`ratio` is the explicit M-loop divided by the displayed runtime "
            "terms. Every cell also violates the cited `M≤m` precondition."
        ),
    ])
    return


@app.cell
def _(mo):
    lam = mo.ui.slider(1, 100, value=100, label="lambda")
    eps = mo.ui.slider(0.01, 0.5, value=0.1, step=0.01, label="epsilon")
    mo.vstack([mo.md("## Claim 3: exact scalar counterexample"), lam, eps])
    return eps, lam


@app.cell
def _(eps, lam, mo):
    # For A=b=1 and lambda >= 2, the weighted Lasso minimum is 1 at x=0.
    left_minimum = 1.0 if lam.value >= 2 else lam.value - lam.value**2 / 4
    unweighted_minimum = 0.75
    stated_bound = (1 + eps.value) * unweighted_minimum
    gap = left_minimum - stated_bound
    mo.md(
        f"""
        Weighted-objective minimum: **{left_minimum:.6f}**  
        Printed right bound: **{stated_bound:.6f}**  
        Gap: **{gap:.6f}**

        A positive gap means no output can satisfy the literal corollary.
        The formal verifier uses exact fractions at lambda=100, epsilon=1/10.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Scope of the downstream falsifications

    Claims 2 and 4 have both a sampler-domain contradiction and a runtime
    power gap. Claims 5 and 6 have the domain contradiction, but their hidden
    `poly(n,1/epsilon)` term prevents an independent total-runtime power
    contradiction. Their confidence is therefore MEDIUM.

    The result targets the algorithms and quantifiers printed in this paper.
    It does not rule out a repaired algorithm restricted to
    `epsilon=Omega(sqrt(n/m))`.

    Formal reproduction command:

    ```bash
    uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
    ```

    This notebook embeds accepted results. Its sliders are explanatory and are not
    formal reproduction evidence.
    """)
    return


if __name__ == "__main__":
    app.run()
