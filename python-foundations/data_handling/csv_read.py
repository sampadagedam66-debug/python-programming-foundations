"""
csv_read.py

Topic: Reading CSV Files in Python
Covers: csv.reader basics | skipping header rows + calculation | csv.DictReader

Note: run csv_write.py first, since this file reads the CSVs it creates.
"""

import csv

# ---------------------------------------------------------
# SECTION 1: csv.reader Basics — Cricket Squad List
# ---------------------------------------------------------
print("---- csv.reader: Cricket Squad List ----")

with open("cricket_squad.csv", "r") as squad_file:
    csv_reader = csv.reader(squad_file)
    for row in csv_reader:
        print(row)


# ---------------------------------------------------------
# SECTION 2: Skipping Header + Calculation — Store Product List
# ---------------------------------------------------------
print("\n---- Header Handling: Store Product Value ----")

total_inventory_value = 0

with open("store_products.csv", "r") as product_file:
    csv_reader = csv.reader(product_file)
    header_row = next(csv_reader)   # reads and skips the header
    print(f"Header: {header_row}")

    for row in csv_reader:
        product_name, price, quantity = row
        item_value = float(price) * int(quantity)
        total_inventory_value += item_value
        print(f"{product_name}: Rs {item_value:.2f}")

print(f"\nTotal inventory value: Rs {total_inventory_value:.2f}")


# ---------------------------------------------------------
# SECTION 3: csv.DictReader — Event Registration Filtering
# ---------------------------------------------------------
print("\n---- DictReader: Filtering Pune Registrations ----")

pune_attendee_count = 0

with open("event_registrations.csv", "r") as registration_file:
    dict_reader = csv.DictReader(registration_file)
    for entry in dict_reader:
        print(f"{entry['name']} - {entry['city']} - {entry['ticket_type']}")
        if entry["city"] == "Pune":
            pune_attendee_count += 1

print(f"\nTotal attendees from Pune: {pune_attendee_count}")
