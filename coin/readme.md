# Project Euler 78 — Partition Divisibility

## Problem Statement

Find the smallest integer `n` such that the partition number `p(n)` is divisible by one million.

---

# Approach

The solution uses Euler’s recurrence relation for partition numbers along with generalized pentagonal numbers.

The partition values are generated iteratively until a value divisible by one million is found.

---

# Why Normal DP is Not Efficient

A straightforward dynamic programming approach for partition numbers would use:

```text
p(n) = p(n - 1) + p(n - 2) + ...
```
This leads to approximately:

```text
O(n²)
```

So instead of checking all previous states, Euler’s recurrence only uses generalized pentagonal numbers, reducing unnecessary computations.

This improves complexity to approximately:

```text
O(n√n)
```

which is much more efficient.

---

# Logic Used

Partition numbers are calculated using:

```text
p(n) = Σ (-1)^(k+1) * p(n - gk)
```

where:

```text
gk = k(3k ± 1) / 2
```

These are called generalized pentagonal numbers.

The signs follow the pattern:

```text
+ + - - + + - -
```

---

# Optimization

Instead of storing very large partition numbers:
- modulo `1,000,000` is applied during computation

This keeps memory usage and integer size manageable.

---

# Validation

The implementation validates that:
- the divisor is positive

Invalid input raises an error.

---

# Code Structure

The implementation is divided into:
- `find_smallest_partition_divisible()` → contains core partition logic
- `main()` → handles execution and output

This improves readability and maintainability.

---

# Time Complexity

Approximately:

```text
O(n√n)
```

because for each `n`, only generalized pentagonal numbers up to `√n` are processed.

---

# Space Complexity

```text
O(n)
```
for storing partition values.

---
