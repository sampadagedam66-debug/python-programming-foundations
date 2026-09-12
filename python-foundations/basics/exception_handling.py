"""
exception_handling.py

Topic: Exception Handling in Python
Covers: try/except basics | try/except/else/finally | catching multiple
        specific exceptions | raising custom exceptions
Mini use-case: a restaurant table booking system with input validation
"""

# ---------------------------------------------------------
# SECTION 1: try/except Basics — Movie Ticket Quantity
# ---------------------------------------------------------
print("---- try/except: Movie Ticket Quantity ----")

ticket_input = input("Enter number of movie tickets to book: ")

try:
    ticket_count = int(ticket_input)
    print(f"Booking {ticket_count} ticket(s).")
except ValueError:
    print(f"'{ticket_input}' is not a valid number. Booking cancelled.")


# ---------------------------------------------------------
# SECTION 2: try/except/else/finally — Loading Settings File
# ---------------------------------------------------------
print("\n---- try/except/else/finally: Settings Loader ----")

# create a settings file first so this section has something to load
with open("app_settings.txt", "w") as settings_file:
    settings_file.write("theme=dark\nvolume=80\n")

try:
    settings_file = open("app_settings.txt", "r")
except FileNotFoundError:
    print("Settings file not found. Using default settings.")
else:
    # 'else' runs ONLY if the try block succeeded with no exception
    print("Settings file loaded successfully:")
    print(settings_file.read())
    settings_file.close()
finally:
    # 'finally' ALWAYS runs, whether an exception happened or not
    print("Settings load attempt complete.")


# ---------------------------------------------------------
# SECTION 3: Catching Multiple Specific Exceptions — Simple Calculator
# ---------------------------------------------------------
print("\n---- Multiple Exceptions: Simple Calculator ----")

numerator_input = input("Enter numerator: ")
denominator_input = input("Enter denominator: ")

try:
    numerator = float(numerator_input)
    denominator = float(denominator_input)
    result = numerator / denominator
    print(f"Result: {result}")
except ValueError:
    print("Both inputs must be valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ---------------------------------------------------------
# SECTION 4: Raising Custom Exceptions — Driving License Age Check
# ---------------------------------------------------------
print("\n---- Raising Exceptions: Driving License Age Check ----")

def verify_driving_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age seems unrealistic, please check the entry.")
    if age < 18:
        raise ValueError("Applicant must be at least 18 years old to apply.")
    return True


age_input = input("Enter applicant's age: ")

try:
    applicant_age = int(age_input)
    verify_driving_age(applicant_age)
    print("Applicant is eligible to apply for a driving license.")
except ValueError as error:
    print(f"Application rejected: {error}")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Restaurant Table Booking System
# ---------------------------------------------------------
# Combines everything above: input validation, multiple exception
# types, and a custom check — a different domain from every
# section above.

print("\n---- Mini Project: Restaurant Table Booking ----")

MAX_TABLE_SIZE = 10


def validate_party_size(size):
    if size <= 0:
        raise ValueError("Party size must be at least 1.")
    if size > MAX_TABLE_SIZE:
        raise ValueError(f"We can only accommodate up to {MAX_TABLE_SIZE} guests per table.")
    return True


party_size_input = input(f"Enter number of guests (1-{MAX_TABLE_SIZE}): ")
booking_time_input = input("Enter booking hour (0-23): ")

try:
    party_size = int(party_size_input)
    booking_hour = int(booking_time_input)

    validate_party_size(party_size)

    if booking_hour < 0 or booking_hour > 23:
        raise ValueError("Booking hour must be between 0 and 23.")

except ValueError as error:
    print(f"Booking failed: {error}")
else:
    print(f"Table booked for {party_size} guest(s) at {booking_hour}:00.")
finally:
    print("Booking attempt finished.")
