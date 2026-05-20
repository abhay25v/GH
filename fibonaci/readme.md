# Even Fibonacci Sum — Approach Documentation

## Problem Statement

Find the sum of all even Fibonacci numbers that do not exceed a given limit.

---

# Approach

The Fibonacci sequence is generated iteratively using two variables.

For each Fibonacci number:
- check if it is even
- if even, add it to the total sum

The process continues until the generated number exceeds the given limit.

---

Steps followed:
1. Generate Fibonacci numbers iteratively
2. Check whether the number is even
3. Add even numbers to the sum
4. Stop when the limit is exceeded

---


# Code Structure

The implementation is divided into:
- `sum_even_fibonacci()` - contains core logic
- `main()` - handles input and output

This improves readability and maintainability.

---

# Time Complexity

```text
O(n)
```

Where:
- `n` is the number of Fibonacci terms generated.

---

# Space Complexity

```text
O(1)
```
---