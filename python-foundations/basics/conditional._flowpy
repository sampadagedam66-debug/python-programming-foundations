"""
control_flow.py

Topic: Control Flow in Python
Covers: if / elif / else | comparison & logical operators |
        for loop | while loop | break & continue
Mini use-case: a cab ride fare calculator with surge pricing and loyalty discount
"""

# ---------------------------------------------------------
# SECTION 1: if / elif / else — Smart Thermostat Decision
# ---------------------------------------------------------
print("---- If / Elif / Else: Smart Thermostat ----")

current_temp = int(input("Enter current room temperature (C): "))
target_temp = int(input("Enter target temperature (C): "))
temp_difference = current_temp - target_temp

if temp_difference > 3:
    action = "COOLER ON (High Speed)"
elif temp_difference > 0:
    action = "COOLER ON (Low Speed)"
elif temp_difference < -3:
    action = "HEATER ON (High Power)"
elif temp_difference < 0:
    action = "HEATER ON (Low Power)"
else:
    action = "SYSTEM IDLE"

print(f"Current: {current_temp}C, Target: {target_temp}C -> Action: {action}")


# ---------------------------------------------------------
# SECTION 2: Logical operators — ATM Withdrawal Eligibility
# ---------------------------------------------------------
print("\n---- Logical Operators: ATM Withdrawal Check ----")

DAILY_LIMIT = 25000

account_balance = float(input("Enter account balance: Rs "))
withdrawal_amount = float(input("Enter amount to withdraw: Rs "))
already_withdrawn_today = float(input("Enter amount already withdrawn today: Rs "))
is_card_blocked = input("Is the card blocked? (y/n): ").strip().lower() == "y"

has_sufficient_balance = withdrawal_amount <= account_balance
within_daily_limit = (already_withdrawn_today + withdrawal_amount) <= DAILY_LIMIT

# 'and' requires both conditions, 'not' flips the blocked-card check
can_withdraw = has_sufficient_balance and within_daily_limit and not is_card_blocked

print(f"Sufficient balance: {has_sufficient_balance}")
print(f"Within daily limit: {within_daily_limit}")
print(f"Card blocked: {is_card_blocked}")
print(f"Final decision - Withdrawal allowed: {can_withdraw}")


# ---------------------------------------------------------
# SECTION 3: for loop — SIP Investment Growth Simulation
# ---------------------------------------------------------
print("\n---- For Loop: SIP Investment Growth ----")

monthly_investment = float(input("Enter monthly SIP amount: Rs "))
annual_interest_rate = float(input("Enter expected annual return rate (%): "))
investment_years = int(input("Enter investment duration in years: "))

monthly_rate = annual_interest_rate / 12 / 100
total_months = investment_years * 12
balance = 0.0

print("\nYear-wise growth:")
for month in range(1, total_months + 1):
    balance = (balance + monthly_investment) * (1 + monthly_rate)
    if month % 12 == 0:
        completed_years = month // 12
        print(f"After year {completed_years}: Rs {balance:.2f}")

print(f"\nFinal maturity value after {investment_years} years: Rs {balance:.2f}")


# ---------------------------------------------------------
# SECTION 4: while loop + break + continue — Smart Parking System
# ---------------------------------------------------------
print("\n---- While Loop: Smart Parking System ----")

TOTAL_SLOTS = 5
occupied_slots = 0

print(f"Parking system online. Total slots: {TOTAL_SLOTS}")
print("Enter 1 for car entry, 2 for car exit, -1 to close the gate for the day.")

while True:
    entry_choice = int(input("Your choice: "))

    if entry_choice == -1:
        print("Gate closed for the day.")
        break  # exits the loop immediately

    if entry_choice == 1:
        if occupied_slots >= TOTAL_SLOTS:
            print("Parking full! Entry denied.")
            continue  # skip rest of loop, ask again
        occupied_slots += 1
        print(f"Car entered. Occupied: {occupied_slots}/{TOTAL_SLOTS}")

    elif entry_choice == 2:
        if occupied_slots <= 0:
            print("No cars currently parked.")
            continue
        occupied_slots -= 1
        print(f"Car exited. Occupied: {occupied_slots}/{TOTAL_SLOTS}")

    else:
        print("Invalid choice, please enter 1, 2, or -1.")
        continue


# ---------------------------------------------------------
# SECTION 5: Mini Project — Cab Fare Calculator with Surge Pricing
# ---------------------------------------------------------
# Combines everything above: conditional surge pricing, logical
# eligibility for a loyalty discount, and a validated while loop
# across multiple trip segments.

print("\n---- Mini Project: Cab Fare Calculator ----")

BASE_FARE = 50
RATE_PER_KM = 12
TOTAL_TRIPS = 2

ride_hour = int(input("Enter current hour of day (0-23): "))
is_peak_hour = (ride_hour >= 8 and ride_hour <= 10) or (ride_hour >= 18 and ride_hour <= 20)
surge_multiplier = 1.5 if is_peak_hour else 1.0

is_loyalty_member = input("Are you a loyalty member? (y/n): ").strip().lower() == "y"
loyalty_discount_rate = 0.10 if is_loyalty_member else 0.0

trip_number = 1
grand_total = 0.0

while trip_number <= TOTAL_TRIPS:
    distance_km = float(input(f"Enter distance for trip {trip_number} in km: "))

    if distance_km <= 0:
        print("Invalid distance, please enter a positive number.")
        continue  # re-ask for the same trip, don't advance

    fare = (BASE_FARE + distance_km * RATE_PER_KM) * surge_multiplier
    discount_amount = fare * loyalty_discount_rate
    final_fare = fare - discount_amount

    print(f"Trip {trip_number}: {distance_km} km -> Rs {final_fare:.2f}")
    grand_total += final_fare
    trip_number += 1

print("\n----- RIDE SUMMARY -----")
print(f"Peak Hour Surge Applied: {is_peak_hour}")
print(f"Loyalty Discount Applied: {is_loyalty_member}")
print(f"Total Fare for {TOTAL_TRIPS} trips: Rs {grand_total:.2f}")
