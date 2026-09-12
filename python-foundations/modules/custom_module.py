"""
custom_module.py

Topic: Creating a Custom Module in Python
A small reusable unit-conversion utility module — meant to be
imported elsewhere, not run directly (see the __main__ guard below).
"""

PI = 3.14159


def km_to_miles(km):
    return km * 0.621371


def kg_to_pounds(kg):
    return kg * 2.20462


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def circle_area(radius):
    return PI * (radius ** 2)


# This block ONLY runs when custom_module.py is executed directly,
# NOT when it's imported by another file (like module_demo.py).
# It's useful for quickly testing the module on its own.
if __name__ == "__main__":
    print("Running custom_module.py directly — testing functions:")
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"70 kg = {kg_to_pounds(70):.2f} pounds")
    print(f"25 C = {celsius_to_fahrenheit(25):.2f} F")
    print(f"Area of circle (radius 5) = {circle_area(5):.2f}")
