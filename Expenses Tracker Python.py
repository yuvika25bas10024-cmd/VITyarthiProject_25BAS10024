expenses = {}

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: ₹"))
    expenses[category] = expenses.get(category, 0) + amount
    print(f"Expense added successfully! ₹{amount} spent on {category}")

def view_expenses():
    if not expenses:
        print("No expenses added yet!")
    else:
        print("Expenses:")
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount:.2f}")

def delete_expense():
    category = input("Enter expense category to delete: ")
    if category in expenses:
        del expenses[category]
        print(f"Expense deleted successfully! {category} removed")
    else:
        print(f"No expense found for {category}")

def calculate_total():
    total = sum(expenses.values())
    print(f"Total expenses: ₹{total:.2f}")

def main():
    while True:
        print("\nPersonal Expenses Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print("End")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    