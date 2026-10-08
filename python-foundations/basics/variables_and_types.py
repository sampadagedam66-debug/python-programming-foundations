"""
variables_and_types.py
Topic: Variables and Data Types in Python

Covers:
1. Basic data types
2. type() and isinstance()
3. Constants and type conversion
4. Mutability and object identity
5. Augmented assignment
6. Float precision
7. Boolean and integer relationship
8. Mini project - AI API billing
"""

# 1. Basic Data Types
print("\n--- SYSTEM CONFIGURATION ---")

application = input("Enter application name: ").strip()
version = float(input("Enter application version: "))
users = int(input("Enter number of active users: "))
maintenance = input("Is maintenance enabled? (yes/no): ").lower() == "yes"

print("\nApplication:", application)
print("Version:", version)
print("Active Users:", users)
print("Maintenance:", maintenance)

print("\nData Types:")
print(type(application).__name__)
print(type(version).__name__)
print(type(users).__name__)
print(type(maintenance).__name__)


# 2. type() and isinstance()
print("\n--- TYPE CHECKING ---")

value = input("Enter any value: ")

print("Value:", value)
print("Type:", type(value).__name__)
print("Is string?", isinstance(value, str))
print("Is integer?", isinstance(value, int))

# Input() always returns a string
number = int(input("Enter a number: "))

print("Number:", number)
print("Is integer?", isinstance(number, int))


# 3. Constants and Type Conversion
print("\n--- DATA CONVERSION ---")

MAX_USERS = 1000
current_users = int(input("Enter current users: "))

remaining = MAX_USERS - current_users
usage_percentage = (current_users / MAX_USERS) * 100

print("Remaining user slots:", remaining)
print("Usage:", round(usage_percentage, 2), "%")

# Explicit type conversion
percentage_text = str(round(usage_percentage, 2))
print("Percentage as string:", percentage_text)


# 4. Mutability and Object Identity
print("\n--- OBJECT IDENTITY ---")

scores = [75, 82, 91]
backup = scores

print("Original scores:", scores)
print("Scores ID:", id(scores))
print("Backup ID:", id(backup))

scores.append(88)

print("\nAfter modifying scores:")
print("Scores:", scores)
print("Backup:", backup)
print("Same object?", scores is backup)


# 5. Augmented Assignment
print("\n--- RESOURCE TRACKER ---")

storage = 250
print("Starting storage:", storage, "GB")

storage += 100
print("After adding storage:", storage, "GB")

storage -= 50
print("After removing storage:", storage, "GB")

storage *= 2
print("After upgrade:", storage, "GB")


# 6. Float Precision
print("\n--- FLOAT PRECISION ---")

first = 0.1
second = 0.2

result = first + second

print("0.1 + 0.2 =", result)
print("Using round():", round(result, 2))
print("Exact comparison:", result == 0.3)


# 7. Boolean and Integer Relationship
print("\n--- BOOLEAN AND INTEGER ---")

login = input("Was login successful? (yes/no): ").lower() == "yes"

print("Login status:", login)
print("Boolean value as integer:", int(login))
print("Is bool a subclass of int?", issubclass(bool, int))


# 8. Mini Project - AI API Billing
print("\n--- AI API BILLING SYSTEM ---")

BASE_PRICE = 499
INCLUDED_TOKENS = 100000
PRICE_PER_1000 = 0.80

customer = input("Enter customer name: ").strip()
tokens_used = int(input("Enter total tokens used: "))

if tokens_used < 0:
    print("Invalid token count.")
else:
    extra_tokens = max(0, tokens_used - INCLUDED_TOKENS)
    extra_cost = (extra_tokens / 1000) * PRICE_PER_1000

    plan = input("Are you a Pro member? (yes/no): ").lower()
    discount = extra_cost * 0.20 if plan == "yes" else 0

    final_amount = BASE_PRICE + extra_cost - discount

    print("\n----- BILL SUMMARY -----")
    print("Customer:", customer)
    print("Tokens Used:", tokens_used)
    print("Included Tokens:", INCLUDED_TOKENS)
    print("Extra Tokens:", extra_tokens)
    print(f"Extra Usage Cost: Rs {extra_cost:.2f}")
    print(f"Discount: Rs {discount:.2f}")
    print(f"Final Amount: Rs {final_amount:.2f}")

print("\nProgram completed successfully.")