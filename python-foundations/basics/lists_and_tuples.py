"""
lists_and_tuples.py
Topic: Lists and Tuples in Python

Covers:
1. List operations
2. Slicing and list comprehension
3. Tuples
4. Nested lists
5. Mini project
"""

# 1. Grocery List
print("\n--- GROCERY LIST ---")

items = input("Enter grocery items separated by comma: ").split(",")

items = [item.strip() for item in items if item.strip()]

print("Your list:", items)

add = input("Add one more item: ").strip()
if add:
    items.append(add)

print("Updated list:", items)


# 2. Student Marks
print("\n--- STUDENT MARKS ---")

marks = list(map(int, input("Enter marks separated by space: ").split()))

print("All marks:", marks)
print("Last 3 marks:", marks[-3:])

good_marks = [mark for mark in marks if mark >= 75]
print("Marks 75 and above:", good_marks)

print("Average:", sum(marks) / len(marks))


# 3. Tuple
print("\n--- STUDENT PROFILE ---")

name = input("Enter your name: ")
branch = input("Enter your branch: ")
year = input("Enter your year: ")

student = (name, branch, year)

print("Student information:", student)
print("Name:", student[0])
print("Branch:", student[1])
print("Year:", student[2])


# 4. Nested List
print("\n--- CLASSROOM SEATING ---")

classroom = [
    ["Aarav", "Riya"],
    ["Rahul", "Sneha"]
]

print("Classroom:")
for row in classroom:
    print(row)

print("Student at Row 1, Seat 2:", classroom[0][1])


# 5. Movie Watchlist
print("\n--- MOVIE WATCHLIST ---")

movies = []

for i in range(3):
    movie = input(f"Enter movie {i + 1}: ")
    movies.append(movie)

print("Your watchlist:", movies)

remove = input("Enter a movie to remove: ")

if remove in movies:
    movies.remove(remove)
    print("Movie removed!")
else:
    print("Movie not found.")

movies.sort()

print("Final watchlist:", movies)

print("\n🎉 Thanks for using the program!")
