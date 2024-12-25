import datetime

# Represents an individual expense with category, amount, date, and optional description
class Expense:
    def __init__(self, category, amount, date, description=""):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        # Returns a string representation of the expense for display purposes
        return f"[{self.date}] {self.category}: ${self.amount:.2f} ({self.description})"

# Manages a list of expenses and provides functionality to manipulate them
class ExpenseTracker:
    def __init__(self):
        # Initializes an empty list to store expenses
        self.expenses = []

    def add_expense(self, category, amount, date, description=""):
        # Adds a new expense to the tracker
        new_expense = Expense(category, amount, date, description)
        self.expenses.append(new_expense)

    def view_expenses(self):
        # Returns the list of all expenses
        return self.expenses

    def view_expenses_by_category(self, category):
        # Filters and returns expenses matching the given category
        return [expense for expense in self.expenses if expense.category == category]

    def calculate_total(self, start_date=None, end_date=None):
        # Calculates the total amount of expenses, optionally within a date range
        total = 0
        for expense in self.expenses:
            if start_date and expense.date < start_date:
                continue
            if end_date and expense.date > end_date:
                continue
            total += expense.amount
        return total

# Main function to provide a user interface for interacting with the ExpenseTracker
def main():
    tracker = ExpenseTracker()
    while True:
        # Display menu options
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Exit")

        # Get user's choice
        choice = input("Choose an option: ")
        if choice == "1":
            # Add a new expense
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            description = input("Enter description (optional): ")
            tracker.add_expense(category, amount, date, description)
            print("Expense added successfully!")
        elif choice == "2":
            # View all recorded expenses
            expenses = tracker.view_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == "3":
            # View expenses filtered by category
            category = input("Enter category to view: ")
            expenses = tracker.view_expenses_by_category(category)
            if not expenses:
                print(f"No expenses found for category: {category}")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == "4":
            # Calculate the total expenses within an optional date range
            start_date_str = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ")
            end_date_str = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None
            total = tracker.calculate_total(start_date, end_date)
            print(f"Total expenses: ${total:.2f}")
        elif choice == "5":
            # Exit the application
            print("Exiting the application. Goodbye!")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
