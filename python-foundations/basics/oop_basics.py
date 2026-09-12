"""
oop_basics.py

Topic: Object-Oriented Programming Basics in Python
Covers: class definition, __init__, attributes | methods that modify state |
        multiple objects from one class | self explained + computed methods
Mini use-case: a simple food ordering system
"""

# ---------------------------------------------------------
# SECTION 1: Class Definition & Attributes — Library Book Record
# ---------------------------------------------------------
print("---- Class Basics: Library Book Record ----")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # default value when a book is created

    def display_info(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}")


book_1 = Book("The Alchemist", "Paulo Coelho", "978-0062315007")
book_1.display_info()


# ---------------------------------------------------------
# SECTION 2: Methods That Modify State — Bank Account
# ---------------------------------------------------------
print("\n---- Methods Modifying State: Bank Account ----")

class Account:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount}. New balance: Rs {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: Rs {self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew Rs {amount}. New balance: Rs {self.balance}")


savings_account = Account("Rohan Gupta", balance=1000)
savings_account.deposit(500)
savings_account.withdraw(2000)   # should show insufficient funds
savings_account.withdraw(800)    # should succeed


# ---------------------------------------------------------
# SECTION 3: Multiple Objects From One Class — Employee Records
# ---------------------------------------------------------
print("\n---- Multiple Objects: Employee Records ----")

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self):
        print(f"{self.name} - {self.role} - Rs {self.salary}/month")


employee_1 = Employee("Sana Iqbal", "Backend Developer", 55000)
employee_2 = Employee("Devraj Singh", "QA Engineer", 42000)
employee_3 = Employee("Meera Nair", "UI/UX Designer", 48000)

employee_1.display_info()
employee_2.display_info()
employee_3.display_info()

# each object keeps its own separate data, even though all three
# come from the exact same class definition
print(f"\nEmployee 1 salary: {employee_1.salary}, Employee 2 salary: {employee_2.salary}")


# ---------------------------------------------------------
# SECTION 4: self Explained + Computed Method — Rectangle
# ---------------------------------------------------------
print("\n---- self Explained: Rectangle ----")

class Rectangle:
    def __init__(self, length, width):
        # 'self' refers to THIS specific object being created —
        # it's how the object stores its own length and width
        self.length = length
        self.width = width

    def calculate_area(self):
        # 'self' here lets the method reach back into the SAME
        # object's length and width, not some other rectangle's
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


rectangle_1 = Rectangle(10, 5)
rectangle_2 = Rectangle(7, 3)

print(f"Rectangle 1: Area = {rectangle_1.calculate_area()}, Perimeter = {rectangle_1.calculate_perimeter()}")
print(f"Rectangle 2: Area = {rectangle_2.calculate_area()}, Perimeter = {rectangle_2.calculate_perimeter()}")
print("Notice: same method, but 'self' makes each call use its own object's values.")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Simple Food Ordering System
# ---------------------------------------------------------
# Two classes working together, a different domain from every
# section above: an Order holds a list of MenuItem objects.

print("\n---- Mini Project: Food Ordering System ----")

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Added '{menu_item.name}' (Rs {menu_item.price}) to {self.customer_name}'s order")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


margherita_pizza = MenuItem("Margherita Pizza", 249)
cold_coffee = MenuItem("Cold Coffee", 99)
garlic_bread = MenuItem("Garlic Bread", 129)

customer_order = Order("Aditi Sharma")
customer_order.add_item(margherita_pizza)
customer_order.add_item(cold_coffee)
customer_order.add_item(garlic_bread)

order_total = customer_order.calculate_total()
print(f"\nTotal bill for {customer_order.customer_name}: Rs {order_total}")
