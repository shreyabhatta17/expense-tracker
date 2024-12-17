import csv
import os

# Function to display the menu
def display_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Exit")

# Function to add a new expense
def add_expense(expense_file):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Shopping): ")
    description = input("Enter a short description: ")
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    # Save expense to file
    with open(expense_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(expense_file):
    if not os.path.exists(expense_file):
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print(f"{'Date':<15} {'Category':<15} {'Description':<25} {'Amount':<10}")
    print("-" * 65)
    with open(expense_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<25} {row[3]:<10}")
    print("-" * 65)

# Function to calculate total expenses
def calculate_total(expense_file):
    if not os.path.exists(expense_file):
        print("No expenses recorded yet.")
        return

    total = 0.0
    with open(expense_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[3])
    print(f"\nTotal Expenses: ${total:.2f}")

# Main function
def expense_tracker():
    expense_file = "expenses.csv"
    # Create the file with headers if it doesn't exist
    if not os.path.exists(expense_file):
        with open(expense_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense(expense_file)
        elif choice == "2":
            view_expenses(expense_file)
        elif choice == "3":
            calculate_total(expense_file)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    expense_tracker()
