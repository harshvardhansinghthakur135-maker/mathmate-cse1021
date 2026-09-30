"""Module 1 - Number Basics.

Course concepts (Unit 3 - Fundamental Algorithms): exchange the values, counting,
summation, factorial computation, Fibonacci sequence, reverse, base conversion,
character to number conversion. Uses tuple assignment (Unit 2) and while/for loops.
"""

DIGIT_SYMBOLS = "0123456789ABCDEF"


def swap_values(a, b):
    """Exchange two values using tuple assignment."""
    a, b = b, a
    return a, b


def count_digits(n):
    """Counting: number of digits in an integer."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def sum_of_digits(n):
    """Summation: add up the digits of an integer."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def factorial(n):
    """Factorial by iteration. n must be >= 0."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_series(count):
    """Return the first `count` Fibonacci numbers as a list."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


def reverse_number(n):
    """Reverse the digits of an integer (sign is kept)."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return sign * reversed_n


def is_palindrome(n):
    """A number is a palindrome if it equals its own reverse."""
    return n >= 0 and n == reverse_number(n)


def to_base(n, base):
    """Convert a decimal integer to text in the given base (2 to 16)."""
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    digits = ""
    while n > 0:
        digits = DIGIT_SYMBOLS[n % base] + digits
        n //= base
    return "-" + digits if negative else digits


def from_base(text, base):
    """Convert text written in the given base (2 to 16) to a decimal integer."""
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    text = text.strip().upper()
    if text == "":
        raise ValueError("Nothing to convert.")
    negative = text.startswith("-")
    if negative:
        text = text[1:]
    if text == "":
        raise ValueError("Nothing to convert.")
    value = 0
    for symbol in text:
        position = DIGIT_SYMBOLS.find(symbol)
        if position == -1 or position >= base:
            raise ValueError(f"'{symbol}' is not a valid digit in base {base}.")
        value = value * base + position
    return -value if negative else value


def char_to_number(text):
    """Character to number conversion: list of (character, code) tuples."""
    if text == "":
        raise ValueError("Text cannot be empty.")
    return [(character, ord(character)) for character in text]


def number_to_char(code):
    """Convert a character code back to its character."""
    if code < 0 or code > 0x10FFFF:
        raise ValueError("Code is outside the valid character range.")
    return chr(code)
