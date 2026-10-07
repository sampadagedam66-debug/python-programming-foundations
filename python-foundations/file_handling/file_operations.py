```python
# Basic File Handling Operations

file_name = "student.txt"


# Write data to the file
file = open(file_name, "w")

file.write("Welcome to Python File Handling!\n")
file.write("I am learning how to work with files in Python.\n")
file.write("This file is created using Python.\n")

file.close()

print("Data written successfully.")


# Read the file
file = open(file_name, "r")

print("\nFile Content:")
print(file.read())

file.close()


# Add more data without deleting existing content
file = open(file_name, "a")

file.write("This is an additional line.\n")

file.close()

print("Data added successfully.")


# Read the updated file line by line
file = open(file_name, "r")

print("\nUpdated File Content:")

for line in file:
    print(line.strip())

file.close()


# Check the number of characters
file = open(file_name, "r")

content = file.read()
print("\nNumber of characters:", len(content))

file.close()
```

