"""
strings.py

Topic: Strings in Python
Covers: indexing & slicing | string methods (case, strip, replace, split, join) |
        f-strings & formatting | string checking methods
Mini use-case: a movie name formatter for a ticket booking display
"""

# ---------------------------------------------------------
# SECTION 1: Indexing & Slicing — Vehicle Number Plate Parser
# ---------------------------------------------------------
print("---- Indexing & Slicing: Number Plate Parser ----")

number_plate = "MH12AB1234"

state_code = number_plate[0:2]     # MH
district_code = number_plate[2:4]  # 12
series_code = number_plate[4:6]    # AB
unique_number = number_plate[6:]   # 1234
last_char = number_plate[-1]       # last digit using negative indexing

print(f"Full Plate: {number_plate}")
print(f"State Code: {state_code}")
print(f"District Code: {district_code}")
print(f"Series Code: {series_code}")
print(f"Unique Number: {unique_number}")
print(f"Last Character: {last_char}")


# ---------------------------------------------------------
# SECTION 2: String Methods — Email Address Cleanup
# ---------------------------------------------------------
print("\n---- String Methods: Email Cleanup ----")

raw_email = "   RahulSharma99@GMAIL.com   "

cleaned_email = raw_email.strip().lower()
username_part, domain_part = cleaned_email.split("@")
corrected_email = cleaned_email.replace("gmail", "gmail")  # placeholder for real fixes

print(f"Raw Email: '{raw_email}'")
print(f"Cleaned Email: '{cleaned_email}'")
print(f"Username Part: {username_part}")
print(f"Domain Part: {domain_part}")

# join is the reverse of split — combining parts back together
rebuilt_email = "@".join([username_part, domain_part])
print(f"Rebuilt Email: {rebuilt_email}")


# ---------------------------------------------------------
# SECTION 3: f-strings & Formatting — Restaurant Order Receipt
# ---------------------------------------------------------
print("\n---- f-strings & Formatting: Restaurant Receipt ----")

item_1, price_1 = "Paneer Butter Masala", 220.5
item_2, price_2 = "Butter Naan", 45.0
item_3, price_3 = "Cold Coffee", 90.75

print(f"{item_1:.<25}{price_1:.>8.2f}")
print(f"{item_2:.<25}{price_2:.>8.2f}")
print(f"{item_3:.<25}{price_3:.>8.2f}")

total = price_1 + price_2 + price_3
print(f"{'TOTAL':.<25}{total:.>8.2f}")


# ---------------------------------------------------------
# SECTION 4: String Checking Methods — Password Rule Checker
# ---------------------------------------------------------
print("\n---- String Checking Methods: Password Rules ----")

password = "Secure123"

has_letters = any(character.isalpha() for character in password)
has_digits = any(character.isdigit() for character in password)
starts_with_upper = password[0].isupper()
contains_space = " " in password
ends_with_digit = password[-1].isdigit()

print(f"Password: {password}")
print(f"Has letters: {has_letters}")
print(f"Has digits: {has_digits}")
print(f"Starts with uppercase: {starts_with_upper}")
print(f"Contains space: {contains_space}")
print(f"Ends with digit: {ends_with_digit}")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Movie Name Formatter
# ---------------------------------------------------------
# Combines cleanup, formatting, and string checks into one small tool,
# a different domain from every section above.

print("\n---- Mini Project: Movie Ticket Booking Formatter ----")

raw_title = "   the DARK knight    "

# clean and convert to title case for display
formatted_title = raw_title.strip().title()

# collapse any accidental multiple spaces left inside the title
formatted_title = " ".join(formatted_title.split())

seat_number = "G14"
show_time = "7:30 PM"

booking_message = (
    f"Booking Confirmed!\n"
    f"Movie: {formatted_title}\n"
    f"Seat: {seat_number} | Show Time: {show_time}"
)

print(f"Raw Title: '{raw_title}'")
print(f"Formatted Title: '{formatted_title}'")
print("\n" + booking_message)
