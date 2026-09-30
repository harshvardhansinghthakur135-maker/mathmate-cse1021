# MathMate - Problem Solving Toolkit

A menu-driven Python program that lets you try the core algorithms of **CSE1021 - Introduction to Problem
Solving and Programming** with your own inputs, and compare simple and improved algorithms by counting steps.
Built for the VITyarthi *Build Your Own Project* evaluation.

## Overview
MathMate has four modules, each mapped to a unit of the syllabus:

| Module | Syllabus unit | What it does |
|---|---|---|
| Number Basics | Unit 3 | swap, count/sum digits, factorial, Fibonacci, reverse, palindrome, base conversion, character codes |
| Factoring & Number Theory | Unit 4 | square root, smallest divisor, GCD/LCM, primes, prime factors, pseudo-random numbers, large powers, nth Fibonacci |
| Array & List Analyzer | Unit 5 | statistics, reverse, count, remove duplicates, partition, Kth smallest, frequency (dictionary), sets |
| Efficiency Lab | Unit 1 + Unit 5 (time trade-off) | naive vs improved methods with step counts and result verification |

## Features
- Clean text menus (dictionary-driven)
- Every input is validated; the program asks again instead of crashing
- Clear error messages for invalid mathematical input (for example factorial of a negative number)
- Activity log in `logs/mathmate.log`
- 70 automated test cases (unit, edge case, verification and menu-integration tests)

## Technologies / Tools Used
- Python 3.8+ (standard library only: `os`, `datetime`, `subprocess` (tests), `sys`)
- Git and GitHub for version control
- Graphviz / Mermaid for diagrams (documentation only)

## Installation
```bash
git clone <your-repository-url>
cd mathmate
python --version        # must be 3.8 or newer
```
No packages need to be installed.

## Run
```bash
python main.py
```
Choose a module by typing its number and pressing Enter. Type `0` to go back or exit.

## Testing
```bash
python tests/run_tests.py
```
This prints a table (Test ID, Description, Input, Expected, Actual, Status) and rewrites
`docs/test_results.md`. The exit code is 0 only if all tests pass.

## Project Structure
```
mathmate/
├── main.py                     entry point
├── toolkit/
│   ├── menu.py                 menus (user interface)
│   ├── validation.py           safe input reading
│   ├── logger.py               activity log
│   ├── basic_algorithms.py     Module 1 (Unit 3)
│   ├── factoring.py            Module 2 (Unit 4)
│   ├── array_tools.py          Module 3 (Unit 5)
│   └── efficiency.py           Module 4 (Unit 1 / time trade-off)
├── tests/                      test cases and runner
├── docs/                       design, diagrams, viva, audit, sample runs
├── statement.md
└── README.md
```

## Screenshots
Add your own screenshots to `docs/screenshots/` and link them here (see `docs/screenshot_checklist.md`).
Real console output captured from runs is available in `docs/sample_runs/`.

## Documentation
See the `docs/` folder: `design.md`, `diagrams.md`, `test_results.md`, `viva_prep.md`,
`requirement_audit.md`, `git_commit_plan.md`.

## Limitations
Command-line only; integer inputs only; results are not saved between runs.
