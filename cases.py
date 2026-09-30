"""Test case definitions for MathMate.

Each case: (id, description, function, args, expected)
  * expected is a value          -> result must equal it
  * expected is an Exception class -> function must raise it
  * expected is Contains("text") -> result (a string) must contain the text
"""
import os
import subprocess
import sys

from toolkit import basic_algorithms as b
from toolkit import factoring as f
from toolkit import array_tools as a
from toolkit import efficiency as e
from toolkit import validation as v

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Contains:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"output containing '{self.text}'"


def run_app(user_input):
    """Run main.py with the given keyboard input and return everything it printed."""
    done = subprocess.run([sys.executable, "main.py"], input=user_input, text=True,
                          capture_output=True, cwd=ROOT, timeout=20)
    return done.stdout


def verify_naive_equals_improved():
    """Program verification: both smallest-divisor methods agree for 2..500."""
    return all(e.smallest_divisor_naive(n)[0] == e.smallest_divisor_improved(n)[0]
               for n in range(2, 501))


def verify_power_methods():
    """Both power methods agree for several bases and exponents."""
    return all(e.power_naive(x, y)[0] == e.power_fast(x, y)[0]
               for x in (-3, 0, 2, 7) for y in (0, 1, 5, 20))


def verify_sqrt_range():
    """integer_sqrt(n) satisfies r*r <= n < (r+1)*(r+1) for n = 0..2000."""
    return all(f.integer_sqrt(n) ** 2 <= n < (f.integer_sqrt(n) + 1) ** 2
               for n in range(2001))


def verify_prime_factor_product():
    """Multiplying the prime factors gives back the original number (2..1000)."""
    for n in range(2, 1001):
        product = 1
        for p in f.prime_factors(n):
            product *= p
        if product != n:
            return False
    return True


