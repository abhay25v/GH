# Amicable Numbers — Approach Documentation

## Problem Statement

Find the sum of all amicable numbers below a given limit.

---

# Approach

The solution first precomputes the sum of proper divisors for every number below the limit.

Then for each number:
1. Find its divisor sum
2. Check whether the reverse relation also holds
3. Ensure the numbers are different

If all conditions are satisfied:
- the number is amicable

---

# Logic Used

A sieve-style approach is used to efficiently calculate divisor sums.

For every divisor:
- add it to all of its multiples

This avoids recalculating divisors repeatedly.

---

# Validation

The program validates that:
- the limit is positive

Invalid inputs raise an error message.

---

# Code Structure

The implementation is divided into:
- `build_divisor_sums()` - precomputes divisor sums
- `is_amicable()` - checks amicable condition
- `sum_amicable_numbers()` - calculates final answer
- `main()` - handles input and output

This improves readability and maintainability.

---

# Time Complexity

```text
O(n log n)
```

due to divisor preprocessing.

---

# Space Complexity

```text
O(n)
```

for storing divisor sums.

