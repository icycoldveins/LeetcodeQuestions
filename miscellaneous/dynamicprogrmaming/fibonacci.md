### Problem Statement

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is:

```
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

Given a number `n`, write a function to compute the `n`th Fibonacci number. For this example, `Fib(0) = 0`, `Fib(1) = 1`.

### Naive Recursive Solution

A naive approach is to use simple recursion:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

This solution is straightforward but highly inefficient for large `n` due to repeated computations.

### Dynamic Programming Approach

DP solves this inefficiency by storing the results of subproblems, so we don't have to recompute them. There are two main DP approaches: top-down (memoization) and bottom-up (tabulation).

#### 1. Top-Down (Memoization)

We use recursion but store the results of each `fib(n)` we compute in a memoization table (usually an array or dictionary) to avoid redundant calculations.

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

#### 2. Bottom-Up (Tabulation)

We iteratively compute `fib(n)` for all `n` from 0 up to the target number, storing the results in a table (array) as we go along.

```python
def fib_tab(n):
    if n <= 1:
        return n
    fib_table = [0] * (n+1)
    fib_table[1] = 1
    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
    return fib_table[n]
```

### Explanation

- **Memoization** is like climbing a tree and marking where you've been to avoid retracing your steps.
- **Tabulation** is like building a staircase from the bottom up, where each step relies on the previous steps.

Both strategies turn the exponential time complexity of the naive recursive solution into polynomial time complexity, making it much more efficient for large inputs.

### Why Is This DP?

Dynamic programming is at play here because we're solving complex problems by breaking them down into simpler subproblems and remembering the results of those subproblems to avoid redundant work. This is the essence of DP, and the Fibonacci sequence provides a clear and simple illustration of this powerful concept.