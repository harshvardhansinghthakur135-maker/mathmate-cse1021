# Screenshot Checklist
Run `python main.py` and capture the terminal window (keep the window wide enough that nothing wraps).
Save into `docs/screenshots/` with the file names below. **Only use real screenshots of your own runs.**
Matching text output already exists in `docs/sample_runs/` so you can cross-check what you should see.

| # | File name | Input to type (in order) | What must be visible | Why useful | Report section |
|---|---|---|---|---|---|
| 1 | 01_main_menu.png | run program | banner and main menu with 4 modules | shows entry point and structure | 10 Screenshots |
| 2 | 02_number_basics.png | 1, 6, 255, 16 | 255 converted to FF | Module 1 (Unit 3) | 10 |
| 3 | 03_factoring.png | 2, 5, 360 | `360 = 2^3 x 3^2 x 5` | Module 2 (Unit 4) | 10 |
| 4 | 04_large_power.png | 2, 7, base 2, exponent 100 | 2^100 with digit count | large power demo | 10 |
| 5 | 05_array_summary.png | 3, 1, `12 5 9 5 20 1` | statistics table | Module 3 (Unit 5) | 10 |
| 6 | 06_kth_smallest.png | 3, 6, `9 4 7 1 8`, 3 | Kth smallest = 7 | array technique | 10 |
| 7 | 07_efficiency_lab.png | 4, 1, 999983 | 999982 vs 500 steps, both agree | Unit 1 analysis | 10 |
| 8 | 08_validation.png | 1, 3, `abc`, then 999 | re-asked messages | input validation | 10 / 11 |
| 9 | 09_error_handling.png | 1, 7, base 2, `1092` | `Error: '9' is not a valid digit in base 2.` then menu again | error handling | 10 / 11 |
| 10 | 10_test_run.png | `python tests/run_tests.py` | last lines: `Total: 70 Passed: 70 Failed: 0` | testing evidence | 11 |
| 11 | 11_log_file.png | open logs/mathmate.log | timestamped INFO and WARNING lines | logging NFR | 10 |
| 12 | 12_github_repo.png | browser | repository file list, README | GitHub structure | 10 |
| 13 | 13_commit_history.png | browser | commits page | version control | 10 |
