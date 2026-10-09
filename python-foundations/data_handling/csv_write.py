"""
csv_write.py
Topic: Data Handling - Writing CSV files

Covers:
1. Write mode "w" (new file / overwrite) and append mode "a" (add rows)
2. csv.DictWriter - write dictionaries  (writeheader, writerows)
3. csv.writer     - write lists         (writerow)
4. Checking the input before saving it
5. Reading the file back to confirm it was saved

Run the file and type your answers when asked.
The files it creates can be opened with csv_read.py.
Tip: try a name like  Rao, Asha  - the csv module adds quotes automatically.
"""

import csv
import os
import sys

FIELDS = ["name", "roll_no", "branch", "maths", "science", "english"]


def read_whole(prompt):
    """Keep asking until a whole number is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def read_mark(prompt):
    """Keep asking until a mark between 0 and 100 is entered."""
    while True:
        try:
            mark = float(input(prompt))
        except ValueError:
            print("  Please enter a number.")
            continue

        if 0 <= mark <= 100:
            if mark.is_integer():
                return int(mark)        # save 85 instead of 85.0
            return mark
        print("  Marks must be between 0 and 100.")


def show_file(name):
    """Read a CSV file and print it in neat columns."""
    print("\n--- CONTENTS OF", name, "---")
    with open(name, newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            for value in row:
                print(f"{value:<12}", end="")
            print()


print("===== CSV WRITER =====")

# ---------------------------------------------------
# 1. CHOOSE THE FILE AND THE MODE
# ---------------------------------------------------
filename = input("Enter file name to save (press Enter for new_students.csv): ").strip()
if filename == "":
    filename = "new_students.csv"
if not filename.endswith(".csv"):
    filename += ".csv"

mode = "w"                  # "w" = create a new file (or overwrite)
write_header = True

if os.path.exists(filename):
    print("\n" + filename, "already exists.")
    choice = input("Type A to add rows, or W to overwrite it: ").strip().lower()

    if choice == "a":
        mode = "a"          # "a" = append rows at the end
        write_header = False

        # the old file must have the same columns
        with open(filename, newline="", encoding="utf-8") as file:
            first_row = next(csv.reader(file), [])
        if first_row != FIELDS:
            print("The columns in that file are different. Nothing was changed.")
            sys.exit()
    elif choice == "w":
        sure = input("This will erase the old data. Are you sure? (yes/no): ").strip().lower()
        if sure != "yes":
            print("Cancelled. Nothing was changed.")
            sys.exit()
    else:
        print("Cancelled. Nothing was changed.")
        sys.exit()


# ---------------------------------------------------
# 2. COLLECT THE DATA
# ---------------------------------------------------
count = read_whole("\nHow many students do you want to add? ")
if count <= 0:
    print("Nothing to write.")
    sys.exit()

records = []                # a list of dictionaries

for number in range(1, count + 1):
    print("\nStudent", number)
    record = {
        "name": input("  Name: ").strip().title(),
        "roll_no": read_whole("  Roll number: "),
        "branch": input("  Branch: ").strip().upper(),
        "maths": read_mark("  Maths marks: "),
        "science": read_mark("  Science marks: "),
        "english": read_mark("  English marks: "),
    }
    records.append(record)


# ---------------------------------------------------
# 3. WRITE WITH csv.DictWriter  (dictionaries)
# ---------------------------------------------------
with open(filename, mode, newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=FIELDS)
    if write_header:
        writer.writeheader()        # the first row with column names
    writer.writerows(records)       # many rows at once

print("\n" + str(len(records)), "row(s) saved in", filename)


# ---------------------------------------------------
# 4. WRITE WITH csv.writer  (lists) - a summary file
# ---------------------------------------------------
base, extension = os.path.splitext(filename)
summary_file = base + "_summary" + extension

with open(summary_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "total", "average", "result"])     # one row

    for record in records:
        total = record["maths"] + record["science"] + record["english"]
        average = round(total / 3, 2)

        if average >= 40:
            result = "Pass"
        else:
            result = "Fail"

        writer.writerow([record["name"], total, average, result])

print("Summary of the new students saved in", summary_file)


# ---------------------------------------------------
# 5. READ THE FILES BACK
# ---------------------------------------------------
show_file(filename)
show_file(summary_file)

print("\nDone!")