# Project Euler 34 — Digit Factorials

## Problem Statement

Find the sum of all numbers which are equal to the sum of the factorials of their digits.

Example:

```text
145 = 1! + 4! + 5!
```

So `145` is a curious number.

---

# Approach

The solution first precomputes factorials for digits `0` to `9`.

Then for every number in the valid search range:
1. extract each digit
2. calculate the sum of factorials of its digits
3. compare the sum with the original number

If both are equal:
- the number is considered a curious number

---

# Why Precompute Factorials?

Digit factorials are repeatedly used during computation.

Instead of recalculating:

```text
5! = 120
```

multiple times, factorial values are stored once in a list.

This reduces repeated computations and improves efficiency.

---

# Upper Limit Logic

The search range is limited using:

```text
7 × 9! = 2540160
```

Reason:
- the largest possible digit factorial sum for a 7-digit number is `7 × 9!`
- beyond this point, numbers become larger than the maximum factorial digit sum possible

So checking numbers above this limit is unnecessary.

---

# Validation

The implementation validates that:
- numbers processed are non-negative

Invalid values raise an error.

---

# Code Structure

The implementation is divided into:
- `buildDigitFactorials()` → precomputes digit factorials
- `isCuriousNumber()` → checks curious number condition
- `findCuriousNumbersSum()` → computes final answer
- `main()` → handles execution and output

This improves readability and maintainability.

---

# Time Complexity

```text
O(n × d)
```

Where:
- `n` = numbers checked
- `d` = number of digits per number

---

# Space Complexity

```text
O(1)
```

Only constant extra memory is used.

---

# Example Output

```text
Sum of all curious numbers: 40730
```