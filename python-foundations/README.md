# Python Foundations

This repository documents my journey learning Python as a 1st-year Computer Engineering student — starting from core fundamentals and building up to small real-world projects. Everything here is written and understood by me, built incrementally as I learned each concept.

## Repository Structure

```
python-foundations/
├── basics/               Core Python concepts, one topic per file
├── file_handling/        Reading and writing text files
├── data_handling/        Working with CSV and Excel files
├── modules/              Creating and using a custom Python module
├── mini_projects/        Small standalone practice projects
├── projects/             Larger projects combining multiple concepts
├── requirements.txt      Python packages required to run everything here
└── .gitignore
```

## What's Inside

**`basics/`** — variables & types, control flow, functions, strings, lists & tuples, dictionaries & sets, exception handling, and OOP basics. Each file is self-contained, with a small real-world example baked in.

**`file_handling/`** — reading and writing `.txt` files, checking file existence, and a simple personal notes app.

**`data_handling/`** — reading/writing CSV files and Excel spreadsheets using `csv` and `openpyxl`.

**`modules/`** — a custom unit-conversion module, and a demo showing three different ways to import and use it.

**`mini_projects/`** — a to-do list, a contact book, and a quiz game. Small, self-contained, no file persistence by design.

**`projects/`** — two larger projects that combine OOP, file persistence, and exception handling:
- `library_management/` — track books, issue/return, with data saved to CSV
- `banking_system/` — accounts, PIN-protected transactions, fund transfers

## How to Run Any File

```
python <path_to_file>.py
```

Some files depend on another running first (e.g. `text_file_read.py` needs `text_file_write.py` run beforehand) — this is noted at the top of those files.

## Setup

```
pip install -r requirements.txt
```

## What I'd Improve Next

- Add persistent transaction history to the banking system
- Add due-date tracking to the library system
- Start exploring basic DSA and algorithmic problem-solving
- Explore building a small project with an actual database instead of CSV files

## About This Repository

I'm a 1st-year CSE student building this repo to genuinely track and demonstrate what I've learned, not to look more advanced than I am. Every file was built, tested, and understood — not copy-pasted. Suggestions and feedback are welcome.
