"""Module 4 - Efficiency Lab.

Course concepts (Unit 1 - Efficiency of Algorithms, Analysis of Algorithms;
Unit 5 - Time Trade-off). Each task is solved by a simple method and an improved
method. Both count their basic steps, so the difference is visible and does not
depend on the speed of the computer. Both methods must give the same answer
(program verification).
"""


def smallest_divisor_naive(n):
    """Try 2, 3, 4, ... up to n. Returns (divisor, steps)."""
    if n < 2:
        raise ValueError("Number must be at least 2.")
    steps = 0
    i = 2
    while i <= n:
        steps += 1
        if n % i == 0:
            return i, steps
        i += 1
    return n, steps


def smallest_divisor_improved(n):
    """Try 2, then odd numbers up to sqrt(n). Returns (divisor, steps)."""
    if n < 2:
        raise ValueError("Number must be at least 2.")
    steps = 1
    if n % 2 == 0:
        return 2, steps
    i = 3
    while i * i <= n:
        steps += 1
        if n % i == 0:
            return i, steps
        i += 2
    return n, steps


def power_naive(base, exponent):
    """Multiply base by itself `exponent` times. Returns (value, multiplications)."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    result = 1
    steps = 0
    for _ in range(exponent):
        result *= base
        steps += 1
    return result, steps


def power_fast(base, exponent):
    """Repeated squaring. Returns (value, multiplications)."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    result = 1
    steps = 0
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
            steps += 1
        base *= base
        steps += 1
        exponent //= 2
    return result, steps


def has_duplicates_nested(numbers):
    """Compare every pair (no extra memory). Returns (answer, comparisons)."""
    comparisons = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            comparisons += 1
            if numbers[i] == numbers[j]:
                return True, comparisons
    return False, comparisons


def has_duplicates_set(numbers):
    """Remember seen values in a set (extra memory, fewer steps). Returns (answer, lookups)."""
    seen = set()
    lookups = 0
    for value in numbers:
        lookups += 1
        if value in seen:
            return True, lookups
        seen.add(value)
    return False, lookups


def format_comparison(title, simple_label, simple_steps, improved_label, improved_steps):
    """Build a small text table comparing the step counts of two methods."""
    lines = [title,
             f"  {'Method':<28}{'Steps':>12}",
             f"  {simple_label:<28}{simple_steps:>12}",
             f"  {improved_label:<28}{improved_steps:>12}"]
    if improved_steps > 0:
        lines.append(f"  Improved method used {simple_steps / improved_steps:.1f}x fewer steps.")
    return "\n".join(lines)
