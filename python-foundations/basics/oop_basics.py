"""oop_basics.py - Object-Oriented Programming Basics"""

# 1. Class and Object - Book
print("\n--- BOOK ---")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {status}"

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed!")
        else:
            print("Already borrowed.")

    def return_book(self):
        self.available = True
        print("Book returned!")

book = Book(input("Book name: "), input("Author: "))
print(book)
book.borrow()
print(book)
book.return_book()
print(book)


# 2. Bank Account
print("\n--- BANK ACCOUNT ---")

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

account = Account(input("Holder: "), float(input("Starting balance: ")))
account.deposit(float(input("Deposit: ")))
account.withdraw(float(input("Withdraw: ")))
print("Final balance: Rs", account.balance)


# 3. Students
print("\n--- STUDENTS ---")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "-", self.marks, "marks")

s1 = Student(input("Student 1: "), int(input("Marks: ")))
s2 = Student(input("Student 2: "), int(input("Marks: ")))
s1.show()
s2.show()


# 4. Rectangle
print("\n--- RECTANGLE ---")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(float(input("Length: ")), float(input("Width: ")))
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


# 5. Food Order
print("\n--- FOOD ORDER ---")

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def add_item(self, name, price):
        self.items.append(name)
        self.total += price

    def show_order(self):
        print("\nCustomer:", self.customer)
        print("Items:", self.items)
        print("Total: Rs", self.total)

order = Order(input("Your name: "))
for _ in range(2):
    order.add_item(input("Food item: "), float(input("Price: ")))
order.show_order()

print("\n🎉 Thank you for using the program!")