# Problem 1: Boolean Expression Evaluator
# This program evaluates chained comparisons and confirms De Morgan's Law.

# Get user input
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Expression 1: Chained comparison
expr1 = a < b < c

# Expression 2: De Morgan's candidate
expr2 = not (a > b or b > c)

# Expression 3: Equivalent expression
expr3 = a <= b and b <= c

# Print results
print("a < b < c :", expr1)
print("not (a > b or b > c) :", expr2)
print("a <= b and b <= c :", expr3)

# Confirm whether expressions 2 and 3 match
if expr2 == expr3:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("De Morgan's NOT confirmed: Expressions 2 and 3 do not match.")


# Problem 2: Weather Advisory System
# This program gives a weather advisory based on temperature and rain.

# Get user input
temperature = float(input("Enter current temperature (°F): "))
raining_input = input("Is it raining? (yes/no): ").strip().lower()

# Convert rain input to Boolean
raining = raining_input == "yes"

# Temperature-based advisory using if-elif-else chain
if temperature > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temperature > 85:
    if raining:
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temperature <= 85:
    if raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temperature <= 59:
    print("It's cold — bundle up!")

else:  # temperature < 32
    print("FREEZE WARNING: Roads may be icy!")


# Problem 3: Student Grade Report
# This program calculates average, letter grade, and academic standing.

# Get student information
name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

# Calculate average
average = (exam1 + exam2 + exam3) / 3

# Determine letter grade (highest ranges first!)
if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Determine academic standing
if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Print formatted report
print("\n============================")
print("STUDENT GRADE REPORT")
print("============================")
print("Student:", name)
print("Exam 1:", exam1)
print("Exam 2:", exam2)
print("Exam 3:", exam3)
print("----------------------------")
print("Average:", round(average, 2))
print("Grade:", grade)
print("Status:", status)
print("============================")

