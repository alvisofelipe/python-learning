# Problem 1: Movie Ticket Pricing
# Calculates movie ticket price based on age and showing type

# Get user input
age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    # Use conditional expression (ternary) to convert input to Boolean
    is_matinee = True if matinee_input == "yes" else False

    # Nested if: outer = age group, inner = matinee vs regular
    if age < 13:
        age_group = "Child"
        price = 6.00 if is_matinee else 8.00
    elif age <= 17:
        age_group = "Teen"
        price = 7.00 if is_matinee else 10.00
    elif age <= 64:
        age_group = "Adult"
        price = 8.00 if is_matinee else 13.00
    else:
        age_group = "Senior"
        price = 6.00 if is_matinee else 7.00

    print(f"Age group: {age_group}")
    print(f"Ticket price: ${price:.2f}")


# Problem 2: Input Validator
# Validates a student profile, collecting all errors before reporting

# Collect all inputs
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

errors = []

# --- Validate Student ID ---
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")
if not student_id[0].isalpha() if student_id else True:
    errors.append("Student ID must start with a letter")
if len(student_id) > 1 and not student_id[1:].isdigit():
    errors.append("Student ID characters 2–8 must all be digits")

# --- Validate Name ---
if len(name.strip()) < 2:
    if name.strip() == "":
        errors.append("Name cannot be empty")
    else:
        errors.append("Name must be at least 2 characters")

# --- Validate Age (type + range) ---
age = None
try:
    age = int(age_input)
    if not (16 <= age <= 99):
        errors.append("Age must be between 16 and 99 (inclusive)")
except ValueError:
    errors.append("Age must be a valid integer")

# --- Validate Major ---
valid_majors = ["CS", "IT", "CE", "DS"]
if major.strip().upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# --- Report results ---
if not errors:
    print("\n✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name.strip()}")
    print(f"Age: {age}")
    print(f"Major: {major.strip().upper()}")
else:
    print("\n✗ Profile has errors:")
    for error in errors:
        print(f"  - {error}")


# Problem 3: Campus Café Menu
# Menu-driven ordering system with customization, validation, and receipt

print("=" * 30)
print("    CAMPUS CAFÉ ORDER SYSTEM")
print("=" * 30)
print("1. Coffee    - $3.50")
print("2. Sandwich  - $6.00")
print("3. Salad     - $5.50")
print("4. Combo     - $8.00")
print("5. Exit")
print("=" * 30)

choice = input("Enter your choice (1-5): ").strip()

# Exit early if user chooses 5
if choice == "5":
    print("Goodbye!")
    exit()

item_name = ""
unit_price = 0.0

if choice == "1":
    # Coffee: ask for size
    size = input("Size? (small/medium/large): ").strip().lower()
    if size == "medium":
        unit_price = 4.50
        item_name = "Coffee (Medium)"
    elif size == "large":
        unit_price = 5.50
        item_name = "Coffee (Large)"
    else:
        if size not in ("small",):
            print("Invalid size. Defaulting to Small.")
        unit_price = 3.50
        item_name = "Coffee (Small)"

elif choice == "2":
    # Sandwich: ask about cheese
    cheese = input("Add cheese? (yes/no): ").strip().lower()
    if cheese == "yes":
        unit_price = 6.75
        item_name = "Sandwich + Cheese"
    else:
        unit_price = 6.00
        item_name = "Sandwich"

elif choice == "3":
    # Salad: ask for dressing
    valid_dressings = ["ranch", "italian", "vinaigrette", "none"]
    dressing = input("Dressing? (ranch/italian/vinaigrette/none): ").strip().lower()
    if dressing not in valid_dressings:
        print("Invalid dressing. Defaulting to none.")
        dressing = "none"
    unit_price = 5.50
    item_name = f"Salad ({dressing.capitalize()} dressing)"

elif choice == "4":
    # Combo: coffee size + cheese
    size = input("Coffee size? (small/medium/large): ").strip().lower()
    if size == "medium":
        coffee_price = 1.00  # upcharge
        size_label = "Medium"
    elif size == "large":
        coffee_price = 2.00
        size_label = "Large"
    else:
        if size not in ("small",):
            print("Invalid size. Defaulting to Small.")
        coffee_price = 0.00
        size_label = "Small"

    cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
    if cheese == "yes":
        cheese_price = 0.75
        cheese_label = "+ Cheese"
    else:
        cheese_price = 0.00
        cheese_label = ""

    unit_price = 8.00 + coffee_price + cheese_price
    item_name = f"Combo (Sandwich{cheese_label} + Coffee {size_label})"

else:
    print("Invalid choice. Please run the program again.")
    exit()

# --- Get customer name (cannot be empty) ---
name = ""
while not name:
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")

# --- Get quantity (positive integer, validated with try/except) ---
quantity = 0
while quantity <= 0:
    try:
        quantity = int(input("How many? "))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

# --- Calculate totals ---
subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax

# --- Print receipt ---
print("\n" + "=" * 30)
print("         ORDER RECEIPT")
print("=" * 30)
print(f"Customer:  {name}")
print(f"Item:      {item_name}")
print(f"Quantity:  {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal:  ${subtotal:.2f}")
print(f"Tax (7%):  ${tax:.2f}")
print(f"Total:     ${total:.2f}")
print("=" * 30)
print("   Thank you for your order!")