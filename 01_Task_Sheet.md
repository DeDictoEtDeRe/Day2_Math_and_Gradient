# Day 2 Independent Exit Check — Math & Gradient Descent

**Time limit: 20 minutes. First attempt: no AI, web search, notes or old code.**

## Part A — predict before running

For vectors `a = [3, 4]` and `b = [4, -3]`:

1. Calculate dot product, both norms, and cosine similarity by hand.
2. State whether the vectors are similar, unrelated, or opposite in direction.

## Part B — build

Using NumPy only, create a Python file that implements:

- `dot_product(a, b)`
- `vector_norm(a)`
- `cosine_similarity(a, b)`

Include a test for the zero-vector edge case.

## Part C — gradient descent transfer

Use `linear_data.csv` to fit a one-variable linear regression using gradient descent. Make a loss-vs-iteration plot. Before running, write one sentence predicting what could happen when learning rate changes from `0.05` to `5.0`.

## Show the evaluator

- Your calculations and code/tests.
- The loss plot.
- A two-minute explanation: Why does moving opposite the gradient usually reduce loss?
