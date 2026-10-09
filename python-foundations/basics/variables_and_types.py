"""
variables_and_data_types_advanced.py
Topic: Variables and Data Types (slightly advanced)

Covers: multiple assignment, swapping, constants, type hints,
type detection and conversion, number types, mutable vs immutable,
identity (id / is), copying, None, and truthy / falsy values.

Run the file and type your answers when asked.
"""

import sys


def read_int(prompt):
    """Keep asking until a valid whole number is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def detect_type(text):
    """Turn text into the most suitable type: bool, int, float or str."""
    if text.lower() in ("true", "false"):
        return text.lower() == "true"
    for convert in (int, float):
        try:
            return convert(text)
        except ValueError:
            pass
    return text


# ---------------------------------------------------
# 1. VARIABLES
# ---------------------------------------------------
print("--- 1. VARIABLES ---")

x = y = z = 0                                    # one value, many variables
print("x, y, z =", x, y, z)

first = input("\nEnter first value : ")
second = input("Enter second value: ")
print(f"Before swap -> first: {first}, second: {second}")

first, second = second, first                    # swap in one line
print(f"After swap  -> first: {first}, second: {second}")

MAX_LIMIT = 100                                  # CAPITALS = constant (by convention)

score: int = "ninety"                            # type hint says int, but Python does not enforce it
print("\nscore has a type hint of int, yet its type is", type(score).__name__)


# ---------------------------------------------------
# 2. TYPE DETECTION
# ---------------------------------------------------
print("\n--- 2. TYPE DETECTION ---")

text = input("Enter any value (try 42, 3.14, True, hello): ")
value = detect_type(text)

print(f"\nValue        : {value!r}")
print(f"Type         : {type(value).__name__}")
print(f"Memory id    : {id(value)}")
print(f"Size (bytes) : {sys.getsizeof(value)}")
print(f"As a bool    : {bool(value)}")


# ---------------------------------------------------
# 3. NUMBER TYPES
# ---------------------------------------------------
print("\n--- 3. NUMBER TYPES ---")

n = read_int("Enter a whole number: ")

print(f"\nBinary / Octal / Hex : {bin(n)} / {oct(n)} / {hex(n)}")
print(f"As float             : {float(n)}")
print(f"As complex           : {complex(n, 2)}")
print(f"n to the power 20    : {n ** 20}   (int has no size limit)")
print(f"0.1 + 0.2            : {0.1 + 0.2}   (floats are approximate)")
print(f"round(0.1 + 0.2, 2)  : {round(0.1 + 0.2, 2)}")
print(f"True + True          : {True + True}   (bool is a kind of int)")


# ---------------------------------------------------
# 4. MUTABLE vs IMMUTABLE
# ---------------------------------------------------
print("\n--- 4. MUTABLE vs IMMUTABLE ---")

word = input("Enter a word: ")

try:
    word[0] = "X"                                # strings cannot be changed in place
except TypeError as error:
    print("Strings are immutable ->", error)

fruits = ["apple", "banana"]
fruits.append(input("Add a fruit: "))

alias = fruits                                   # same list, new name
copied = fruits.copy()                           # a separate list
fruits.append("mango")

print("\nfruits :", fruits)
print("alias  :", alias, "<- changed too (same object)")
print("copied :", copied, "<- not changed")
print("alias is fruits  :", alias is fruits)
print("copied is fruits :", copied is fruits)

# A tuple is immutable, but a list stored inside it can still change
data = (1, [2, 3])
data[1].append(4)
print("\nTuple with a list inside:", data)

try:
    bad = {["a", "b"]: "value"}                  # lists cannot be dictionary keys
except TypeError as error:
    print("Dictionary key error ->", error)


# ---------------------------------------------------
# 5. NONE AND TRUTHY / FALSY
# ---------------------------------------------------
print("\n--- 5. NONE AND TRUTHY / FALSY ---")

nothing = None
print("None type   :", type(nothing).__name__)
print("Is None?    :", nothing is None)

print()
for item in [0, 0.0, "", "0", [], [0], {}, None]:
    print(f"bool({item!r:>4}) -> {bool(item)}")

print("\nDone!")



