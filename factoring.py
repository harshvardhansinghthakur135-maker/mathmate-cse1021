"""Module 2 - Factoring & Number Theory.

Course concepts (Unit 4 - Factoring Methods): finding square root, smallest divisor,
GCD, generating prime numbers, computing prime factors, generating pseudo-random
numbers, raising a number to a large power, computing nth Fibonacci number.
"""


def integer_sqrt(n):
    """Integer square root (floor) using Newton's iterative method."""
    if n < 0:
        raise ValueError("Square root of a negative number is not supported.")
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def smallest_divisor(n):
    """Smallest divisor > 1 of n. Only checks up to sqrt(n)."""
    if n < 2:
        raise ValueError("Number must be at least 2.")
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


def gcd(a, b):
    """Greatest common divisor by Euclid's algorithm."""
    if a < 0 or b < 0:
        raise ValueError("GCD needs non-negative numbers.")
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least common multiple, computed from the GCD."""
    if a <= 0 or b <= 0:
        raise ValueError("LCM needs positive numbers.")
    return a * b // gcd(a, b)


def is_prime(n):
    """True if n is prime."""
    return n >= 2 and smallest_divisor(n) == n


def primes_up_to(limit):
    """All primes <= limit using the Sieve of Eratosthenes (list of booleans)."""
    if limit < 2:
        return []
    is_marked_prime = [True] * (limit + 1)
    is_marked_prime[0] = False
    is_marked_prime[1] = False
    i = 2
    while i * i <= limit:
        if is_marked_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_marked_prime[multiple] = False
        i += 1
    return [number for number in range(2, limit + 1) if is_marked_prime[number]]


def prime_factors(n):
    """List of prime factors of n, smallest first (e.g. 12 -> [2, 2, 3])."""
    if n < 2:
        raise ValueError("Number must be at least 2.")
    factors = []
    while n > 1:
        divisor = smallest_divisor(n)
        factors.append(divisor)
        n //= divisor
    return factors


def factor_dictionary(n):
    """Prime factorisation as a dictionary {prime: exponent}."""
    counts = {}
    for prime in prime_factors(n):
        counts[prime] = counts.get(prime, 0) + 1
    return counts


def lcg_random(seed, count, low, high):
    """Pseudo-random numbers in [low, high] from a Linear Congruential Generator."""
    if count < 1:
        raise ValueError("Count must be at least 1.")
    if low > high:
        raise ValueError("Low limit cannot be greater than high limit.")
    a, c, m = 1103515245, 12345, 2 ** 31
    x = seed % m
    numbers = []
    for _ in range(count):
        x = (a * x + c) % m
        numbers.append(low + x % (high - low + 1))
    return numbers


def fast_power(base, exponent):
    """base ** exponent by repeated squaring (about log2(exponent) steps)."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def nth_fibonacci(n):
    """nth Fibonacci number (F0 = 0, F1 = 1) using two variables."""
    if n < 0:
        raise ValueError("Position cannot be negative.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
