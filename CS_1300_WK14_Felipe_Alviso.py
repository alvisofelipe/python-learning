# ============================================
# CS1300 - Week 14 Lecture 2
# Lists Part II – Units 1, 2, 3 Exercises
# ============================================


# ============================================
# UNIT 1: TUPLES
# ============================================

# ---------- Beginner Exercise ----------
rgb_color = (255, 128, 0)

print("Red:", rgb_color[0])
print("Green:", rgb_color[1])
print("Blue:", rgb_color[2])

palette = []
palette.append(rgb_color)

print("Palette:", palette)


# ---------- Intermediate Exercise ----------
student1 = ("Alice", 90, 20)
student2 = ("Bob", 85, 19)
student3 = ("Charlie", 88, 21)

classroom = [student1, student2, student3]

print("Second student:", classroom[1][0])

name, grade, age = classroom[0]
print(f"{name} is {age} years old and has a grade of {grade}.")


# ---------- Advanced Exercise ----------
student = ("Alice", [85, 90, 78], 0)

student[1].append(92)

avg = sum(student[1]) / len(student[1])

updated_student = (student[0], student[1], avg)

print("Original:", student)
print("Updated:", updated_student)



# ============================================
# UNIT 2: LIST VS TUPLE
# ============================================

# ---------- Beginner Exercise ----------
grades = [85, 90, 78]
today = (4, 20, 2026)

def boost_grades(grades_list):
    for i in range(len(grades_list)):
        grades_list[i] += 5

boost_grades(grades)

print("Boosted grades:", grades)

# Explanation:
# Lists are used for grades because they change.
# Tuples are used for dates because they should not change.


# ---------- Intermediate Exercise ----------
def find_range(*args):
    return (min(args), max(args))

print(find_range(10, 5, 20))
print(find_range(3, 8, 1, 9, 15, 2, 7))

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))


# ---------- Advanced Exercise ----------
def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    avg = total / count if count > 0 else 0
    return (count, total, avg)

def update_student_records(records, bonus):
    new_records = []
    for name, grade in records:
        new_records.append((name, grade + bonus))
    return new_records

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

updated = update_student_records(students, 5)

stats = calculate_statistics(*[grade for _, grade in updated])

print("Updated Records:", updated)
print("Stats (count, sum, avg):", stats)



# ============================================
# UNIT 3: NESTED LISTS & COMPREHENSIONS
# ============================================

# ---------- Beginner Exercise ----------
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Grid:", grid)
print("Center:", grid[1][1])

for row in grid:
    print(row)


# ---------- Intermediate Exercise ----------
scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [s for s in scores if s >= 60]

letter_grades = [
    'A' if s >= 90 else
    'B' if s >= 80 else
    'C' if s >= 70 else
    'D'
    for s in passing_grades
]

print("Passing:", passing_grades)
print("Letters:", letter_grades)


# ---------- Advanced Exercise ----------
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

print("Multiplication Table:")
for row in table:
    print(row)

def sum_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

print("Diagonal sum:", sum_diagonal(table))

even_gen = (num for row in table for num in row if num % 2 == 0)

print("First 5 even numbers:")
count = 0
for val in even_gen:
    print(val)
    count += 1
    if count == 5:
        break