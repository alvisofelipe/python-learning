# Problem 1: BMI Calculator
# This program calculates BMI based on the unit system (Metric or Imperial)
# and prints the BMI category.

# Ask user for weight
weight = float(input("Enter weight: "))

# Ask for unit system
unit = input("Enter unit system (M/I): ")

# Check if metric system
if unit.lower() == "m":
    height = float(input("Enter height (meters): "))
    bmi = weight / (height ** 2)

# Check if imperial system
elif unit.lower() == "i":
    height = float(input("Enter height (inches): "))
    bmi = (weight * 703) / (height ** 2)

# Invalid unit system
else:
    print("Invalid unit system.")
    exit()

# Print BMI formatted to 1 decimal place
print(f"BMI: {bmi:.1f}")

# Determine category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Normal weight")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")


# Problem 2: Password Strength Checker
# This program checks whether a password meets several security criteria.

password = input("Enter a password: ")

length_ok = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Loop through each character in the password
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

# Print results
print("Length >= 8:", "PASS" if length_ok else "FAIL")
print("Uppercase:", "PASS" if has_upper else "FAIL")
print("Lowercase:", "PASS" if has_lower else "FAIL")
print("Digit:", "PASS" if has_digit else "FAIL")
print("Special char:", "PASS" if has_special else "FAIL")

# Count how many criteria were met
count = 0
if length_ok: count += 1
if has_upper: count += 1
if has_lower: count += 1
if has_digit: count += 1
if has_special: count += 1

print("Criteria met:", count, "/ 5")

# Determine strength rating
if count == 5:
    print("Strength: Strong")
elif count >= 3:
    print("Strength: Moderate")
elif count >= 1:
    print("Strength: Weak")
else:
    print("Strength: No password entered")


# Problem 3: Inventory Manager
# This program manages store inventory using two parallel lists.

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

print("=== INVENTORY ===")

# Print inventory table
for i in range(len(products)):
    print(i + 1, ".", products[i], "-", quantities[i])

# Find highest and lowest quantities without max() or min()
highest_index = 0
lowest_index = 0

for i in range(len(quantities)):
    if quantities[i] > quantities[highest_index]:
        highest_index = i
    if quantities[i] < quantities[lowest_index]:
        lowest_index = i

print("Highest:", products[highest_index], "(", quantities[highest_index], ")")
print("Lowest:", products[lowest_index], "(", quantities[lowest_index], ")")

# Calculate total quantity
total = 0
for q in quantities:
    total += q

average = total / len(quantities)

print("Total quantity:", total)
print(f"Average quantity: {average:.2f}")

# Append Webcam
products.append("Webcam")
quantities.append(15)

# Insert USB Hub at index 2
products.insert(2, "USB Hub")
quantities.insert(2, 50)

# Remove Headset
index = products.index("Headset")
products.pop(index)
quantities.pop(index)

# Pop last product
removed_product = products.pop()
removed_quantity = quantities.pop()

print("Removed:", removed_product, "-", removed_quantity)

# Final inventory
print("=== FINAL INVENTORY ===")
for i in range(len(products)):
    print(i + 1, ".", products[i], "-", quantities[i])

print("Inventory length:", len(products))


# Problem 4: Parking Fee Calculator
# This program calculates parking fees based on vehicle type and duration.

vehicle = input("Enter vehicle type (car/motorcycle/truck): ")
hours = float(input("Enter hours parked: "))
pass_holder = input("Monthly pass? (yes/no): ")

fee = 0

# Monthly pass holders park free
if pass_holder.lower() == "yes":
    fee = 0

else:
    if vehicle.lower() == "motorcycle":
        if hours <= 2:
            fee = 1.00
        else:
            fee = 1.00 + (hours - 2) * 0.50

    elif vehicle.lower() == "car":
        if hours <= 2:
            fee = 3.00
        else:
            fee = 3.00 + (hours - 2) * 1.50

    elif vehicle.lower() == "truck":
        if hours <= 2:
            fee = 5.00
        else:
            fee = 5.00 + (hours - 2) * 2.50

    else:
        print("Invalid vehicle type.")
        exit()

# Print receipt
print("--- Parking Receipt ---")
print("Vehicle:", vehicle.capitalize())
print(f"Duration: {hours:.2f} hours")
print("Pass holder:", "Yes" if pass_holder.lower() == "yes" else "No")
print(f"Fee: ${fee:.2f}")


# Problem 5: Word Frequency Counter
# This program analyzes the words in a sentence and counts how often each appears.

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Print total number of words
print("\nTotal words:", len(words))

# Build list of unique words (no duplicates)
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Print unique word list
print("Unique words:", unique_words)

print("\n--- Word Frequencies ---")

# Track most frequent word
most_word = ""
most_count = 0

# Count frequency for each unique word
for uword in unique_words:
    count = 0
    
    # Compare with each word in original list
    for word in words:
        if word == uword:
            count += 1

    print(uword + ":", count)

    # Check if this is the most frequent so far
    if count > most_count:
        most_count = count
        most_word = uword

# Print most frequent word
print(f'Most frequent word: "{most_word}" ({most_count} times)')