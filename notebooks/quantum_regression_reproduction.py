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

    **Evidence first:** two literal paper claims have exact counterexamples;
    four universal quantum-runtime claims remain blocked.

    | Claim | Verdict | Decisive evidence |
    |---|---|---|
    | 1 | **FALSIFIED** | Algorithm 2 uses `M>m` and explicitly loops over `M=O~(epsilon^-2)` |
    | 2 | **BLOCKED** | finite linear ratio 1.000004; no quantum-runtime certificate |
    | 3 | **BLOCKED** | printed display has exact gap `1 - 33/40 = 7/40`; headline firstness/runtime remains unresolved |
    | 4 | **BLOCKED** | finite Ridge ratio 1.000207; inherited runtime unresolved |
    | 5 | **BLOCKED** | finite Huber ratio 1.002026; QMLSO runtime unresolved |
    | 6 | **BLOCKED** | finite ell-0.5 ratio 1.002983; cited solver range starts above p=1 |

    Live score: **0/12**. Conservative forecast: **0–2/12**.
    Best-supported possibility: **2/12**, not a judge result.
    """)
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
    ## Why the other claims stay blocked

    The CPU program faithfully simulates the *target sampling distributions* and
    solves finite regression tasks. It does not execute quantum leverage
    estimation or QMLSO. Finite scaling therefore cannot establish a universal
    asymptotic theorem.

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
