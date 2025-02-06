# ---------------------------------------------
# Personal Finance Tracker
# ---------------------------------------------
# This program allows users to:
# 1. Add income categorized by month.
# 2. Add expenses categorized by type.
# 3. View a financial summary including income and expenses.
# 4. View all expense categories.
# 5. Exit the program.
# ---------------------------------------------
# Data Storage:
# - 'wallet' Dictionary:
#   Key: Month | Value: List of Tuples [(Category, Income)]
# - 'expense_list' Dictionary:
#   Key: Expense Type | Value: List of Amounts
# ---------------------------------------------

wallet = {}  # Stores income categorized by month
expense_list = {}  # Stores expenses categorized by type

# ---------------------------------------------
# Function to Add Income
# ---------------------------------------------

def add_income():
    """
    Allows the user to add income categorized by month and category.
    """
    while True:
        month = input("\nEnter the month for the income (or type 'done' to finish): ").strip()
        if month.lower() == "done":
            break

        try:
            income = float(input("Enter the income amount: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        category = input("Enter the category for this income: ").strip()

        if month in wallet:
            wallet[month].append((category, income))
        else:
            wallet[month] = [(category, income)]

        print(f"\nIncome for {month} under '{category}' has been recorded!")

# ---------------------------------------------
# Function to Add Expenses
# ---------------------------------------------

def add_expense():
    """
    Allows the user to add expenses categorized by type.
    """
    while True:
        category = input("\nEnter the expense category (or type 'done' to finish): ").strip()
        if category.lower() == "done":
            break

        try:
            amount = float(input("Enter the expense amount: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if category in expense_list:
            expense_list[category].append(amount)
        else:
            expense_list[category] = [amount]

        print(f"\nExpense under '{category}' of ${amount:.2f} has been recorded!")

# ---------------------------------------------
# Function to View Financial Summary
# ---------------------------------------------

def view_summary():
    """
    Displays a summary of all recorded income and expenses,
    along with the total balance.
    """
    total_income = 0
    total_expense = 0

    print("\n--------------------------------------")
    print("| Month | Category | Income ($) |")
    print("--------------------------------------")
    
    if wallet:
        for month, month_list in wallet.items():
            for category, income in month_list:
                print(f"| {month:<6} | {category:<8} | ${income:<10.2f} |")
                total_income += income
    else:
        print("| No income records found.")

    print("--------------------------------------")
    print(f"Total Income: ${total_income:.2f}\n")

    print("\n--------------------------------------")
    print("| Expense Type | Amount ($) |")
    print("--------------------------------------")

    if expense_list:
        for category, amounts in expense_list.items():
            for amount in amounts:
                print(f"| {category:<12} | ${amount:<10.2f} |")
                total_expense += amount
    else:
        print("| No expense records found.")

    print("--------------------------------------")
    print(f"Total Expenses: ${total_expense:.2f}\n")

    balance = total_income - total_expense
    print(f"💰 Net Balance: ${balance:.2f}")
    print("--------------------------------------")

# ---------------------------------------------
# Function to View All Expense Categories
# ---------------------------------------------

def view_categories():
    """
    Displays all unique income and expense categories.
    """
    categories = set()

    for month, month_list in wallet.items():
        for category, _ in month_list:
            categories.add(category)

    for category in expense_list.keys():
        categories.add(category)

    if categories:
        print(f"\n🔹 Categories recorded: {', '.join(categories)}")
    else:
        print("\nNo categories found.")

# ---------------------------------------------
# Function to Handle User Menu Choices
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing finances.
    """
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Categories")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            add_income()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            view_summary()
        elif choice == 4:
            view_categories()
        elif choice == 5:
            print("\nThank you for using the Personal Finance Tracker. Goodbye! 💰")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-5).")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    menu()
