# Design Document - MathMate

## 1. Functional Requirements
| ID | Requirement | Module |
|---|---|---|
| FR1 | Swap values, count/sum digits, factorial, Fibonacci series, reverse/palindrome, base conversion (2-16), character codes | Number Basics |
| FR2 | Integer square root, smallest divisor / prime check, GCD and LCM, prime sieve, prime factors, LCG random numbers, fast power, nth Fibonacci | Factoring |
| FR3 | Statistics, reverse, count, remove duplicates (ordered), partition, Kth smallest, frequency table, set operations | Array Analyzer |
| FR4 | Compare simple vs improved algorithm by step count and verify both answers match | Efficiency Lab |
| FR5 | Validate every input (type and range) and ask again when invalid | validation.py |
| FR6 | Show readable error messages for invalid mathematical input | menu.py |
| FR7 | Record each action in a log file | logger.py |

Input: numbers, lists of numbers, text (for character codes / other bases), menu choices.
Processing: the algorithm functions. Output: text printed to the terminal, log lines in `logs/mathmate.log`.

## 2. Non-Functional Requirements
| ID | Type | Requirement | How it is met / evidence |
|---|---|---|---|
| NFR1 | Usability | Numbered menus, prompts show valid ranges, invalid input is re-asked | menu.py, validation.py; T63-T65 |
| NFR2 | Reliability / error handling | Invalid input or invalid maths must never crash the program | try/except ValueError in `run_submenu`; EOF handling; T66, T70 |
| NFR3 | Performance | Every operation offered by the menu completes almost instantly | Measured on the build machine: sieve to 100000 = 8.7 ms, 2000-bit power < 1 ms, factorial(500) = 0.1 ms (single runs, will vary by machine) |
| NFR4 | Maintainability | Small single-purpose functions, docstrings, logic separated from UI | 7 source modules; tests call algorithm functions directly |
| NFR5 | Logging | Every action and error is recorded with timestamp | logger.py |
| NFR6 | Resource efficiency / security | Input ranges are capped (sieve <= 100000, exponent <= 2000, factorial <= 500) so a user cannot freeze the program | `read_int(..., minimum, maximum)` calls in menu.py |
| NFR7 | Portability | Standard library only, works on Windows, Linux, macOS | requirements.txt |

## 3. Architecture (layers)
1. **Presentation**: `main.py`, `menu.py` (menus, printing)
2. **Validation**: `validation.py`
3. **Algorithms**: `basic_algorithms.py`, `factoring.py`, `array_tools.py`, `efficiency.py`
4. **Support**: `logger.py`
Algorithm modules never call `input()` or `print()`, so they can be tested without a keyboard.

## 4. Course Concept Mapping
| Course concept (syllabus unit) | Project feature | Implementation | Evidence |
|---|---|---|---|
| Top-down design (U1) | Program split into menu -> modules -> functions | main.py, menu.py, four modules | Architecture diagram |
| Algorithm representation: flowchart, pseudo-code (U1) | Workflow flowchart of the program | docs/diagrams/workflow.png | Report section 7 |
| Program verification (U1) | Both methods must agree; properties checked over ranges | menu.py `do_lab_*`; tests/cases.py | T51, T53, T60, T61 |
| Efficiency and analysis of algorithms (U1) | Step counters for naive vs improved | efficiency.py | T52, T54, sample run 4 |
| Values, variables, expressions, tuple assignment (U2) | Swap, Euclid's GCD, Fibonacci update | `swap_values`, `gcd`, `nth_fibonacci` | T01, T23, T36 |
| Functions, parameters, arguments, modules (U2) | Every feature is a function in a module | all files | Component diagram |
| Exchange values, counting, summation, factorial, Fibonacci, reverse, base conversion, character to number (U3) | Module 1 | basic_algorithms.py | T01-T17 |
| Conditionals, while, for, continue, pass (U3) | Menus, validation loops | menu.py, validation.py (`continue`), logger.py (`pass`) | T63-T66 |
| Square root, smallest divisor, GCD, primes, prime factors, pseudo-random numbers, large power, nth Fibonacci (U4) | Module 2 | factoring.py | T18-T36, T60, T61 |
| Array reversal, counting, maximum, duplicate removal in ordered array, partitioning, Kth smallest (U5) | Module 3 | array_tools.py | T37-T47 |
| Lists, tuples, sets, dictionaries (U5) | `partition` returns a tuple; `set_operations` uses sets; `frequency_table`, `factor_dictionary` and menu tables use dictionaries | array_tools.py, factoring.py, menu.py | T44, T48, T49, T30 |
| Time trade-off (U5) | Nested loops vs set for duplicate detection | efficiency.py | T55, T56 |
| Tools: Scratch, Raptor (U6) | **Not used in the program.** Optional: draw a Raptor flowchart of `gcd` or `prime_factors` and add it to the report | - | - |

## 5. Design Decisions and Rationale
| Decision | Chosen | Alternatives considered | Why |
|---|---|---|---|
| Interface | Text menus | tkinter GUI, web app | GUI and web are not in the syllabus; a CLI keeps the focus on algorithms |
| Structure | Functions in modules | Classes (OOP) | OOP is not in the syllabus; the college accepts a component diagram instead of a class diagram |
| Menu control | Dictionary `{key: (label, function)}` | long if/elif chain | Uses dictionaries (Unit 5), adding an option is one line |
| Error strategy | Algorithms `raise ValueError`; menu catches it | return error codes | Keeps algorithms clean; one place shows messages |
| Input safety | `validation.py` re-asks until valid | validate inside every function | Avoids repeated code; crash-proof input |
| Efficiency measurement | Count steps | Time with `time` module | Step counts are the same on every computer and match Big-O analysis taught in Unit 1 |
| Tests | Plain data table + runner | unittest / pytest | Not in syllabus, no installation needed, and table output matches the college test-case format |
| Storage | Text log only | JSON / SQLite | The program needs no saved data, so no ER diagram is needed |

## 6. Error Handling Design
- Wrong type (letters for a number): `read_int` prints a message and asks again.
- Out of range: `read_int` checks minimum/maximum and asks again.
- Mathematically invalid (factorial of negative, digit not valid in base): the algorithm raises `ValueError`; `run_submenu` catches it, prints `Error: ...`, logs a WARNING and returns to the menu.
- Input stream closed (Ctrl+D / Ctrl+Z): caught and the program exits cleanly.
- Log file cannot be written: ignored so the program keeps working.

## 7. Security Considerations
There are no accounts, network access or stored personal data. Relevant risks are limited to resource
exhaustion, handled by capping input sizes (NFR6), and malformed input, handled by validation. `eval()` is never used.

## 8. Limitations
- Integers only (no decimals); command-line only; nothing saved between runs.
- `kth_smallest` is O(k x n), chosen for simplicity over speed.
- Prime factoring by trial division becomes slow for very large numbers with big prime factors.
- Efficiency Lab naive divisor and multiplication methods are capped only by menu range; a very large prime in option 1 takes noticeable time (a 6-digit prime took 73 ms on the build machine).

## 9. Future Enhancements
Raptor flowcharts for key algorithms; a Scratch animation of the sieve; saving results to a file;
decimal input; a step-by-step trace mode; more algorithms (e.g. binary search) once covered in class.