CASES = [
    # ---- Module 1: Number Basics ----
    ("T01", "Swap two values", b.swap_values, (3, 9), (9, 3)),
    ("T02", "Count digits of 12345", b.count_digits, (12345,), 5),
    ("T03", "Count digits of 0 (edge case)", b.count_digits, (0,), 1),
    ("T04", "Sum of digits of 9875", b.sum_of_digits, (9875,), 29),
    ("T05", "Factorial of 5", b.factorial, (5,), 120),
    ("T06", "Factorial of 0 (edge case)", b.factorial, (0,), 1),
    ("T07", "Factorial of negative number", b.factorial, (-3,), ValueError),
    ("T08", "First 8 Fibonacci terms", b.fibonacci_series, (8,), [0, 1, 1, 2, 3, 5, 8, 13]),
    ("T09", "Reverse 1230 (trailing zero dropped)", b.reverse_number, (1230,), 321),
    ("T10", "Palindrome check 12321", b.is_palindrome, (12321,), True),
    ("T11", "Palindrome check 123", b.is_palindrome, (123,), False),
    ("T12", "255 to binary", b.to_base, (255, 2), "11111111"),
    ("T13", "255 to hexadecimal", b.to_base, (255, 16), "FF"),
    ("T14", "Binary 1010 to decimal", b.from_base, ("1010", 2), 10),
    ("T15", "Digit '9' invalid in base 2", b.from_base, ("1092", 2), ValueError),
    ("T16", "Base 20 rejected", b.to_base, (10, 20), ValueError),
    ("T17", "Character codes of 'Hi'", b.char_to_number, ("Hi",), [("H", 72), ("i", 105)]),
    # ---- Module 2: Factoring & Number Theory ----
    ("T18", "Integer sqrt of 99", f.integer_sqrt, (99,), 9),
    ("T19", "Integer sqrt of 0 (edge case)", f.integer_sqrt, (0,), 0),
    ("T20", "Integer sqrt of negative", f.integer_sqrt, (-4,), ValueError),
    ("T21", "Smallest divisor of 91", f.smallest_divisor, (91,), 7),
    ("T22", "Smallest divisor of prime 97", f.smallest_divisor, (97,), 97),
    ("T23", "GCD of 48 and 18", f.gcd, (48, 18), 6),
    ("T24", "GCD with zero", f.gcd, (0, 5), 5),
    ("T25", "LCM of 4 and 6", f.lcm, (4, 6), 12),
    ("T26", "Primes up to 30", f.primes_up_to, (30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ("T27", "Primes up to 1 (edge case)", f.primes_up_to, (1,), []),
    ("T28", "Prime factors of 360", f.prime_factors, (360,), [2, 2, 2, 3, 3, 5]),
    ("T29", "Prime factors of 1 rejected", f.prime_factors, (1,), ValueError),
    ("T30", "Factor dictionary of 360", f.factor_dictionary, (360,), {2: 3, 3: 2, 5: 1}),
    ("T31", "LCG gives 5 numbers inside 1..6", lambda: all(1 <= x <= 6 for x in f.lcg_random(7, 5, 1, 6)) and len(f.lcg_random(7, 5, 1, 6)) == 5, (), True),
    ("T32", "LCG is repeatable for same seed", lambda: f.lcg_random(42, 10, 0, 99) == f.lcg_random(42, 10, 0, 99), (), True),
    ("T33", "LCG low > high rejected", f.lcg_random, (1, 3, 9, 2), ValueError),
    ("T34", "2 to the power 100", f.fast_power, (2, 100), 1267650600228229401496703205376),
    ("T35", "Power with negative exponent", f.fast_power, (2, -1), ValueError),
    ("T36", "10th Fibonacci number", f.nth_fibonacci, (10,), 55),
    # ---- Module 3: Array & List Analyzer ----
    ("T37", "Reverse [1,2,3,4]", a.reverse_array, ([1, 2, 3, 4],), [4, 3, 2, 1]),
    ("T38", "Reverse empty list (edge case)", a.reverse_array, ([],), []),
    ("T39", "Count occurrences of 2", a.count_occurrences, ([2, 5, 2, 2], 2), 3),
    ("T40", "Maximum of [4,-1,9,3]", a.find_max, ([4, -1, 9, 3],), 9),
    ("T41", "Maximum of empty list", a.find_max, ([],), ValueError),
    ("T42", "Remove duplicates from sorted list", a.remove_duplicates_sorted, ([1, 1, 2, 3, 3, 3],), [1, 2, 3]),
    ("T43", "Unsorted list rejected", a.remove_duplicates_sorted, ([3, 1, 2],), ValueError),
    ("T44", "Partition around 5", a.partition, ([7, 2, 5, 9, 5, 1], 5), ([2, 1], [5, 5], [7, 9])),
    ("T45", "3rd smallest of [9,4,7,1,8]", a.kth_smallest, ([9, 4, 7, 1, 8], 3), 7),
    ("T46", "k larger than list size", a.kth_smallest, ([1, 2], 5), ValueError),
    ("T47", "k = 0 rejected", a.kth_smallest, ([1, 2], 0), ValueError),
    ("T48", "Frequency table", a.frequency_table, ([1, 2, 1, 3, 1],), {1: 3, 2: 1, 3: 1}),
    ("T49", "Set operations", a.set_operations, ([1, 2, 3], [2, 3, 4]), {"union": [1, 2, 3, 4], "intersection": [2, 3], "difference": [1]}),
    ("T50", "Summary of [2,4,6]", a.summary, ([2, 4, 6],), {"count": 3, "sum": 12, "mean": 4.0, "maximum": 6, "minimum": 2, "distinct": 3}),
    # ---- Module 4: Efficiency Lab ----
    ("T51", "Naive vs improved divisor agree (2..500)", verify_naive_equals_improved, (), True),
    ("T52", "Improved divisor uses fewer steps for 999983", lambda: e.smallest_divisor_improved(999983)[1] < e.smallest_divisor_naive(999983)[1], (), True),
    ("T53", "Both power methods agree", verify_power_methods, (), True),
    ("T54", "Fast power steps for exponent 1000", e.power_fast, (2, 1000), (2 ** 1000, 16)),
    ("T55", "Nested duplicate check, no duplicates", e.has_duplicates_nested, ([1, 2, 3, 4],), (False, 6)),
    ("T56", "Set duplicate check finds duplicate", e.has_duplicates_set, ([1, 2, 1, 4],), (True, 3)),
    # ---- Validation ----
    ("T57", "Parse '4, 7 2'", v.parse_int_list, ("4, 7 2",), [4, 7, 2]),
    ("T58", "Parse empty text", v.parse_int_list, ("   ",), ValueError),
    ("T59", "Parse text with a letter", v.parse_int_list, ("1 x 3",), ValueError),
    # ---- Verification (properties) ----
    ("T60", "integer_sqrt property for 0..2000", verify_sqrt_range, (), True),
    ("T61", "Product of prime factors equals n (2..1000)", verify_prime_factor_product, (), True),
    # ---- Integration: whole program through the menu ----
    ("T62", "Menu: factorial of 5 through the UI", run_app, ("1\n3\n5\n0\n0\n",), Contains("5! = 120")),
    ("T63", "Menu: invalid main choice is rejected", run_app, ("9\n0\n",), Contains("Invalid choice")),
    ("T64", "Menu: letters instead of number are re-asked", run_app, ("1\n3\nabc\n4\n0\n0\n",), Contains("please enter a whole number")),
    ("T65", "Menu: out-of-range value is re-asked", run_app, ("1\n3\n999\n3\n0\n0\n",), Contains("at most 500")),
    ("T66", "Menu: bad digit shows error, app continues", run_app, ("1\n7\n2\n1092\n0\n0\n",), Contains("Error:")),
    ("T67", "Menu: prime factors of 360 through the UI", run_app, ("2\n5\n360\n0\n0\n",), Contains("2^3 x 3^2 x 5")),
    ("T68", "Menu: kth smallest through the UI", run_app, ("3\n6\n9 4 7 1 8\n3\n0\n0\n",), Contains("(k = 3) is 7")),
    ("T69", "Menu: efficiency lab shows verification", run_app, ("4\n1\n97\n0\n0\n",), Contains("both methods agree")),
    ("T70", "Menu: closed input ends program cleanly", run_app, ("1\n3\n",), Contains("Input closed")),
]
