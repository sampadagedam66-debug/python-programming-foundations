"""
lists_and_tuples.py

Topic: Lists and Tuples in Python
Covers: list creation & basic operations | slicing & list comprehension |
        tuple basics & immutability | nested lists
Mini use-case: A movie watchlist manager
"""

# ---------------------------------------------------------
# SECTION 1: List Creation & Basic Operations — Grocery Shopping List
# ---------------------------------------------------------
print("---- List Basics: Grocery Shopping List ----")

shopping_list = ["Rice", "Milk", "Eggs"]
print(f"Initial list: {shopping_list}")

shopping_list.append("Bread")            # add to the end
shopping_list.insert(1, "Vegetables")     # insert at a specific position
print(f"After append & insert: {shopping_list}")

shopping_list.remove("Eggs")              # remove by value
print(f"After removing Eggs: {shopping_list}")

shopping_list.sort()                      # sort alphabetically
print(f"Sorted list: {shopping_list}")

print(f"Total items: {len(shopping_list)}")


# ---------------------------------------------------------
# SECTION 2: Slicing & List Comprehension — Cricket Match Scores
# ---------------------------------------------------------
print("\n---- Slicing & Comprehension: Cricket Scores ----")

# runs scored on each ball across an innings
runs_per_ball = [1, 4, 0, 6, 2, 1, 4, 0, 6, 6, 1, 2]

last_five_balls = runs_per_ball[-5:]
print(f"All balls: {runs_per_ball}")
print(f"Last 5 balls: {last_five_balls}")

# list comprehension: keep only boundary hits (4s and 6s)
boundary_hits = [run for run in runs_per_ball if run == 4 or run == 6]
print(f"Boundary hits (4s & 6s): {boundary_hits}")
print(f"Total boundaries: {len(boundary_hits)}")

total_runs = sum(runs_per_ball)
print(f"Total runs scored: {total_runs}")


# ---------------------------------------------------------
# SECTION 3: Tuple Basics & Immutability — GPS Coordinates
# ---------------------------------------------------------
print("\n---- Tuples: Delivery GPS Coordinates ----")

warehouse_location = (19.0760, 72.8777)   # (latitude, longitude)
delivery_point_1 = (18.5204, 73.8567)
delivery_point_2 = (21.1458, 79.0882)

# unpacking a tuple into separate variables
latitude, longitude = warehouse_location
print(f"Warehouse coordinates: {warehouse_location}")
print(f"Latitude: {latitude}, Longitude: {longitude}")

all_delivery_points = (delivery_point_1, delivery_point_2)
print(f"Delivery points: {all_delivery_points}")

# tuples are immutable — this line would raise an error if uncommented:
# warehouse_location[0] = 20.0000
print("Tuples are immutable — coordinates can't be accidentally changed once set.")


# ---------------------------------------------------------
# SECTION 4: Nested Lists — Classroom Seating Arrangement
# ---------------------------------------------------------
print("\n---- Nested Lists: Classroom Seating ----")

# 3 rows, 3 seats each — a list of lists
classroom_seating = [
    ["Aman", "Priya", "Rohit"],
    ["Sneha", "Vikram", "Neha"],
    ["Karan", "Isha", "Dev"],
]

print("Full seating chart:")
print(classroom_seating[0])
print(classroom_seating[1])
print(classroom_seating[2])

# accessing a specific seat: row 1, seat 2
student_at_seat = classroom_seating[1][2]
print(f"\nStudent at Row 2, Seat 3: {student_at_seat}")

# updating a seat (someone changed seats)
classroom_seating[0][1] = "Farhan"
print(f"After seat change, Row 1: {classroom_seating[0]}")


# ---------------------------------------------------------
# SECTION 5: Mini Project — Movie Watchlist Manager
# ---------------------------------------------------------
# A small list-driven utility, a different domain from every
# section above, combining add/remove/sort/search operations.

print("\n---- Mini Project: Movie Watchlist Manager ----")

watchlist = ["Inception", "Interstellar", "The Matrix"]
print(f"Current watchlist: {watchlist}")

new_movie = input("Enter a movie to add to your watchlist: ")
if new_movie not in watchlist:
    watchlist.append(new_movie)
    print(f"Added '{new_movie}' to watchlist.")
else:
    print(f"'{new_movie}' is already in your watchlist.")

watched_movie = input("Enter a movie you've finished watching (to remove): ")
if watched_movie in watchlist:
    watchlist.remove(watched_movie)
    print(f"Removed '{watched_movie}' — enjoy, it's watched!")
else:
    print(f"'{watched_movie}' was not found in your watchlist.")

watchlist.sort()
print(f"\nFinal sorted watchlist: {watchlist}")
print(f"Movies remaining to watch: {len(watchlist)}")
