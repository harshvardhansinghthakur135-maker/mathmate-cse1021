# Viva Preparation

## 1. Project overview
**Q: Explain your project in 30 seconds.**
MathMate is a menu-driven Python program with four modules: Number Basics (Unit 3), Factoring (Unit 4), Array Analyzer (Unit 5) and an Efficiency Lab (Unit 1). A student enters values, gets results, and can compare a simple algorithm with an improved one by counting steps.

## 2. Problem statement
**Q: What problem does it solve?** Beginners practise algorithms in separate programs and never see why one method is better. MathMate puts them in one validated tool with a comparison mode.
**Follow-up: Who is the user?** First-year CSE1021 students and teachers demonstrating efficiency.

## 3. Why this project?
Every feature is a syllabus algorithm, so the project demonstrates the course itself instead of only mentioning it. It is small enough to explain line by line.

## 4. Why this technology?
Python, because the course teaches Python. Standard library only, so nothing needs installing. CLI, because GUI/web frameworks are outside the syllabus.
**Follow-up: Why not a GUI?** It would add code that is unrelated to problem solving and harder to defend.

## 5. Course concepts used
Top-down design, functions and modules, tuple assignment, loops and conditionals, all Unit 3 fundamental algorithms, all Unit 4 factoring methods, Unit 5 array techniques, lists/tuples/sets/dictionaries, efficiency analysis and time trade-off. (See mapping table in `docs/design.md`.)
**Follow-up: Which syllabus items did you NOT use?** `break` and the Scratch/Raptor tools. I used `continue`, `pass`, and return statements instead of `break`.

## 6. Architecture
Four layers: presentation (main.py, menu.py), validation, algorithm modules, support (logger). Algorithm modules never use `input` or `print`, so they can be tested alone.
**Follow-up: Why separate them?** So logic can be tested without a keyboard and the interface can change without touching algorithms.

## 7. Algorithms
- **GCD:** Euclid, `a, b = b, a % b` until b is 0.
- **Smallest divisor:** try 2, then odd numbers up to sqrt(n); a composite number always has a divisor <= sqrt(n).
- **Sieve:** cross out multiples of each prime up to sqrt(limit).
- **Prime factors:** repeatedly divide by the smallest divisor.
- **Fast power:** if exponent is odd multiply result by base; square the base; halve the exponent. About log2(n) steps: 2^1000 needs 16 multiplications instead of 1000 (measured, T54 and sample run).
- **Integer sqrt:** Newton's method with integer division.
- **LCG:** x = (a*x + c) mod m with a = 1103515245, c = 12345, m = 2^31; same seed gives same numbers, so it is pseudo-random.
- **Kth smallest:** remove the minimum k times, O(k*n).
- **Base conversion:** repeated division by the base collecting remainders.
**Follow-up: Complexity of trial division?** O(sqrt n). **Of the sieve?** About O(n log log n). **Of nested duplicate check vs set?** O(n^2) vs O(n) but the set needs extra memory (time trade-off).
**Follow-up: Is LCG secure?** No, it is predictable; fine for demonstration, not for cryptography.

## 8. Data structures
Lists (inputs and results), tuples (returned pairs like `(divisor, steps)`, partition result), sets (union/intersection, duplicate detection), dictionaries (frequency table, prime exponents, menu tables).
**Follow-up: Why a dictionary for menus?** Lookup by key, adding an option is one line, and it avoids a long if/elif chain.

## 9. Database
None. Only a text log file. An ER diagram is required only if storage is used, so it is marked not applicable.

## 10. Security
No accounts or network. Risks are bad input and resource exhaustion: handled by validation and capped ranges. No `eval`.

## 11. Error handling
`read_int` re-asks on wrong type/range. Algorithms raise `ValueError` for invalid maths; `run_submenu` catches it, prints a message and logs a warning. Closed input is caught too.
**Follow-up: What happens for factorial(-3)?** `ValueError` in the function; through the menu the range check stops it earlier.

## 12. Testing
70 test cases: unit, edge cases (0, empty list, k out of range), error cases, property checks over ranges (e.g. integer_sqrt for 0..2000, product of prime factors), and menu integration tests using piped input. Result of the last run: 70 passed.
**Follow-up: Did any test fail?** Yes, the first run had one failure, T54: my expected step count (12) was wrong; the correct count for exponent 1000 is 16 (10 squarings + 6 multiplications). I fixed the test, not the code.

## 13. Design decisions
CLI over GUI, functions over classes, step counting over timing, dictionary menus, a plain test table instead of a test framework (see `docs/design.md` section 5).
**Follow-up: Why count steps instead of time?** Time depends on the computer; step counts show the algorithm's growth.

## 14. Limitations
Integer-only, CLI-only, no persistence; trial division is slow for huge numbers; Kth smallest is not optimal.

## 15. Future improvements
Raptor flowcharts, step-by-step trace mode, saving results, binary search and sorting once covered.

## 16. Difficulties
- Deciding the scope so it stays inside the syllabus (no OOP, no databases).
- Keeping UI and logic separate.
- Wrong expected value in one test (T54) and an ungrammatical message ("3th") found while testing.
- Diagram tools: Mermaid could not be rendered locally, so Graphviz was used for the PDF images.

## Tricky examiner questions
1. *Why is `is_prime(1)` False?* By definition primes are >= 2; the function checks `n >= 2` first.
2. *What if I enter 0 for GCD?* gcd(0, b) = b; the menu asks for >= 1, the function accepts 0.
3. *Why does `reverse_number(1230)` give 321?* Leading zeros vanish in an integer.
4. *Why does `remove_duplicates_sorted` reject unsorted lists?* The one-pass method compares neighbours, which only works on ordered data; the menu sorts the list first.
5. *Show me where tuple assignment is used.* `swap_values`, `gcd`, `nth_fibonacci`, `fibonacci_series`.
6. *Can you hand-trace gcd(48, 18)?* (48,18) -> (18,12) -> (12,6) -> (6,0) -> answer 6.
7. *Why does the improved divisor method use 500 steps for 999983?* sqrt(999983) is about 999.99; testing odd numbers from 3 to 999 gives 499 checks plus the initial check of 2 = 500.
