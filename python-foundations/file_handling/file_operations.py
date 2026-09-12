"""
file_operations.py

Topic: File Operations in Python
Covers: with statement (context manager) | checking file existence | deleting a file
Mini use-case: a simple personal notes app
"""

import os

# ---------------------------------------------------------
# SECTION 1: with Statement — Reading App Configuration
# ---------------------------------------------------------
print("---- with Statement: App Configuration ----")

# create a sample config file first
with open("config.txt", "w") as config_file:
    config_file.write("theme=dark\n")
    config_file.write("font_size=14\n")

# 'with' automatically closes the file afterward, even if an error occurs
with open("config.txt", "r") as config_file:
    settings = config_file.read()

print("App settings loaded:")
print(settings)


# ---------------------------------------------------------
# SECTION 2: Checking File Existence — Saved Game File
# ---------------------------------------------------------
print("---- Checking File Existence: Saved Game ----")

save_file_path = "game_save.txt"

if os.path.exists(save_file_path):
    print("Save file found. Loading game...")
    with open(save_file_path, "r") as save_file:
        print(save_file.read())
else:
    print("No save file found. Starting a new game.")
    with open(save_file_path, "w") as save_file:
        save_file.write("level=1\nscore=0\n")
    print("New save file created.")


# ---------------------------------------------------------
# SECTION 3: Deleting a File — Clearing Temporary Cache
# ---------------------------------------------------------
print("\n---- Deleting a File: Temporary Cache ----")

cache_file_path = "temp_cache.txt"

with open(cache_file_path, "w") as cache_file:
    cache_file.write("temporary session data")

print(f"Cache file exists before cleanup: {os.path.exists(cache_file_path)}")

if os.path.exists(cache_file_path):
    os.remove(cache_file_path)

print(f"Cache file exists after cleanup: {os.path.exists(cache_file_path)}")


# ---------------------------------------------------------
# SECTION 4: Mini Project — Simple Personal Notes App
# ---------------------------------------------------------
# Combines everything above: with statement, existence check,
# append writing, and file deletion — a different domain from
# every section above.

print("\n---- Mini Project: Personal Notes App ----")

NOTES_FILE = "notes.txt"

new_note = input("Enter a note to save: ")

with open(NOTES_FILE, "a") as notes_file:
    notes_file.write(new_note + "\n")

print("\nAll saved notes:")
if os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "r") as notes_file:
        for line_number, note_line in enumerate(notes_file, start=1):
            print(f"{line_number}. {note_line.strip()}")

clear_choice = input("\nClear all notes? (y/n): ").strip().lower()
if clear_choice == "y":
    os.remove(NOTES_FILE)
    print("All notes cleared.")
else:
    print("Notes kept.")
