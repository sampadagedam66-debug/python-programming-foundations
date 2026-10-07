"""
functions.py

Topic: Functions in Python

Covers:
1. Function definition and parameters
2. Default arguments
3. *args
4. **kwargs
5. Multiple return values
6. Mini project using functions
"""


# =========================================================
# SECTION 1: Function Definition and Parameters
# Bus Ticket Calculator
# =========================================================

print("\n===== BUS TICKET CALCULATOR =====")


def calculate_ticket_price(distance, passenger_type):
    rate = 2.5
    fare = distance * rate

    if passenger_type == "child":
        fare = fare * 0.5
    elif passenger_type == "student":
        fare = fare * 0.8

    return fare


# Get valid distance
while True:
    try:
        distance = float(input("Enter travel distance (km): "))

        if distance > 0:
            break
        else:
            print("Distance must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


passenger_type = input(
    "Enter passenger type (adult/child/student): "
).strip().lower()


if passenger_type in ["adult", "child", "student"]:
    ticket_price = calculate_ticket_price(distance, passenger_type)

    print("\n--- Ticket Details ---")
    print(f"Distance       : {distance:.1f} km")
    print(f"Passenger Type : {passenger_type}")
    print(f"Ticket Price   : Rs {ticket_price:.2f}")

else:
    print("Invalid passenger type.")


# =========================================================
# SECTION 2: Default Arguments
# Gym Membership Calculator
# =========================================================

print("\n===== GYM MEMBERSHIP =====")


def calculate_membership_fee(months, monthly_fee=1200):
    total = months * monthly_fee

    if months >= 6:
        total = total * 0.90

    return total


while True:
    try:
        months = int(input("Enter membership duration (months): "))

        if months > 0:
            break
        else:
            print("Months must be greater than 0.")

    except ValueError:
        print("Please enter a whole number.")


membership_fee = calculate_membership_fee(months)

print("\n--- Membership Details ---")
print(f"Duration : {months} months")
print(f"Total Fee: Rs {membership_fee:.2f}")

if months >= 6:
    print("You received a 10% discount!")


# =========================================================
# SECTION 3: *args
# Student Marks Average
# =========================================================

print("\n===== STUDENT MARKS =====")


def calculate_average(*marks):
    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


while True:
    try:
        number_of_subjects = int(input("Enter number of subjects: "))

        if number_of_subjects > 0:
            break
        else:
            print("Number of subjects must be greater than 0.")

    except ValueError:
        print("Please enter a whole number.")


marks = []

for i in range(number_of_subjects):

    while True:
        try:
            mark = float(input(f"Enter marks for subject {i + 1}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


average = calculate_average(*marks)

print("\n--- Result ---")
print(f"Total Subjects : {number_of_subjects}")
print(f"Average Marks  : {average:.2f}")

if average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")


# =========================================================
# SECTION 4: **kwargs
# Student Profile
# =========================================================

print("\n===== STUDENT PROFILE =====")


def create_student_profile(**details):
    print("\n--- Student Information ---")

    for key, value in details.items():
        print(f"{key.capitalize()} : {value}")


name = input("Enter your name: ").strip()
branch = input("Enter your branch: ").strip()
year = input("Enter your year: ").strip()
city = input("Enter your city: ").strip()


create_student_profile(
    name=name,
    branch=branch,
    year=year,
    city=city
)


# =========================================================
# SECTION 5: Multiple Return Values
# Temperature Converter
# =========================================================

print("\n===== TEMPERATURE CONVERTER =====")


def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    return fahrenheit, kelvin


while True:
    try:
        celsius = float(input("Enter temperature in Celsius: "))

        if celsius >= -273.15:
            break
        else:
            print("Temperature cannot be below -273.15 C.")

    except ValueError:
        print("Please enter a valid number.")


fahrenheit, kelvin = convert_temperature(celsius)

print("\n--- Temperature ---")
print(f"Celsius    : {celsius:.2f} C")
print(f"Fahrenheit : {fahrenheit:.2f} F")
print(f"Kelvin     : {kelvin:.2f} K")


# =========================================================
# SECTION 6: Mini Project
# Currency Converter
# =========================================================

print("\n===== CURRENCY CONVERTER =====")


exchange_rates = {
    "USD": 83.2,
    "EUR": 90.5,
    "GBP": 105.8
}


def convert_to_inr(amount, currency):
    if currency not in exchange_rates:
        return None

    return amount * exchange_rates[currency]


def show_currency_result(amount, currency, result):
    if result is None:
        print("Sorry, this currency is not supported.")
    else:
        print(f"\n{amount:.2f} {currency} = Rs {result:.2f}")


while True:
    try:
        amount = float(input("Enter amount: "))

        if amount > 0:
            break
        else:
            print("Amount must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


currency = input(
    "Enter currency (USD/EUR/GBP): "
).strip().upper()


converted_amount = convert_to_inr(amount, currency)

show_currency_result(
    amount,
    currency,
    converted_amount
)


print("\n===== PROGRAM COMPLETED =====")
