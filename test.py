import unittest
from datetime import date
from exptrack import ExpenseTracker, Expense  # Importing the ExpenseTracker and Expense classes from the main module

# Unit tests for the ExpenseTracker class
class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        # Test case to verify adding an expense to the tracker
        tracker = ExpenseTracker()
        tracker.add_expense("Food", 50.0, date(2024, 12, 25), "Dinner")  # Adding a food expense
        self.assertEqual(len(tracker.expenses), 1)  # Check if one expense is added
        self.assertEqual(tracker.expenses[0].category, "Food")  # Verify the category of the expense
        self.assertEqual(tracker.expenses[0].amount, 50.0)  # Verify the amount of the expense

    def test_calculate_total(self):
        # Test case to verify the total calculation of expenses
        tracker = ExpenseTracker()
        tracker.add_expense("Food", 50.0, date(2024, 12, 25))  # Adding a food expense
        tracker.add_expense("Transport", 20.0, date(2024, 12, 26))  # Adding a transport expense
        total = tracker.calculate_total()  # Calculate the total of all expenses
        self.assertEqual(total, 70.0)  # Verify the total is correct

# Entry point to run the unit tests
if __name__ == "__main__":
    unittest.main()
