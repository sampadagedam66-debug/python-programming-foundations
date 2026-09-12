"""
csv_write.py

Topic: Writing CSV Files in Python
Covers: csv.writer basics | writing with a header row | csv.DictWriter
"""

import csv

# ---------------------------------------------------------
# SECTION 1: csv.writer Basics — Cricket Squad List
# ---------------------------------------------------------
print("---- csv.writer: Cricket Squad List ----")

squad_members = [
    ["Player Name", "Role"],
    ["Rohit Verma", "Batsman"],
    ["Kunal Shah", "Bowler"],
    ["Arjun Rao", "All-Rounder"],
]

with open("cricket_squad.csv", "w", newline="") as squad_file:
    csv_writer = csv.writer(squad_file)
    for row in squad_members:
        csv_writer.writerow(row)

print("Squad list written to cricket_squad.csv")


# ---------------------------------------------------------
# SECTION 2: Writing With a Header Row — Store Product List
# ---------------------------------------------------------
print("\n---- Header Row: Store Product List ----")

with open("store_products.csv", "w", newline="") as product_file:
    csv_writer = csv.writer(product_file)
    csv_writer.writerow(["Product", "Price", "Quantity"])   # header row
    csv_writer.writerow(["Notebook", 45, 100])
    csv_writer.writerow(["Pen", 10, 250])
    csv_writer.writerow(["Eraser", 5, 150])

print("Product list written to store_products.csv")


# ---------------------------------------------------------
# SECTION 3: csv.DictWriter — Event Registration List
# ---------------------------------------------------------
print("\n---- DictWriter: Event Registration ----")

registrations = [
    {"name": "Neha Joshi", "city": "Pune", "ticket_type": "VIP"},
    {"name": "Farhan Ali", "city": "Mumbai", "ticket_type": "General"},
    {"name": "Divya Menon", "city": "Pune", "ticket_type": "General"},
]

field_names = ["name", "city", "ticket_type"]

with open("event_registrations.csv", "w", newline="") as registration_file:
    dict_writer = csv.DictWriter(registration_file, fieldnames=field_names)
    dict_writer.writeheader()          # writes the header automatically
    for entry in registrations:
        dict_writer.writerow(entry)

print("Registrations written to event_registrations.csv")
