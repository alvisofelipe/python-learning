# =========================
# Problem 1 — FizzBuzz
# =========================
# Prints numbers 1–30 with substitutions

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")   # divisible by both
    elif i % 3 == 0:
        print("Fizz")       # divisible by 3
    elif i % 5 == 0:
        print("Buzz")       # divisible by 5
    else:
        print(i)            # otherwise print number


# =========================
# Problem 2 — Times Table
# =========================
# Prints a 6x6 multiplication table (aligned)

n = 6

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")  # width 4 for alignment
    print()  # move to next row


# =========================
# Problem 3 — Remove Duplicates (Preserve Order)
# =========================
# Returns a new list without duplicates, keeping order

def unique_preserve_order(lst):
    result = []
    for item in lst:
        if item not in result:   # only add if not seen before
            result.append(item)
    return result


# =========================
# Problem 4 — Fibonacci
# =========================
# Returns first n Fibonacci numbers

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])  # sum of last two
    return seq


# =========================
# Problem 5 — Mini Banking System
# =========================
# Simple interactive banking program

balance = 1000.0
history = []

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show transaction history")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print(f"Current balance: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter amount: "))
        if amount > 0:
            balance += amount
            history.append(("Deposit", amount))
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    elif choice == "3":
        amount = float(input("Enter amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            history.append(("Withdraw", amount))
            print("Withdrawal successful.")
        elif amount <= 0:
            print("Amount must be positive.")
        else:
            print("Insufficient funds.")

    elif choice == "4":
        if not history:
            print("No transactions yet.")
        else:
            for i, (t, amt) in enumerate(history, 1):
                print(f"{i}. {t}: ${amt:.2f}")

    elif choice == "5":
        print(f"Final balance: ${balance:.2f}")
        break

    else:
        print("Invalid choice, please select 1-5.")