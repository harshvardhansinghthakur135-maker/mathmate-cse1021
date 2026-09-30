# Project Statement - MathMate

## Problem Statement
First-year programming students learn many classic algorithms (digit manipulation, base conversion,
GCD, prime factors, Kth smallest element, and so on), but each algorithm is usually practised in a
separate, throw-away program. Students also rarely see *why* one method is better than another, because
the difference is hidden when the numbers are small. There is no single place where a beginner can try
these algorithms with their own inputs, get clear error messages when the input is wrong, and compare a
simple method with an improved one.

## Project Scope
**In scope**
- A menu-driven Python program (command-line) with four modules:
  1. Number Basics (CSE1021 Unit 3)
  2. Factoring & Number Theory (Unit 4)
  3. Array & List Analyzer (Unit 5)
  4. Efficiency Lab (Unit 1 analysis of algorithms, Unit 5 time trade-off)
- Input validation, error handling and an activity log
- 70 automated test cases and full documentation

**Out of scope**
- Graphical / web interface, database, user accounts, networking
- Algorithms not present in the CSE1021 syllabus (for example sorting algorithm libraries, recursion, OOP)

## Target Users
- First-year students taking CSE1021 (Introduction to Problem Solving and Programming)
- Teachers who want a quick demonstration tool for algorithm efficiency
- Beginners who want to check their own hand-calculated answers

## High-Level Features
- Swap, digit count/sum, factorial, Fibonacci series, reverse/palindrome, base conversion (2-16), character codes
- Integer square root, smallest divisor, GCD/LCM, prime sieve, prime factors, LCG pseudo-random numbers, fast power, nth Fibonacci
- List statistics, reverse, counting, duplicate removal (ordered list), partition, Kth smallest, frequency table, set operations
- Step-count comparison of simple vs improved algorithms, with a built-in check that both give the same answer
- Repeated prompting on invalid input, readable error messages, log file of activity
