expenses = []

while True:
    print("=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Show total spent")
    print("5. Exit")
    print("")

    choice = int(input("Choose an option: "))

    if choice == 1:
        expenseName = input("Name: ")
        expenseAmount = float(input("Amount: "))
        expenseCategory = input("Category: ")

        expense = {
            "name": expenseName,
            "amount": expenseAmount,
            "category": expenseCategory,
        }

        expenses.append(expense)

        print("Created new expense")
        print("")

    if choice == 2:
        print("Your Expenses:")

        for expense in expenses:
            print(
                f"{expense['name']} - ${expense['amount']:.2f} - {expense['category']}"
            )

        print("")

    if choice == 3:
        found = False

        rmExpense = input("Enter the name of the expense you want to remove: ")

        for expense in expenses:
            if rmExpense == expense["name"]:
                expenses.remove(expense)
                print("Expense removed successfully")
                found = True
                break

        if not found:
            print("Expense name not found")

        print("")

    if choice == 4:
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expense: ${total:.2f}")
        print("")

    if choice == 5:
        print("Goodbye!")
        break
