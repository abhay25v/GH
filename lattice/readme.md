# Project Euler 15 — Lattice Paths

## Problem Statement

Find the number of unique paths from the top-left corner to the bottom-right corner of a grid.

Movement is allowed only:
- right
- down

---

# Approach

The solution uses:
- Depth First Search (DFS)
- Memoization (Dynamic Programming)

At every cell:
- move right
- move down

The total paths from a cell are:

```text
paths(row, col) =
paths(row + 1, col) +
paths(row, col + 1)
```

---

# Why Memoization is Needed

Without memoization:
- the same states are recomputed multiple times

This leads to exponential complexity:

```text
O(2^(rows + cols))
```

Using memoization:
- already computed states are stored
- repeated calculations are avoided

This reduces complexity significantly.

---

# Logic Used

Base cases:
- out of bounds → return 0
- destination reached → return 1

For every valid cell:
- recursively compute paths in both directions
- store the result in `memo`

---

# Validation

The implementation validates that:
- rows and columns are positive integers

Invalid input raises an error.

---

# Code Structure

The implementation is divided into:
- `dfs()` → recursive path computation
- `uniquePaths()` → initializes memoization
- `main()` → handles input and output

This improves readability and maintainability.

---

# Time Complexity

```text
O(rows × cols)
```

Each grid cell is computed only once.

---

# Space Complexity

```text
O(rows × cols)
```

for memoization storage and recursion stack.

---

# Example

## Input

```text
20 20
```

## Output

```text
137846528820
```