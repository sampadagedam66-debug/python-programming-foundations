# Library Management System

A console-based library management system built in Python. Tracks books, lets you issue and return them, and saves everything to a CSV file so data isn't lost between runs.

## Features
- Add new books (or add more copies of an existing one, matched by ISBN)
- View all books with real-time available/total copy counts
- Search books by title or author (case-insensitive, partial match)
- Issue a book (blocks issuing if no copies are available)
- Return a book (blocks over-returning beyond total copies)
- Data automatically saved to `library_data.csv` on exit, and reloaded on next run

## Concepts Used
- Object-Oriented Programming (`Book` and `Library` classes)
- File handling with CSV (`csv.DictReader` / `csv.DictWriter`)
- Menu-driven program loop
- Conditional logic for input validation and business rules
- Exception handling for invalid numeric input

## How to Run
```
python library.py
```

## Project Structure
```
library_management/
├── library.py
├── library_data.csv   (created automatically after first run)
└── README.md
```

## Future Improvements
- Add due dates and overdue tracking for issued books
- Add a member/borrower system instead of tracking only ISBNs
