"""User interface layer: text menus that connect the user to the algorithm modules.

Course concepts: functions (Unit 2), dictionary used as a menu dispatch table (Unit 5),
if/while control flow (Unit 3). Menus only read input, call a module function and
print the result. All calculations live in the algorithm modules.
"""
from toolkit import basic_algorithms as basic
from toolkit import factoring as fac
from toolkit import array_tools as arr
from toolkit import efficiency as eff
from toolkit.validation import read_int, read_int_list, read_text
from toolkit.logger import log_event


# ---------- Module 1: Number Basics ----------
def do_swap():
    a = read_int("  First number : ")
    b = read_int("  Second number: ")
    print("  Before swap:", (a, b), "-> After swap:", basic.swap_values(a, b))


def do_digits():
    n = read_int("  Enter an integer: ")
    print(f"  Digits: {basic.count_digits(n)}, sum of digits: {basic.sum_of_digits(n)}")


def do_factorial():
    n = read_int("  Enter n (0-500): ", 0, 500)
    print(f"  {n}! = {basic.factorial(n)}")


def do_fibonacci_series():
    n = read_int("  How many terms (1-90)? ", 1, 90)
    print("  ", basic.fibonacci_series(n))


def do_reverse():
    n = read_int("  Enter an integer: ")
    r = basic.reverse_number(n)
    print(f"  Reverse: {r}. Palindrome: {'Yes' if basic.is_palindrome(n) else 'No'}")


def do_to_base():
    n = read_int("  Decimal number: ")
    b = read_int("  Target base (2-16): ", 2, 16)
    print(f"  {n} in base {b} = {basic.to_base(n, b)}")


def do_from_base():
    b = read_int("  Source base (2-16): ", 2, 16)
    text = read_text("  Number in that base: ")
    print(f"  {text} (base {b}) = {basic.from_base(text, b)} in decimal")


def do_char_codes():
    text = read_text("  Enter text: ")
    for character, code in basic.char_to_number(text):
        print(f"   '{character}' -> {code}")


BASIC_MENU = {
    "1": ("Swap two values", do_swap),
    "2": ("Count digits and sum of digits", do_digits),
    "3": ("Factorial", do_factorial),
    "4": ("Fibonacci series", do_fibonacci_series),
    "5": ("Reverse a number / palindrome check", do_reverse),
    "6": ("Decimal to another base", do_to_base),
    "7": ("Another base to decimal", do_from_base),
    "8": ("Character to number codes", do_char_codes),
}


# ---------- Module 2: Factoring & Number Theory ----------
def do_sqrt():
    n = read_int("  Enter a non-negative integer: ", 0)
    print(f"  Integer square root of {n} = {fac.integer_sqrt(n)}")


def do_smallest_divisor():
    n = read_int("  Enter a number (>= 2): ", 2)
    print(f"  Smallest divisor of {n} = {fac.smallest_divisor(n)}"
          f" ({n} is {'prime' if fac.is_prime(n) else 'composite'})")


def do_gcd_lcm():
    a = read_int("  First number (>= 1) : ", 1)
    b = read_int("  Second number (>= 1): ", 1)
    print(f"  GCD = {fac.gcd(a, b)}, LCM = {fac.lcm(a, b)}")


def do_primes():
    n = read_int("  Generate primes up to (<= 100000): ", 2, 100000)
    primes = fac.primes_up_to(n)
    print(f"  {len(primes)} primes found.")
    print("  ", primes if len(primes) <= 60 else primes[:60] + ["..."])


def do_prime_factors():
    n = read_int("  Enter a number (>= 2): ", 2)
    factors = fac.prime_factors(n)
    grouped = fac.factor_dictionary(n)
    text = " x ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in grouped.items())
    print(f"  Prime factors: {factors}   ->   {n} = {text}")


def do_random():
    seed = read_int("  Seed (any integer): ")
    count = read_int("  How many numbers (1-50)? ", 1, 50)
    low = read_int("  Lowest value : ")
    high = read_int("  Highest value: ", low)
    print("  ", fac.lcg_random(seed, count, low, high))


def do_power():
    base = read_int("  Base: ")
    exponent = read_int("  Exponent (0-2000): ", 0, 2000)
    value = fac.fast_power(base, exponent)
    text = str(value)
    print(f"  {base}^{exponent} = {text if len(text) <= 80 else text[:40] + '...' + text[-20:]}"
          f"  ({len(text)} digits)")


def do_nth_fibonacci():
    n = read_int("  Position n (0-5000): ", 0, 5000)
    text = str(fac.nth_fibonacci(n))
    print(f"  F({n}) = {text if len(text) <= 80 else text[:40] + '...' + text[-20:]}")


FACTORING_MENU = {
    "1": ("Integer square root", do_sqrt),
    "2": ("Smallest divisor / prime check", do_smallest_divisor),
    "3": ("GCD and LCM", do_gcd_lcm),
    "4": ("Generate primes (sieve)", do_primes),
    "5": ("Prime factors", do_prime_factors),
    "6": ("Pseudo-random numbers", do_random),
    "7": ("Raise a number to a large power", do_power),
    "8": ("nth Fibonacci number", do_nth_fibonacci),
}


# ---------- Module 3: Array & List Analyzer ----------
def do_summary():
    data = read_int_list("  Enter numbers (space/comma separated): ")
    for key, value in arr.summary(data).items():
        print(f"   {key:<9}: {value}")


