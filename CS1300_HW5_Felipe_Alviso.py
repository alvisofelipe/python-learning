# CS1300 Homework Assignment 5 - Programming Solutions
# All 5 problems included below

# Problem 1: Temperature Converter
# This program converts a temperature from Celsius to Fahrenheit or vice versa

# Ask user for temperature value and convert it to float
temp = float(input("Enter temperature: "))

# Ask user for the scale (Celsius/Fahrenheit) and convert to uppercase
scale = input("Enter scale (C/F): ").upper()

# Check if scale is Celsius
if scale == "C":
    # Convert Celsius to Fahrenheit
    f = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {f:.1f}°F")
# Check if scale is Fahrenheit
elif scale == "F":
    # Convert Fahrenheit to Celsius
    c = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {c:.1f}°C")
# If user enters invalid scale
else:
    print("Invalid scale.")


# Problem 2: String Analyzer
# This program analyzes a sentence to count characters, uppercase, lowercase, digits, spaces, and reverses it

# Ask user for a sentence
sentence = input("Enter a sentence: ")

# Count total characters including spaces
total = len(sentence)

# Count uppercase letters
upper = sum(1 for c in sentence if c.isupper())

# Count lowercase letters
lower = sum(1 for c in sentence if c.islower())

# Count digits
digits = sum(1 for c in sentence if c.isdigit())

# Count spaces
spaces = sum(1 for c in sentence if c == " ")

# Print all the analysis results
print(f"Total characters: {total}")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")

# Print the sentence reversed
print(f"Reversed: {sentence[::-1]}")


# Problem 3: List Operations Toolkit
# This program performs multiple operations on a list and prints results step by step

# Initialize the list of numbers
numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

# Print the original list
print("Original:", numbers)

# Print first and last elements
print("First:", numbers[0], "Last:", numbers[-1])

# Print a slice of the middle 4 elements (indices 3 to 6)
print("Middle 4:", numbers[3:7])

# Append 99 to the end of the list
numbers.append(99)
print("After append 99:", numbers)

# Insert 0 at the beginning (index 0)
numbers.insert(0, 0)
print("After insert 0 at start:", numbers)

# Remove the value 42 from the list
numbers.remove(42)
print("After removing 42:", numbers)

# Pop (remove) the last element and store it in 'removed'
removed = numbers.pop()
print("Popped last element:", removed)

# Check if 23 is in the list and print True or False
print("23 in list?", 23 in numbers)

# Print the index of the value 16
print("Index of 16:", numbers.index(16))

# Print the final list and its length
print("Final list:", numbers, "Length:", len(numbers))


# Problem 4: Course Eligibility Checker
# This program determines if a student is eligible to register for an advanced course

# Ask user for GPA and convert to float
gpa = float(input("Enter GPA (0.0-4.0): "))

# Ask user for number of completed credit hours
credits = int(input("Enter credit hours completed: "))

# Ask user if prerequisite course is completed, convert input to lowercase
prereq = input("Prerequisite completed? (yes/no): ").lower()

# Check eligibility conditions using if-elif-else chain
if gpa >= 3.5 and credits >= 60 and prereq == "yes":
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60 and prereq != "yes":
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

# Print registration summary
print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {'Yes' if prereq == 'yes' else 'No'}")
print(f"Status: {status}")
print("----------------------------")


# Problem 5: Student Roster Manager
# This program manages a class roster and performs multiple tasks like finding highest/lowest scores, average, grades, and updates the roster

# Initialize lists of student names and their scores
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1: Print formatted class roster
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

# Task 2: Find student with highest and lowest score
high_idx = 0
low_idx = 0
for i in range(1, len(scores)):
    if scores[i] > scores[high_idx]:
        high_idx = i  # Update highest score index
    if scores[i] < scores[low_idx]:
        low_idx = i   # Update lowest score index
print(f"Highest score: {names[high_idx]} - {scores[high_idx]}")
print(f"Lowest score: {names[low_idx]} - {scores[low_idx]}")

# Task 3: Calculate class average
avg = sum(scores)/len(scores)
print(f"Class average: {avg:.2f}")

# Task 4: Determine letter grade for each student
print("--- Grade Report ---")
for i in range(len(names)):
    s = scores[i]
    if 90 <= s <= 100:
        grade = "A"
    elif 80 <= s <= 89:
        grade = "B"
    elif 70 <= s <= 79:
        grade = "C"
    elif 60 <= s <= 69:
        grade = "D"
    else:
        grade = "F"
    print(f"{names[i]}: {s} -> {grade}")

# Task 5: Add a new student Frank and remove Diana
names.append("Frank")
scores.append(77)

# Remove Diana from both lists
idx_diana = names.index("Diana")
names.pop(idx_diana)
scores.pop(idx_diana)

# Print updated roster length
print("Updated roster length:", len(names))