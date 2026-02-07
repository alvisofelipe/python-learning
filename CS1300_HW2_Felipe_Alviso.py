first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ").title()

age = 2026 - birth_year

print("=" * 36)
print("USER PROFILE CARD")
print("=" * 36)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)
