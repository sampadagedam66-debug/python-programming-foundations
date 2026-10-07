"""
oop_basics.py
Topic: Object-Oriented Programming Basics
"""

# 1. Class and Object - Book
print("\n--- BOOK DETAILS ---")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def show(self):
        status = "Available" if self.available else "Not Available"
        print(f"{self.title} by {self.author} - {status}")


title = input("Enter book name: ")
author = input("Enter author name: ")

book = Book(title, author)
book.show()


# 2. Method that changes data - Bank Account
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


name = input("Enter account holder: ")
balance = float(input("Enter starting balance: "))

account = Account(name, balance)

deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)

withdraw = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw)

print("Final balance: Rs", account.balance)


# 3. Multiple Objects - Students
print("\n--- STUDENT RECORDS ---")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "-", self.marks, "marks")


student1 = Student(input("Enter first student: "),
                   int(input("Enter marks: ")))

student2 = Student(input("Enter second student: "),
                   int(input("Enter marks: ")))

student1.show()
student2.show()


# 4. self + Computed Method - Rectangle
print("\n--- RECTANGLE ---")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter length: "))
width = float(input("Enter width: "))

rectangle = Rectangle(length, width)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# 5. Mini Project - Food Order
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


customer = input("Enter your name: ")
order = Order(customer)

for i in range(2):
    food = input("Enter food item: ")
    price = float(input("Enter price: "))
    order.add_item(food, price)

order.show_order()

print("\n🎉 Thank you for using the program!")
