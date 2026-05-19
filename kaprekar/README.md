# Kaprekar Constant — Approach 

## Problem Statement

The objective of this problem is to implement the Kaprekar routine for an `n`-digit number.

The program should:
- repeatedly apply the Kaprekar operation
- detect whether the sequence reaches:
  - a fixed constant
  - or a repeating cycle
- display the result along with the number of iterations taken

Two different approaches were implemented and compared:
1. Generic implementation using reusable functions
2. Digit-specific implementation using separate functions


# Observation

While working on the implementation, it was observed that not every digit length converges to a single fixed constant.

Possible outcomes are:
- reaching a fixed constant
- entering a repeating cycle

Because of this, cycle detection was added to the implementation instead of assuming that every sequence will converge.

---

# Approach 1 — Generic Implementation

## Idea

In this approach, the same logic is reused for all digit lengths.

The program:
- automatically detects the number of digits
- performs the Kaprekar transformation
- checks whether the sequence reaches:
  - a fixed point
  - or a repeating cycle

---

## Working

The implementation is divided into two main parts:

### 1. Kaprekar Transformation Function

This function:
- sorts digits in ascending order
- sorts digits in descending order
- performs subtraction

---

### 2. Result Detection Function

This function:
- repeatedly applies the transformation
- tracks previously visited numbers
- detects constants or cycles

A `set` is used to store visited values so repeated states can be detected efficiently.

---

## Why `zfill()` Was Used

```python
str(number).zfill(digits)
```

This preserves leading zeros during transformations.

Example:

```text
0999
```

Without zero padding, the Kaprekar operation would produce incorrect results for some cases.

---

## Advantages

### Reusable
The same implementation works for multiple digit lengths.

---

### Less Repetition
The core logic only needs to be written once.

---

### Easier to Maintain
If any logic needs to be changed, it only has to be updated in one place.

---

### Scalable
Additional digit lengths are automatically supported without creating new functions.

---

## Disadvantages

- slightly less straightforward for beginners
- uses a more generalized design

---

# Approach 2 — Digit-Specific Implementation

Implementing separate functions up to 10 digits would mostly increase repetitive code without adding much practical value.

---

## Advantages

### Easy to Understand
Each function handles one specific case, so the flow is simple and explicit.

---

### Beginner Friendly
The logic is easier to trace during debugging.

---

## Disadvantages

### Code Duplication
A lot of logic gets repeated across functions.

---

### Poor Scalability
Supporting more digit lengths requires writing more functions.

---

### Harder Maintenance
Changes have to be made in multiple places.

---

# Time Complexity

For each iteration:

```text
O(d log d)
```

Where:
- `d` = number of digits

because sorting is performed during every transformation.

Overall complexity:

```text
O(k * d log d)
```

Where:
- `k` = number of iterations before convergence or cycle detection

---

# Which Approach is Better?

## Preferred Approach: Generic Implementation

The generic implementation is the better approach overall.

### Reasons

- it avoids repeating the same logic
- easier to maintain and extend
- supports multiple digit lengths automatically
- cleaner and more modular design

The Kaprekar operation itself is identical regardless of digit length, so writing separate functions for every case is unnecessary.

---

# When the Digit-Specific Approach Can Still Be Useful

The second approach can still be useful:
- while teaching basic concepts
- for beginners learning function-based design
- for small constrained problems

because the control flow is more explicit and easier to follow.

---

# Conclusion

Both approaches successfully implement the Kaprekar routine and detect cycles correctly.

However, the generic implementation is more practical because it:
- scales better
- reduces code duplication
- improves maintainability
- provides a cleaner overall design

For these reasons, the generic implementation is the recommended solution.