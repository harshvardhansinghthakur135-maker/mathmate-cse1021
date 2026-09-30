# Requirement Audit (status as of this build)
Legend: **Done** = implemented and checked in this build; **Your action** = needs something only you can supply.

| College requirement | Where implemented | Where documented | Evidence | Status |
|---|---|---|---|---|
| >= 3 major functional modules | 4 modules in `toolkit/` | README, design.md | sample runs | Done |
| Clear input/output structure | menu.py + validation.py | design.md s1 | sample_runs/ | Done |
| Logical workflow | menu.py | workflow diagram | T62-T70 | Done |
| Real-world problem | learning tool for CSE1021 students | statement.md | - | Done |
| >= 4 NFRs | 7 listed | design.md s2 | NFR table | Done |
| Architecture | 4 layers | design.md s3, diagram | architecture.png | Done |
| Correct use of subject concepts | modules map to Units 1-5 | design.md s4 | tests | Done (Scratch/Raptor not used; optional) |
| Modular, clean code, comments | docstrings in every function | source files | - | Done |
| Validation | validation.py | design.md s6 | T57-T59, T63-T65 | Done |
| Error handling | menu.py `run_submenu` | design.md s6 | T66, T70 | Done |
| Git / version control | commit plan provided | git_commit_plan.md | - | **Your action**: run the commands, push to GitHub |
| 5-10 modules/files | 7 source files + 2 test files | README structure | - | Done |
| Folder structure | toolkit/, tests/, docs/ | README | - | Done |
| Testing | tests/ | test_results.md | 70/70 pass on last run | Done |
| Problem Statement, Objectives, FR, NFR | statement.md, design.md, report | report s3-s8 | - | Done |
| Architecture / Workflow / Use case / Component / Sequence diagrams | docs/diagrams | diagrams.md | PNG + Mermaid | Done (Mermaid not render-tested) |
| ER diagram / schema | none (no database) | design.md, report | - | N/A |
| README.md | root | - | - | Done |
| statement.md | root | - | - | Done |
| Project report PDF | report/MathMate_Project_Report.pdf | - | - | Done, but **Your action**: fill name/register number on cover and insert screenshots |
| Screenshots | checklist in docs/ | report s10 | - | **Your action** (cannot be fabricated) |

## Course relevance audit
| Component | Course concept | Code location | How to show in viva |
|---|---|---|---|
| Module 1 | Unit 3 fundamental algorithms | basic_algorithms.py | run menu 1 |
| Module 2 | Unit 4 factoring methods | factoring.py | run menu 2, hand-trace gcd |
| Module 3 | Unit 5 arrays, lists, sets, dicts | array_tools.py | run menu 3 |
| Module 4 | Unit 1 efficiency/analysis, Unit 5 time trade-off | efficiency.py | run menu 4 with 999983 |
| Menu tables | dictionaries | menu.py | point at `BASIC_MENU` |

## Quality audit
Code quality, modularity, validation, error handling, testing (70/70), documentation and diagrams are complete.
Known gaps: no Raptor flowchart, screenshots not yet captured, Git history not yet created, Mermaid blocks not render-tested, personal details missing on cover page.
