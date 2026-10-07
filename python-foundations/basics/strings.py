"""
strings.py
Topic: Strings in Python
"""


# 1. Number Plate
def number_plate():
    print("\n--- NUMBER PLATE ---")

    plate = input("Enter vehicle number plate: ").upper().strip()

    if len(plate) >= 8 and plate[:2].isalpha() and plate[2:4].isdigit():
        print("Full Plate:", plate)
        print("State Code:", plate[:2])
        print("District Code:", plate[2:4])
        print("Series Code:", plate[4:6])
        print("Number:", plate[6:])
        print("Last Character:", plate[-1])
    else:
        print("Invalid plate! Example: MH12AB1234")


# 2. Email Cleanup
def email_cleanup():
    print("\n--- EMAIL CLEANUP ---")

    email = input("Enter your email: ").strip().lower()

    if email.count("@") == 1:
        parts = email.split("@")
        print("Clean Email:", email)
        print("Username:", parts[0])
        print("Domain:", parts[1])
        print("Email again:", "@".join(parts))
    else:
        print("Invalid email! Enter exactly one @.")


# 3. Shopping Receipt
def shopping_receipt():
    print("\n--- SHOPPING RECEIPT ---")

    item = input("Enter item name: ")

    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Price must be positive and quantity must be greater than 0.")
            return

        total = price * quantity

        print(f"\n{item:<20} Rs {price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total:    Rs {total:.2f}")

    except ValueError:
        print("Please enter a valid price and quantity.")


# 4. Password Strength
def password_checker():
    print("\n--- PASSWORD CHECKER ---")

    password = input("Enter a password: ")

    if not password:
        print("Password cannot be empty.")
        return

    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_space = " " in password

    score = sum([has_letter, has_digit, has_upper, len(password) >= 8])

    if has_space:
        strength = "Weak"
    elif score == 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    print("Has letters:", has_letter)
    print("Has digits:", has_digit)
    print("Has uppercase:", has_upper)
    print("Password strength:", strength)


# 5. Movie Ticket
def movie_ticket():
    print("\n--- MOVIE TICKET ---")

    movie = input("Enter movie name: ").strip().title()
    movie = " ".join(movie.split())

    seat = input("Enter seat number: ").upper()
    time = input("Enter show time: ")

    print("\n🎬 BOOKING CONFIRMED!")
    print(f"Movie: {movie}")
    print(f"Seat: {seat}")
    print(f"Show Time: {time}")
    print("🎉 Enjoy your movie!")


# Run all sections
number_plate()
email_cleanup()
shopping_receipt()
password_checker()
movie_ticket()
