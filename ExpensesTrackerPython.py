expenses = {}

def add_expense():
    category = input("What’s the expense category? ")
    try:
        amount = float(input("How much did you spend? ₹"))
    except ValueError:
        print("That doesn’t look like a number. Try again.")
        return
    expenses[category] = expenses.get(category, 0) + amount
    print(f"Got it! You spent ₹{amount} on {category}.")

def view_expenses():
    if not expenses:
        print("You haven’t added any expenses yet.")
        return
    print("Here’s what you’ve spent so far:")
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")

def delete_expense():
    category = input("Which expense category do you want to remove? ")
    if category in expenses:
        del expenses[category]
        print(f"All expenses for {category} are gone.")
    else:
        print(f"No expenses found for {category}.")

def calculate_total():
    total = sum(expenses.values())
    print(f"You’ve spent a total of ₹{total:.2f}")

def main():
    while True:
        print("\nPersonal Expenses Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total")
        print("5. Quit")
        choice = input("Pick an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print("Alright, see you next time.")
            break
        else:
            print("Invalid option. Try again.")

if _name_ == "_main_":
    main()