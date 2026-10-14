"""
library.py

Project: Library Management System
Covers: classes & objects | file persistence (CSV) | menu-driven loop |
        searching, issuing, and returning books | loan tracking with due dates |
        basic exception handling
"""

import csv
import os
from datetime import date, timedelta

DATA_FILE = "library_data.csv"
ISSUES_FILE = "library_issues.csv"
LOAN_DAYS = 14
FINE_PER_DAY = 2


def read_text(prompt):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_positive_int(prompt):
    """Keep asking until the user enters a whole number of at least 1."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value <= 0:
            print("Number must be at least 1.")
            continue
        return value


def shorten(text, width):
    """Trim text to fit a table column, ending with '...' if it was cut."""
    return text if len(text) <= width else text[:width - 3] + "..."


class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        # if not provided (e.g. brand new book), all copies start as available
        self.available_copies = available_copies if available_copies is not None else total_copies


class Library:
    def __init__(self, data_file=DATA_FILE, issues_file=ISSUES_FILE):
        self.data_file = data_file
        self.issues_file = issues_file
        self.books = []
        self.issues = []  # each loan: {"isbn", "member", "issue_date", "due_date"}
        self.load_books()
        self.load_issues()

    # ---------- loading and saving ----------

    def load_books(self):
        if not os.path.exists(self.data_file):
            return  # no saved data yet, start with an empty library

        with open(self.data_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line_number, row in enumerate(reader, start=2):  # line 1 is the header
                try:
                    book = Book(
                        title=row["title"],
                        author=row["author"],
                        isbn=row["isbn"],
                        total_copies=int(row["total_copies"]),
                        available_copies=int(row["available_copies"]),
                    )
                except (KeyError, ValueError, TypeError):
                    print(f"Skipping invalid row at line {line_number} in {self.data_file}.")
                    continue
                self.books.append(book)

    def save_books(self):
        with open(self.data_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["title", "author", "isbn", "total_copies", "available_copies"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "total_copies": book.total_copies,
                    "available_copies": book.available_copies,
                })

    def load_issues(self):
        if not os.path.exists(self.issues_file):
            return  # no loans saved yet

        with open(self.issues_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line_number, row in enumerate(reader, start=2):
                try:
                    self.issues.append({
                        "isbn": row["isbn"],
                        "member": row["member"],
                        "issue_date": date.fromisoformat(row["issue_date"]),
                        "due_date": date.fromisoformat(row["due_date"]),
                    })
                except (KeyError, ValueError, TypeError):
                    print(f"Skipping invalid row at line {line_number} in {self.issues_file}.")

    def save_issues(self):
        with open(self.issues_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["isbn", "member", "issue_date", "due_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for issue in self.issues:
                writer.writerow({
                    "isbn": issue["isbn"],
                    "member": issue["member"],
                    "issue_date": issue["issue_date"].isoformat(),
                    "due_date": issue["due_date"].isoformat(),
                })

    # ---------- books ----------

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def add_book(self, title, author, isbn, total_copies):
        if total_copies <= 0:
            print("Number of copies must be at least 1. Book not added.")
            return

        existing_book = self.find_book_by_isbn(isbn)
        if existing_book is not None:
            # book already exists — add more copies instead of duplicating
            existing_book.total_copies += total_copies
            existing_book.available_copies += total_copies
            self.save_books()
            print(f"Added {total_copies} more copies of '{existing_book.title}'.")
            return

        new_book = Book(title, author, isbn, total_copies)
        self.books.append(new_book)
        self.save_books()
        print(f"'{title}' added to the library.")

    def view_books(self):
        if len(self.books) == 0:
            print("No books in the library yet.")
            return

        print(f"\n{'Title':<25}{'Author':<20}{'ISBN':<15}{'Available':<10}")
        print("-" * 70)
        for book in self.books:
            print(f"{shorten(book.title, 24):<25}{shorten(book.author, 19):<20}"
                  f"{book.isbn:<15}{book.available_copies}/{book.total_copies}")

    def search_book(self, keyword):
        keyword_lower = keyword.lower()
        matches = []
        for book in self.books:
            if keyword_lower in book.title.lower() or keyword_lower in book.author.lower():
                matches.append(book)

        if len(matches) == 0:
            print(f"No books found matching '{keyword}'.")
            return

        print(f"\nFound {len(matches)} match(es):")
        for book in matches:
            print(f"  {book.title} by {book.author} (ISBN: {book.isbn}) - {book.available_copies} available")

    # ---------- loans ----------

    def issue_book(self, isbn, member):
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("No book found with that ISBN.")
            return

        if book.available_copies <= 0:
            print(f"'{book.title}' is currently unavailable — all copies are issued.")
            return

        issue_date = date.today()
        due_date = issue_date + timedelta(days=LOAN_DAYS)

        book.available_copies -= 1
        self.issues.append({
            "isbn": isbn,
            "member": member,
            "issue_date": issue_date,
            "due_date": due_date,
        })
        self.save_books()
        self.save_issues()
        print(f"'{book.title}' issued to {member}. Due on {due_date}.")

    def return_book(self, isbn, member):
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("No book found with that ISBN.")
            return

        record = next(
            (i for i in self.issues
             if i["isbn"] == isbn and i["member"].lower() == member.lower()),
            None,
        )
        if record is None:
            print(f"No issue record found for {member} and '{book.title}'.")
            return

        self.issues.remove(record)
        book.available_copies += 1
        self.save_books()
        self.save_issues()

        days_late = (date.today() - record["due_date"]).days
        if days_late > 0:
            print(f"'{book.title}' returned {days_late} day(s) late. Fine: {days_late * FINE_PER_DAY}")
        else:
            print(f"'{book.title}' returned on time. Thank you, {member}!")

    def view_overdue(self):
        today = date.today()
        overdue = [i for i in self.issues if i["due_date"] < today]

        if not overdue:
            print("No overdue books.")
            return

        print(f"\n{'Member':<20}{'ISBN':<15}{'Due date':<12}{'Days late'}")
        print("-" * 57)
        for issue in overdue:
            days_late = (today - issue["due_date"]).days
            print(f"{shorten(issue['member'], 19):<20}{issue['isbn']:<15}"
                  f"{str(issue['due_date']):<12}{days_late}")


def display_menu():
    print("\n----- LIBRARY MANAGEMENT SYSTEM -----")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. View Overdue Books")
    print("7. Save & Exit")


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = read_text("Enter title: ")
            author = read_text("Enter author: ")
            isbn = read_text("Enter ISBN: ")
            total_copies = read_positive_int("Enter number of copies: ")
            library.add_book(title, author, isbn, total_copies)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            keyword = read_text("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == "4":
            isbn = read_text("Enter ISBN of book to issue: ")
            member = read_text("Enter member name: ")
            library.issue_book(isbn, member)

        elif choice == "5":
            isbn = read_text("Enter ISBN of book to return: ")
            member = read_text("Enter member name: ")
            library.return_book(isbn, member)

        elif choice == "6":
            library.view_overdue()

        elif choice == "7":
            library.save_books()
            library.save_issues()
            print("Library data saved. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Your changes are already saved. Goodbye!")