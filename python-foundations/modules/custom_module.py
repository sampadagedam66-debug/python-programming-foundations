"""
"""
custom_module.py

Topic: Creating a Custom Module in Python
A reusable unit-conversion utility module, meant to be imported
elsewhere (see the __main__ guard at the bottom for a quick demo).

Features:
    - Length, weight, temperature and circle helpers
    - Reverse conversions (miles -> km, F -> C, ...)
    - Input validation with clear error messages
    - convert(): one function for any supported unit pair
    - Interactive converter when the file is run directly
"""

import math

__all__ = [
    "PI",
    "km_to_miles", "miles_to_km",
    "kg_to_pounds", "pounds_to_kg",
    "meters_to_feet", "feet_to_meters",
    "celsius_to_fahrenheit", "fahrenheit_to_celsius",
    "celsius_to_kelvin", "kelvin_to_celsius",
    "circle_area", "circle_circumference",
    "convert",
]

# ---------- Constants ----------
PI = math.pi
KM_TO_MILES = 0.621371
KG_TO_POUNDS = 2.20462
METERS_TO_FEET = 3.28084
ABSOLUTE_ZERO_C = -273.15


# ---------- Validation helpers (private) ----------
def _check_number(value, name="value"):
    """Raise TypeError if value is not an int or float."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")
    return value


def _check_non_negative(value, name="value"):
    """Raise ValueError if value is negative."""
    _check_number(value, name)
    if value < 0:
        raise ValueError(f"{name} cannot be negative, got {value}")
    return value


def _check_celsius(celsius):
    """Raise ValueError if the temperature is below absolute zero."""
    _check_number(celsius, "temperature")
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError(f"temperature cannot be below absolute zero ({ABSOLUTE_ZERO_C} C)")
    return celsius


# ---------- Length ----------
def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return _check_non_negative(km, "km") * KM_TO_MILES


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return _check_non_negative(miles, "miles") / KM_TO_MILES


def meters_to_feet(meters: float) -> float:
    """Convert meters to feet."""
    return _check_non_negative(meters, "meters") * METERS_TO_FEET


def feet_to_meters(feet: float) -> float:
    """Convert feet to meters."""
    return _check_non_negative(feet, "feet") / METERS_TO_FEET


# ---------- Weight ----------
def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return _check_non_negative(kg, "kg") * KG_TO_POUNDS


def pounds_to_kg(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return _check_non_negative(pounds, "pounds") / KG_TO_POUNDS


# ---------- Temperature ----------
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (_check_celsius(celsius) * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    _check_number(fahrenheit, "temperature")
    celsius = (fahrenheit - 32) * 5 / 9
    _check_celsius(celsius)
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return _check_celsius(celsius) - ABSOLUTE_ZERO_C


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return _check_non_negative(kelvin, "kelvin") + ABSOLUTE_ZERO_C


# ---------- Circle ----------
def circle_area(radius: float) -> float:
    """Return the area of a circle."""
    return PI * (_check_non_negative(radius, "radius") ** 2)


def circle_circumference(radius: float) -> float:
    """Return the circumference of a circle."""
    return 2 * PI * _check_non_negative(radius, "radius")


# ---------- One function for everything ----------
_CONVERTERS = {
    ("km", "miles"): km_to_miles,
    ("miles", "km"): miles_to_km,
    ("kg", "pounds"): kg_to_pounds,
    ("pounds", "kg"): pounds_to_kg,
    ("m", "ft"): meters_to_feet,
    ("ft", "m"): feet_to_meters,
    ("c", "f"): celsius_to_fahrenheit,
    ("f", "c"): fahrenheit_to_celsius,
    ("c", "k"): celsius_to_kelvin,
    ("k", "c"): kelvin_to_celsius,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value between two units.

    Example: convert(10, "km", "miles")
    Supported units: km, miles, kg, pounds, m, ft, c, f, k
    """
    key = (from_unit.lower(), to_unit.lower())
    if key not in _CONVERTERS:
        supported = ", ".join(f"{a}->{b}" for a, b in _CONVERTERS)
        raise ValueError(
            f"Unsupported conversion '{from_unit}' -> '{to_unit}'. "
            f"Supported: {supported}"
        )
    return _CONVERTERS[key](value)


# ---------- Interactive mode ----------
def run_converter():
    """Simple loop: type '10 km miles' to convert, 'q' to quit."""
    print("\n=== Unit Converter ===")
    print("Units: km, miles, kg, pounds, m, ft, c, f, k")
    while True:
        text = input("\nEnter '<value> <from> <to>' (or q to quit): ").strip()
        if text.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        parts = text.split()
        if len(parts) != 3:
            print("Format: <value> <from_unit> <to_unit>, e.g. 10 km miles")
            continue
        value_text, from_unit, to_unit = parts
        try:
            result = convert(float(value_text), from_unit, to_unit)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"{value_text} {from_unit} = {result:.2f} {to_unit}")


# This block ONLY runs when custom_module.py is executed directly,
# NOT when it's imported by another file (like module_demo.py).
if __name__ == "__main__":
    print("Running custom_module.py directly - testing functions:")
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"70 kg = {kg_to_pounds(70):.2f} pounds")
    print(f"25 C = {celsius_to_fahrenheit(25):.2f} F")
    print(f"Area of circle (radius 5) = {circle_area(5):.2f}")
    print(f"Circumference of circle (radius 5) = {circle_circumference(5):.2f}")
    run_converter()
