"""
library.py

Project: Library Management System
Covers: classes & objects | file persistence (CSV) | menu-driven loop |
        searching, issuing, and returning books | basic exception handling
"""

import csv
import os

DATA_FILE = "library_data.csv"


class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        # if not provided (e.g. brand new book), all copies start as available
        self.available_copies = available_copies if available_copies is not None else total_copies


class Library:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.data_file):
            return  # no saved data yet, start with an empty library

        with open(self.data_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(
                    title=row["title"],
                    author=row["author"],
                    isbn=row["isbn"],
                    total_copies=int(row["total_copies"]),
                    available_copies=int(row["available_copies"]),
                )
                self.books.append(book)

    def save_books(self):
        with open(self.data_file, "w", newline="") as file:
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

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def add_book(self, title, author, isbn, total_copies):
        existing_book = self.find_book_by_isbn(isbn)
        if existing_book is not None:
            # book already exists — add more copies instead of duplicating
            existing_book.total_copies += total_copies
            existing_book.available_copies += total_copies
            print(f"Added {total_copies} more copies of '{existing_book.title}'.")
            return

        new_book = Book(title, author, isbn, total_copies)
        self.books.append(new_book)
        print(f"'{title}' added to the library.")

    def view_books(self):
        if len(self.books) == 0:
            print("No books in the library yet.")
            return

        print(f"\n{'Title':<25}{'Author':<20}{'ISBN':<15}{'Available':<10}")
        print("-" * 70)
        for book in self.books:
            print(f"{book.title:<25}{book.author:<20}{book.isbn:<15}{book.available_copies}/{book.total_copies}")

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

    def issue_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("No book found with that ISBN.")
            return

        if book.available_copies <= 0:
            print(f"'{book.title}' is currently unavailable — all copies are issued.")
            return

        book.available_copies -= 1
        print(f"'{book.title}' issued successfully. Remaining copies: {book.available_copies}")

    def return_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("No book found with that ISBN.")
            return

        if book.available_copies >= book.total_copies:
            print(f"All copies of '{book.title}' are already marked as available.")
            return

        book.available_copies += 1
        print(f"'{book.title}' returned successfully. Available copies: {book.available_copies}")


def display_menu():
    print("\n----- LIBRARY MANAGEMENT SYSTEM -----")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. Save & Exit")


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            try:
                total_copies = int(input("Enter number of copies: "))
                library.add_book(title, author, isbn, total_copies)
            except ValueError:
                print("Number of copies must be a whole number. Book not added.")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == "4":
            isbn = input("Enter ISBN of book to issue: ")
            library.issue_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == "6":
            library.save_books()
            print("Library data saved. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
