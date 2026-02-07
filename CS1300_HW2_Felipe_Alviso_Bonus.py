# Bonus Question: Palindrome Checker

text = input("Enter a word or phrase: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f'"{text}" → Palindrome')
else:
    print(f'"{text}" → Not a palindrome')
