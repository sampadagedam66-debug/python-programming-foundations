"""
variables_and_data_types.py
Topic: Variables and Data Types
"""

# Variables, multiple assignment and type hints

name: str = input("Enter your name: ")

while True:
try:
age: int = int(input("Enter your age: "))
break
except ValueError:
print("Enter a valid age.")

height: float = float(input("Enter your height: "))
is_student: bool = input("Are you a student? (yes/no): ").lower() == "yes"

x, y = 10, 20
x, y = y, x

MAX_AGE: int = 100

print("\n--- BASIC TYPES ---")
print(f"{name = } | {type(name).**name**}")
print(f"{age = } | {type(age).**name**}")
print(f"{height = } | {type(height).**name**}")
print(f"{is_student = } | {type(is_student).**name**}")

# Other data types

complex_num = complex(age, 2)
nothing = None
skills = ["Python", "Git", "SQL"]
coordinates = (18.52, 73.85)
unique_values = {10, 20, 20, 30}
student = {"name": name, "age": age}

print("\n--- COLLECTIONS & OTHER TYPES ---")
for value in [complex_num, nothing, skills, coordinates, unique_values, student]:
print(f"{value!r:<30} -> {type(value).**name**}")

# Type conversion with error handling

text = input("\nEnter a number for conversion: ")

for conversion in (int, float):
try:
print(f"{conversion.**name**}(): {conversion(text)}")
except ValueError:
print(f"{conversion.**name**}(): conversion failed")

print(f"str(): {str(age)}")
print(f"bool(): {bool(text)}")

# Mutable vs immutable, alias vs copy

numbers = [1, 2, 3]
alias = numbers
copied = numbers.copy()

numbers.append(4)

print("\n--- MUTABILITY & IDENTITY ---")
print("numbers:", numbers)
print("alias  :", alias)
print("copy   :", copied)

print("alias is numbers :", alias is numbers)
print("copy is numbers  :", copied is numbers)
print("id(numbers)      :", id(numbers))

# == vs is

a = [1, 2]
b = [1, 2]
c = a

print("\n--- == VS IS ---")
print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)

print("\nMAX_AGE:", MAX_AGE)
print("Swapped values:", x, y)
print("None check:", nothing is None)
print("Program completed.")



