# Project Euler 5 — Smallest Multiple

## Problem Statement

Find the smallest positive number that is evenly divisible by all numbers from `1` to `n`.

---

# Approach

The solution uses:
- Greatest Common Divisor (GCD)
- Least Common Multiple (LCM)

The smallest number divisible by all numbers from `1` to `n` is obtained by repeatedly computing the LCM.

---

# Logic Used

LCM of two numbers is calculated using:

```text
LCM(a, b) = (a × b) / GCD(a, b)
```

The algorithm:
1. starts with result = 1
2. computes LCM of current result and next number
3. continues until `n`

This ensures the final result is divisible by every number in the range.

---

# Why GCD is Used

Direct multiplication can create unnecessarily large intermediate values.

Using GCD:
- avoids redundant factors
- makes LCM computation more efficient

The Euclidean Algorithm is used for fast GCD computation.

---

# Validation

The implementation validates that:
- the input is a positive integer

Invalid input raises an error.

---

# Code Structure

The implementation is divided into:
- `gcd()` → computes Greatest Common Divisor
- `lcm()` → computes Least Common Multiple
- `smallestMultiple()` → computes final result
- `main()` → handles input and output

This improves readability and maintainability.

---

# Time Complexity

Approximately:

```text
O(n log n)
```

due to repeated GCD computations.

---

# Space Complexity

```text
O(1)
```

Only constant extra memory is used.

---

# Example

## Input

```text
10
```

## Output

```text
2520
```