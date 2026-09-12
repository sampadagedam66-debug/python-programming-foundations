"""
text_file_write.py

Topic: Writing to Text Files in Python
Covers: write mode 'w' | append mode 'a' | writing multiple lines
"""

# ---------------------------------------------------------
# SECTION 1: Write Mode ('w') — Daily Journal Entry
# ---------------------------------------------------------
print("---- Write Mode: Daily Journal Entry ----")

# 'w' mode creates the file if it doesn't exist, and OVERWRITES it if it does
with open("journal.txt", "w") as journal_file:
    journal_file.write("Today I learned how file handling works in Python.\n")
    journal_file.write("It felt confusing at first, but writing to a file is simple.\n")

print("Journal entry written to journal.txt")


# ---------------------------------------------------------
# SECTION 2: Append Mode ('a') — Expense Log
# ---------------------------------------------------------
print("\n---- Append Mode: Expense Log ----")

# 'a' mode adds to the end of the file without erasing existing content
with open("expenses.txt", "a") as expense_file:
    expense_file.write("Groceries: Rs 850\n")

with open("expenses.txt", "a") as expense_file:
    expense_file.write("Bus fare: Rs 40\n")

print("Expense entries appended to expenses.txt (run this file multiple times to see it grow)")


# ---------------------------------------------------------
# SECTION 3: Writing Multiple Lines — Trip Packing Checklist
# ---------------------------------------------------------
print("\n---- Multiple Lines: Trip Packing Checklist ----")

packing_items = [
    "Passport\n",
    "Phone charger\n",
    "Two pairs of clothes\n",
    "Toothbrush\n",
]

with open("packing_checklist.txt", "w") as checklist_file:
    checklist_file.writelines(packing_items)

print("Packing checklist written to packing_checklist.txt")
