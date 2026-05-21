# Project Euler 23 — Non-Abundant Sums

## Problem Statement

Find the sum of all positive integers that cannot be written as the sum of two abundant numbers.

---

# What is an Abundant Number?

A number is called abundant if:

```text
sum of proper divisors > number
```

Example:

```text
12
Proper divisors: 1 + 2 + 3 + 4 + 6 = 16
```

Since:

```text
16 > 12
```

12 is an abundant number.

---

# Approach

The solution works in three main steps:

1. Compute sum of proper divisors for all numbers
2. Generate all abundant numbers
3. Mark all numbers that can be written as the sum of two abundant numbers

Finally:
- add all numbers that cannot be formed this way

---

# Sieve-Based Divisor Sum Computation

Instead of calculating divisors separately for every number, a sieve-style approach is used.

For every divisor:
- add it to all of its multiples

This reduces complexity significantly compared to checking divisors individually.

---

# Logic Used

## Step 1
Build divisor sums using sieve processing.

---

## Step 2
Identify abundant numbers:

```text
divisorSum(number) > number
```

---

## Step 3
Try every pair of abundant numbers:

```text
abundant[i] + abundant[j]
```

If the sum is within limit:
- mark it as writable

---

## Step 4
Add numbers that were never marked.

---

# Why Boolean Array is Used

```python
canBeWritten = [False] * (limit + 1)
```

This allows:
- constant time lookup
- efficient marking of reachable sums

---

# Validation

The implementation validates that:
- the limit is positive

Invalid input raises an error.

---

# Code Structure

The implementation is divided into:
- `buildDivisorSums()` → computes divisor sums
- `buildAbundantNumbers()` → generates abundant numbers
- `nonAbundantSum()` → computes final result
- `main()` → handles input and output

This improves readability and maintainability.

---

# Time Complexity

Approximately:

```text
O(n log n + k²)
```

Where:
- `n` = limit
- `k` = number of abundant numbers

---

# Space Complexity

```text
O(n)
```

for divisor sums and boolean storage.

---

# Example Output

```text
4179871
```

This is the Project Euler answer for limit `28123`.