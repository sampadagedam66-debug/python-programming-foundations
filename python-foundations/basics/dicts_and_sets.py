"""
dicts_and_sets.py

Topic: Dictionaries and Sets in Python
Covers: dict creation & basic operations | looping through dictionaries |
        nested dictionaries | sets & set operations
Mini use-case: an inventory stock tracker for a small shop
"""

# ---------------------------------------------------------
# SECTION 1: Dictionary Basics — Employee ID Card
# ---------------------------------------------------------
print("---- Dictionary Basics: Employee ID Card ----")

employee = {
    "id": "EMP1042",
    "name": "Ritika Verma",
    "department": "Software Engineering",
}

print(f"Employee record: {employee}")
print(f"Name: {employee['name']}")

employee["department"] = "Data Engineering"   # update existing key
employee["joining_year"] = 2024                # add new key
print(f"After update & add: {employee}")

# .get() avoids a crash if the key doesn't exist
manager_name = employee.get("manager", "Not Assigned")
print(f"Manager: {manager_name}")

employee.pop("joining_year")                    # remove a key
print(f"After removing joining_year: {employee}")


# ---------------------------------------------------------
# SECTION 2: Looping Through Dictionaries — Election Results
# ---------------------------------------------------------
print("\n---- Looping: Election Vote Count ----")

vote_count = {
    "Candidate A": 4520,
    "Candidate B": 6103,
    "Candidate C": 2890,
}

winner_name = ""
highest_votes = 0

for candidate, votes in vote_count.items():
    print(f"{candidate}: {votes} votes")
    if votes > highest_votes:
        highest_votes = votes
        winner_name = candidate

total_votes_cast = sum(vote_count.values())
print(f"\nTotal votes cast: {total_votes_cast}")
print(f"Winner: {winner_name} with {highest_votes} votes")


# ---------------------------------------------------------
# SECTION 3: Nested Dictionaries — Online Course Catalog
# ---------------------------------------------------------
print("\n---- Nested Dictionaries: Course Catalog ----")

course_catalog = {
    "python_basics": {
        "instructor": "Dr. Mehta",
        "duration_weeks": 6,
        "price": 1499,
    },
    "web_development": {
        "instructor": "Ms. Kapoor",
        "duration_weeks": 10,
        "price": 2999,
    },
}

python_course_instructor = course_catalog["python_basics"]["instructor"]
print(f"Python Basics instructor: {python_course_instructor}")

# updating a nested field
course_catalog["web_development"]["price"] = 2499
print(f"Updated Web Development price: {course_catalog['web_development']['price']}")

print(f"\nFull catalog: {course_catalog}")


# ---------------------------------------------------------
# SECTION 4: Sets & Set Operations — College Club Memberships
# ---------------------------------------------------------
print("\n---- Sets: College Club Memberships ----")

coding_club_members = {"Aman", "Priya", "Rohit", "Sneha"}
music_club_members = {"Rohit", "Neha", "Sneha", "Karan"}

members_in_both = coding_club_members & music_club_members       # intersection
all_unique_members = coding_club_members | music_club_members     # union
only_coding_club = coding_club_members - music_club_members       # difference

print(f"Coding Club: {coding_club_members}")
print(f"Music Club: {music_club_members}")
print(f"In both clubs: {members_in_both}")
print(f"All unique members across clubs: {all_unique_members}")
print(f"Only in Coding Club: {only_coding_club}")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Inventory Stock Tracker
# ---------------------------------------------------------
# A small dict-driven utility, a different domain from every
# section above, combining lookups, updates, and low-stock checks.

print("\n---- Mini Project: Shop Inventory Tracker ----")

LOW_STOCK_THRESHOLD = 5

inventory = {
    "Notebook": 12,
    "Pen": 4,
    "Eraser": 20,
    "Ruler": 3,
}

print("Current inventory:")
for product, quantity in inventory.items():
    print(f"  {product}: {quantity}")

print("\nLow stock alert:")
for product, quantity in inventory.items():
    if quantity < LOW_STOCK_THRESHOLD:
        print(f"  {product} is LOW ({quantity} left)")

product_to_restock = input("\nEnter a product name to restock: ")
restock_amount = int(input(f"Enter quantity to add for {product_to_restock}: "))

if product_to_restock in inventory:
    inventory[product_to_restock] += restock_amount
    print(f"Updated stock for {product_to_restock}: {inventory[product_to_restock]}")
else:
    inventory[product_to_restock] = restock_amount
    print(f"New product added: {product_to_restock} with stock {restock_amount}")
