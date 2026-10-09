"""
csv_read.py
Topic: Data Handling - Reading CSV files

Covers:
1. Opening a file safely with  with open()  and  try/except
2. csv.reader      - every row comes as a list
3. csv.DictReader  - every row comes as a dictionary
4. Converting text to numbers and skipping bad values
5. Simple statistics (total, average, highest, lowest)
6. Searching and filtering the data

Keep students.csv in the same folder, then run the file
and type your answers when asked.
"""

import csv
import sys


def show_table(header, rows):
    """Print the rows in neat columns."""
    for name in header:
        print(f"{name:<12}", end="")
    print()
    print("-" * 12 * len(header))

    for row in rows:
        for value in row:
            print(f"{value:<12}", end="")
        print()


print("===== CSV READER =====")

# ---------------------------------------------------
# 1. CHOOSE THE FILE
# ---------------------------------------------------
filename = input("Enter CSV file name (press Enter for students.csv): ").strip()
if filename == "":
    filename = "students.csv"

delimiter = input("Enter delimiter (press Enter for comma): ")
if delimiter == "":
    delimiter = ","


# ---------------------------------------------------
# 2. READ WITH csv.reader  (rows are lists)
# ---------------------------------------------------
try:
    # utf-8-sig also handles files saved from Excel
    with open(filename, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, delimiter=delimiter))
except FileNotFoundError:
    print("File not found:", filename)
    sys.exit()

if len(rows) < 2:
    print("The file has no data rows.")
    sys.exit()

header = rows[0]            # the first row has the column names
data = []
for row in rows[1:]:
    if row:                 # skip empty lines
        data.append(row)

print("\nColumns:", header)
print("Rows   :", len(data))

print("\nFirst 5 rows:")
show_table(header, data[:5])


# ---------------------------------------------------
# 3. READ WITH csv.DictReader  (rows are dictionaries)
# ---------------------------------------------------
with open(filename, newline="", encoding="utf-8-sig") as file:
    records = list(csv.DictReader(file, delimiter=delimiter))

print("\nFirst record as a dictionary:")
print(records[0])
print(header[0], "of first record:", records[0][header[0]])


# ---------------------------------------------------
# 4. NUMBERS AND STATISTICS
# ---------------------------------------------------
print("\n--- STATISTICS ---")
column = input("Enter a column that has numbers " + str(header) + ": ").strip()

if column not in header:
    print("Column not found.")
else:
    pairs = []              # (label, number) for every valid row
    skipped = 0

    for record in records:
        try:
            number = float(record[column])
            pairs.append((record[header[0]], number))
        except (ValueError, TypeError):
            skipped += 1    # empty or text values such as N/A

    if pairs:
        total = sum(pair[1] for pair in pairs)
        highest = lowest = pairs[0]
        for pair in pairs:
            if pair[1] > highest[1]:
                highest = pair
            if pair[1] < lowest[1]:
                lowest = pair

        print("\nValid rows :", len(pairs))
        print("Skipped    :", skipped)
        print("Total      :", total)
        print("Average    :", round(total / len(pairs), 2))
        print("Highest    :", highest[0], "->", highest[1])
        print("Lowest     :", lowest[0], "->", lowest[1])
    else:
        print("No numbers found in that column.")


# ---------------------------------------------------
# 5. SEARCH
# ---------------------------------------------------
print("\n--- SEARCH ---")

while True:
    keyword = input("Enter a word to search (press Enter to stop): ").strip().lower()
    if keyword == "":
        break

    matches = []
    for row in data:
        for value in row:
            if keyword in value.lower():
                matches.append(row)
                break       # one match is enough for this row

    print(len(matches), "match(es) found")
    if matches:
        show_table(header, matches)
    print()


# ---------------------------------------------------
# 6. FILTER BY NUMBER
# ---------------------------------------------------
if column in header:
    print("--- FILTER ---")
    limit_text = input("Show rows where " + column + " is at least: ")

    try:
        limit = float(limit_text)
    except ValueError:
        print("That is not a number.")
    else:
        selected = []
        for record in records:
            try:
                if float(record[column]) >= limit:
                    selected.append(list(record.values()))
            except (ValueError, TypeError):
                pass        # ignore rows with bad numbers

        print(len(selected), "row(s) found")
        if selected:
            show_table(header, selected)

print("\nDone!")