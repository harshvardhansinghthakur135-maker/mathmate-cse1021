# Git Commit Plan (suggested - you must run the commands yourself)

This is a *suggested* sequence. Make the commits over the real days you work so the history shows genuine
progress. Do not claim commits you did not make.

```bash
git init
git config user.name "Your Name"
git config user.email "you@example.com"

# 1
git add statement.md .gitignore requirements.txt
git commit -m "Add project statement, gitignore and requirements"
# 2
git add toolkit/__init__.py toolkit/validation.py toolkit/logger.py
git commit -m "Add input validation and logging helpers"
# 3
git add toolkit/basic_algorithms.py
git commit -m "Add Module 1: number basics (Unit 3 algorithms)"
# 4
git add toolkit/factoring.py
git commit -m "Add Module 2: factoring and number theory (Unit 4)"
# 5
git add toolkit/array_tools.py
git commit -m "Add Module 3: array and list analyzer (Unit 5)"
# 6
git add toolkit/efficiency.py
git commit -m "Add Module 4: efficiency lab with step counters"
# 7
git add toolkit/menu.py main.py
git commit -m "Add menu interface and program entry point"
# 8
git add tests/
git commit -m "Add 70 test cases and test runner"
# 9
git add docs/design.md docs/diagrams.md docs/diagrams/
git commit -m "Add design document and diagrams"
# 10
git add docs/sample_runs docs/test_results.md docs/screenshots
git commit -m "Add sample runs, test results and screenshots"
# 11
git add README.md docs/viva_prep.md docs/requirement_audit.md docs/screenshot_checklist.md docs/git_commit_plan.md
git commit -m "Add README and remaining documentation"

git branch -M main
git remote add origin https://github.com/<your-username>/mathmate.git
git push -u origin main
```
Tip: the two-step approach (commit each module right after you finish reading and running it) is more
convincing than committing everything on one day.
