#User Profile Generator
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

#Text Analyzer
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)

print("=== TEXT ANALYZER ===")
print("--- Analysis Results ---")
print(f"Total characters (with spaces): {len(sentence)}")
print(f"Total characters (without spaces): {len(sentence.replace(' ', ''))}")
print(f"Number of words: {len(sentence.split())}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {sentence.upper()}")
print(f"Lowercase version: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Starts with capital: {'Yes' if sentence[0].isupper() else 'No'}")
print(f"Ends with punctuation: {'Yes' if sentence.endswith(('.', '!', '?')) else 'No'}")
