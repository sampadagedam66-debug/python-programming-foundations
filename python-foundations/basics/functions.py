"""
functions.py

Topic: Functions in Python
Covers: function definition & parameters | default arguments |
        *args (variable-length arguments) | **kwargs & multiple return values
Mini use-case: a simple currency converter tool
"""

# ---------------------------------------------------------
# SECTION 1: Function Definition & Parameters — Bus Ticket Pricing
# ---------------------------------------------------------
print("---- Function Definition & Parameters: Bus Ticket Pricing ----")

def calculate_ticket_price(distance_km, passenger_type):
    rate_per_km = 2.5
    base_fare = distance_km * rate_per_km

    if passenger_type == "child":
        return base_fare * 0.5  # children pay half fare
    return base_fare


adult_fare = calculate_ticket_price(40, "adult")
child_fare = calculate_ticket_price(40, "child")
print(f"Adult fare for 40km: Rs {adult_fare:.2f}")
print(f"Child fare for 40km: Rs {child_fare:.2f}")


# ---------------------------------------------------------
# SECTION 2: Default Arguments — Gym Membership Fee
# ---------------------------------------------------------
print("\n---- Default Arguments: Gym Membership Fee ----")

def calculate_membership_fee(monthly_rate, duration_months=1):
    total = monthly_rate * duration_months
    if duration_months >= 6:
        total *= 0.9  # 10% discount for 6+ months
    return total


single_month_fee = calculate_membership_fee(1200)               # uses default duration
six_month_fee = calculate_membership_fee(1200, duration_months=6)  # overrides default
print(f"1 month (default): Rs {single_month_fee:.2f}")
print(f"6 months (with discount): Rs {six_month_fee:.2f}")


# ---------------------------------------------------------
# SECTION 3: *args — Exam Score Averaging
# ---------------------------------------------------------
print("\n---- *args: Exam Score Averaging ----")

def calculate_average_score(*scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


student_a_avg = calculate_average_score(85, 90, 78)          # 3 subjects
student_b_avg = calculate_average_score(70, 88, 95, 60, 82)   # 5 subjects
print(f"Student A average (3 subjects): {student_a_avg:.2f}")
print(f"Student B average (5 subjects): {student_b_avg:.2f}")


# ---------------------------------------------------------
# SECTION 4: **kwargs & Multiple Return Values
# ---------------------------------------------------------
print("\n---- **kwargs: College Profile Builder ----")

def build_student_profile(**details):
    print("Student Profile:")
    for field_name, field_value in details.items():
        print(f"  {field_name}: {field_value}")


build_student_profile(name="Ananya Rao", branch="CSE", year=1, city="Pune")

print("\n---- Multiple Return Values: Temperature Converter ----")

def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin  # returns a tuple of two values


temp_f, temp_k = convert_temperature(30)
print(f"30C = {temp_f:.2f}F = {temp_k:.2f}K")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Currency Converter Tool
# ---------------------------------------------------------
# Combines multiple small functions working together, a different
# domain from every section above.

print("\n---- Mini Project: Currency Converter Tool ----")

EXCHANGE_RATES = {
    "USD": 83.2,
    "EUR": 90.5,
    "GBP": 105.8,
}


def convert_to_inr(amount, currency_code):
    if currency_code not in EXCHANGE_RATES:
        return None
    rate = EXCHANGE_RATES[currency_code]
    return amount * rate


def format_currency_result(amount, currency_code, converted_amount):
    if converted_amount is None:
        return f"Currency '{currency_code}' is not supported."
    return f"{amount} {currency_code} = Rs {converted_amount:.2f}"


amount_to_convert = float(input("Enter amount to convert: "))
currency_code_input = input("Enter currency code (USD/EUR/GBP): ").strip().upper()

converted_value = convert_to_inr(amount_to_convert, currency_code_input)
result_message = format_currency_result(amount_to_convert, currency_code_input, converted_value)
print(result_message)
