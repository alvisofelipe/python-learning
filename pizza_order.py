# ============================================
# PIZZA ORDER SYSTEM — Complete Program
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = [
    "Pepperoni", "Mushrooms", "Green Peppers", "Onions",
    "Sausage", "Bacon", "Extra Cheese", "Pineapple"
]
topping_price = 1.50

# ----- Order Storage -----
order_descriptions = []
order_prices = []
order_size_indexes = []

print("Welcome to the CS 1300 Pizza Shop!\n")

# Ask if they want to start an order
while True:
    start_order = input("Would you like to order a pizza? (yes/no): ").strip().lower()
    if start_order in ["yes", "y"]:
        break
    elif start_order in ["no", "n"]:
        print("\nNo pizzas ordered. See you next time!")
        quit()
    else:
        print("Please enter yes or no.")

# ===== ORDERING LOOP =====
while True:
    # ============================================
    # EXERCISE 1 — Display the size menu
    # ============================================
    print("\n" + "=" * 30)
    print("PIZZA SIZES")
    print("=" * 30)

    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]} ${size_prices[i]:>5.2f}")

    print("=" * 30)

    # ============================================
    # EXERCISE 2 — Get a valid size choice
    # ============================================
    while True:
        choice = input("Pick a size (1-4): ").strip()

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        if choice < 1 or choice > 4:
            print("Choose 1-4.")
            continue

        size_choice = choice - 1
        base_price = size_prices[size_choice]
        break

    # ============================================
    # EXERCISE 3 — Add toppings
    # ============================================
    selected_toppings = []

    print(f"\nAvailable toppings (${topping_price:.2f} each):")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    while True:
        topping_input = input("Add topping # (or 'done'): ").strip().lower()

        if topping_input == "done":
            break

        if not topping_input.isdigit():
            print("Please enter a topping number or 'done'.")
            continue

        topping_num = int(topping_input)

        if topping_num < 1 or topping_num > len(topping_names):
            print(f"Choose 1-{len(topping_names)}.")
            continue

        topping_name = topping_names[topping_num - 1]

        if topping_name in selected_toppings:
            print(f"Already added {topping_name}!")
            continue

        selected_toppings.append(topping_name)
        print(f"✓ Added {topping_name}")

    # ============================================
    # EXERCISE 4 — Calculate price and store pizza
    # ============================================
    pizza_price = base_price + (len(selected_toppings) * topping_price)

    if len(selected_toppings) == 0:
        description = f"{sizes[size_choice]} Cheese"
    else:
        description = f"{sizes[size_choice]} " + ", ".join(selected_toppings)

    order_descriptions.append(description)
    order_prices.append(pizza_price)
    order_size_indexes.append(size_choice)

    print(f"\nAdded to order: {description}")
    print(f"Pizza price: ${pizza_price:.2f}")

    # ============================================
    # EXERCISE 5 — Order another pizza?
    # ============================================
    while True:
        another = input("\nOrder another pizza? (yes/no): ").strip().lower()

        if another in ["yes", "y"]:
            break
        elif another in ["no", "n"]:
            ordering_done = True
            break
        else:
            print("Please enter yes or no.")

    if another in ["no", "n"]:
        break

# ===== POST-ORDER =====
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:
    # ============================================
    # EXERCISE 8 — Discount code with attempt limit
    # ============================================
    discount_rate = 0.0

    while True:
        has_code = input("\nDo you have a discount code? (yes/no): ").strip().lower()
        if has_code in ["yes", "y", "no", "n"]:
            break
        print("Please enter yes or no.")

    if has_code in ["yes", "y"]:
        attempts = 0
        while attempts < 3:
            code = input("Enter discount code (or type 'none' to skip): ").strip().upper()

            if code == "NONE":
                print("No discount applied.")
                break
            elif code == "STUDENT10":
                discount_rate = 0.10
                print("Discount applied: 10% off")
                break
            elif code == "HALFOFF":
                discount_rate = 0.50
                print("Discount applied: 50% off")
                break
            else:
                attempts += 1
                if attempts < 3:
                    print("Invalid code. Try again.")
                else:
                    print("No discount applied.")

    # ============================================
    # EXERCISE 6 — Print receipt
    # ============================================
    print("\n" + "=" * 36)
    print("YOUR ORDER RECEIPT")
    print("=" * 36)

    subtotal = 0.0
    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    print("-" * 36)
    print(f"Subtotal: ${subtotal:>6.2f}")

    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    tax = discounted_subtotal * 0.07
    total = discounted_subtotal + tax

    if discount_rate > 0:
        print(f"Discount: -${discount_amount:>5.2f}")
        print(f"New subtotal: ${discounted_subtotal:>6.2f}")

    print(f"Tax (7%): ${tax:>6.2f}")
    print(f"Total:    ${total:>6.2f}")
    print("=" * 36)

    # ============================================
    # EXERCISE 7 — Find most expensive / cheapest pizza
    # ============================================
    most_expensive_price = order_prices[0]
    most_expensive_desc = order_descriptions[0]

    cheapest_price = order_prices[0]
    cheapest_desc = order_descriptions[0]

    for i in range(len(order_prices)):
        if order_prices[i] > most_expensive_price:
            most_expensive_price = order_prices[i]
            most_expensive_desc = order_descriptions[i]

        if order_prices[i] < cheapest_price:
            cheapest_price = order_prices[i]
            cheapest_desc = order_descriptions[i]

    print(f"\nMost expensive pizza: {most_expensive_desc} (${most_expensive_price:.2f})")
    print(f"Cheapest pizza: {cheapest_desc} (${cheapest_price:.2f})")

    # ============================================
    # EXERCISE 9 — Count pizzas by size
    # ============================================
    personal_count = 0
    medium_count = 0
    large_count = 0
    party_count = 0

    for i in range(len(order_size_indexes)):
        if order_size_indexes[i] == 0:
            personal_count += 1
        elif order_size_indexes[i] == 1:
            medium_count += 1
        elif order_size_indexes[i] == 2:
            large_count += 1
        elif order_size_indexes[i] == 3:
            party_count += 1

    print("\nPIZZA SIZE BREAKDOWN")
    print(f"Personal: {personal_count}")
    print(f"Medium:   {medium_count}")
    print(f"Large:    {large_count}")
    print(f"Party:    {party_count}")

    average_price = subtotal / len(order_prices)
    print(f"Average price per pizza: ${average_price:.2f}")

    print("\nThank you for your order!")