def do_array_reverse():
    data = read_int_list("  Enter numbers: ")
    print("  Reversed:", arr.reverse_array(data))


def do_count():
    data = read_int_list("  Enter numbers: ")
    target = read_int("  Number to count: ")
    print(f"  {target} appears {arr.count_occurrences(data, target)} time(s)")


def do_remove_duplicates():
    data = read_int_list("  Enter numbers: ")
    ordered = sorted(data)
    print("  Sorted   :", ordered)
    print("  No duplicates:", arr.remove_duplicates_sorted(ordered))


def do_partition():
    data = read_int_list("  Enter numbers: ")
    pivot = read_int("  Pivot value: ")
    less, equal, greater = arr.partition(data, pivot)
    print(f"  Less: {less}  Equal: {equal}  Greater: {greater}")


def do_kth():
    data = read_int_list("  Enter numbers: ")
    k = read_int(f"  k (1-{len(data)}): ", 1, len(data))
    print(f"  Kth smallest element (k = {k}) is {arr.kth_smallest(data, k)}")


def do_frequency():
    data = read_int_list("  Enter numbers: ")
    table = arr.frequency_table(data)
    for value in sorted(table):
        print(f"   {value:>6} : {'#' * table[value]} ({table[value]})")


def do_sets():
    first = read_int_list("  First list : ")
    second = read_int_list("  Second list: ")
    for name, result in arr.set_operations(first, second).items():
        print(f"   {name:<13}: {result}")


ARRAY_MENU = {
    "1": ("Summary statistics", do_summary),
    "2": ("Reverse the list", do_array_reverse),
    "3": ("Count occurrences", do_count),
    "4": ("Remove duplicates (ordered list)", do_remove_duplicates),
    "5": ("Partition around a pivot", do_partition),
    "6": ("Kth smallest element", do_kth),
    "7": ("Frequency table (dictionary)", do_frequency),
    "8": ("Set operations on two lists", do_sets),
}


# ---------- Module 4: Efficiency Lab ----------
def do_lab_divisor():
    n = read_int("  Number to test (>= 2, try 999983): ", 2)
    d1, s1 = eff.smallest_divisor_naive(n)
    d2, s2 = eff.smallest_divisor_improved(n)
    print(eff.format_comparison(f"  Smallest divisor of {n}", "Try every number", s1,
                                "Odd numbers up to sqrt(n)", s2))
    print("  Verification: both methods agree" if d1 == d2 else "  WARNING: methods disagree!")


def do_lab_power():
    base = read_int("  Base: ")
    exponent = read_int("  Exponent (0-5000): ", 0, 5000)
    v1, s1 = eff.power_naive(base, exponent)
    v2, s2 = eff.power_fast(base, exponent)
    print(eff.format_comparison(f"  {base}^{exponent}", "Repeated multiplication", s1,
                                "Repeated squaring", s2))
    print("  Verification: both methods agree" if v1 == v2 else "  WARNING: methods disagree!")


def do_lab_duplicates():
    data = read_int_list("  Enter numbers: ")
    a1, s1 = eff.has_duplicates_nested(data)
    a2, s2 = eff.has_duplicates_set(data)
    print(eff.format_comparison("  Duplicate check", "Nested loops (comparisons)", s1,
                                "Set (lookups, extra memory)", s2))
    print(f"  Duplicates present: {'Yes' if a1 else 'No'}"
          + ("" if a1 == a2 else "  WARNING: methods disagree!"))


LAB_MENU = {
    "1": ("Smallest divisor: naive vs sqrt method", do_lab_divisor),
    "2": ("Power: multiplication vs squaring", do_lab_power),
    "3": ("Duplicates: nested loops vs set (time trade-off)", do_lab_duplicates),
}


# ---------- Menu engine ----------
def run_submenu(title, menu):
    """Show a submenu repeatedly until the user chooses 0. Errors never crash the app."""
    while True:
        print(f"\n--- {title} ---")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("  0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            return
        if choice not in menu:
            print("  Invalid choice. Please pick a number from the menu.")
            continue
        label, handler = menu[choice]
        try:
            handler()
            log_event("INFO", f"{title} > {label}")
        except ValueError as error:
            print(f"  Error: {error}")
            log_event("WARNING", f"{title} > {label}: {error}")


MAIN_MENU = {
    "1": ("Number Basics (Unit 3)", BASIC_MENU),
    "2": ("Factoring & Number Theory (Unit 4)", FACTORING_MENU),
    "3": ("Array & List Analyzer (Unit 5)", ARRAY_MENU),
    "4": ("Efficiency Lab (Unit 1 analysis)", LAB_MENU),
}


def main_menu():
    """Top-level loop of the program."""
    log_event("INFO", "Program started")
    print("=" * 46)
    print("  MathMate - Problem Solving Toolkit (CSE1021)")
    print("=" * 46)
    while True:
        print("\nMAIN MENU")
        for key, (label, _) in MAIN_MENU.items():
            print(f"  {key}. {label}")
        print("  0. Exit")
        try:
            choice = input("Choose an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            choice = "0"
        if choice == "0":
            print("Goodbye!")
            log_event("INFO", "Program ended")
            return
        if choice in MAIN_MENU:
            title, submenu = MAIN_MENU[choice]
            try:
                run_submenu(title, submenu)
            except (EOFError, KeyboardInterrupt):
                print("\nInput closed. Returning to exit.")
                log_event("INFO", "Program ended (input closed)")
                return
        else:
            print("  Invalid choice. Please pick a number from the menu.")
