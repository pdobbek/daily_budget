import datetime
import unittest

from core.budget import Budget
from core.transaction import Transaction


class TestBudget(unittest.TestCase):
    @classmethod
    def generate_monthly_bills(cls):
        return [
            Transaction(name="Accom.", amount=300, day=15),
            Transaction(name="Gym", amount=30, day=15),
            Transaction(name="Protein", amount=30, day=15),
            Transaction(name="Phone", amount=50, day=15),
            Transaction(name="Subs.", amount=20, day=15)
        ]

    @classmethod
    def generate_one_off_expenses(cls):
        return [
            Transaction(name="Air ticket", amount=700),
            Transaction(name="Concert", amount=100)
        ]

    def test_calculate_daily_budget(self):
        # TODO Fails
        current_balance = 3000
        budget = Budget(
            current_balance=current_balance,
            end_date=datetime.datetime.now() + datetime.timedelta(days=90),  # three months
            transactions=self.generate_monthly_bills() + (self.generate_one_off_expenses())
        )
        expected_remaining_balance = 910
        self.assertEqual(expected_remaining_balance, budget.calculate_remaining_balance())
        expected_daily_budget = 910 / 90
        self.assertEqual(expected_daily_budget, budget.calculate_daily_budget())

    def test_calculate_total_monthly_bills(self):
        monthly_bills = self.generate_monthly_bills()
        # end date three months from now
        end_date = datetime.datetime.now() + datetime.timedelta(days=90)
        budget = Budget(
            current_balance=1000,
            end_date=end_date,
            transactions=self.generate_monthly_bills()
        )
        self.assertEqual(1290.0, budget.calculate_total_monthly_bills())

    def test_calculate_total_one_off_expenses(self):
        one_off_expenses = self.generate_one_off_expenses()
        expected_total_one_off_expenses = 800
        budget = Budget(
            current_balance=1000,
            end_date=datetime.datetime.now(),
            transactions=self.generate_one_off_expenses()
        )
        self.assertEqual(expected_total_one_off_expenses, budget.calculate_total_one_off_expenses())

    def test_calculate_remaining_balance(self):
        current_balance = 3000
        budget = Budget(
            current_balance=current_balance,
            end_date=datetime.datetime.now() + datetime.timedelta(days=90),
            transactions=self.generate_one_off_expenses() + self.generate_monthly_bills()
        )
        self.assertEqual(current_balance - 800 - 1290, budget.calculate_remaining_balance())


if __name__ == '__main__':
    unittest.main
