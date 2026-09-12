"""
text_file_read.py

Topic: Reading Text Files in Python
Covers: .read() | .readline() vs .readlines() | looping over a file with 'for'

Note: run text_file_write.py first, since this file reads
journal.txt and packing_checklist.txt created by it.
"""

# ---------------------------------------------------------
# SECTION 1: .read() — Reading a Saved Note in Full
# ---------------------------------------------------------
print("---- .read(): Journal Entry ----")

with open("journal.txt", "r") as journal_file:
    full_content = journal_file.read()

print("Full journal content:")
print(full_content)


# ---------------------------------------------------------
# SECTION 2: .readline() vs .readlines() — Recipe Steps
# ---------------------------------------------------------
print("---- .readline() vs .readlines(): Recipe Steps ----")

# create a small recipe file first so this section can read it
with open("recipe.txt", "w") as recipe_file:
    recipe_file.write("Step 1: Boil water\n")
    recipe_file.write("Step 2: Add pasta\n")
    recipe_file.write("Step 3: Cook for 10 minutes\n")

with open("recipe.txt", "r") as recipe_file:
    first_step = recipe_file.readline()   # reads just ONE line
    print(f"First step only: {first_step.strip()}")

with open("recipe.txt", "r") as recipe_file:
    all_steps = recipe_file.readlines()   # reads ALL lines into a list
    print(f"All steps as a list: {all_steps}")


# ---------------------------------------------------------
# SECTION 3: Looping Over a File — Class Attendance List
# ---------------------------------------------------------
print("\n---- Looping Over File: Class Attendance ----")

# create an attendance file first
with open("attendance.txt", "w") as attendance_file:
    attendance_file.write("Aman - Present\n")
    attendance_file.write("Priya - Absent\n")
    attendance_file.write("Rohit - Present\n")
    attendance_file.write("Sneha - Present\n")

present_count = 0

with open("attendance.txt", "r") as attendance_file:
    for line in attendance_file:
        print(line.strip())
        if "Present" in line:
            present_count += 1

print(f"\nTotal students present: {present_count}")
