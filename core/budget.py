from datetime import datetime, timedelta

from core.transaction import Transaction


class Budget:
    def __init__(self, current_balance, end_date: datetime, transactions: list[Transaction]):
        self.current_balance = current_balance
        self.end_date = end_date
        self.monthly_bills = list()
        self.one_off_expenses = list()
        for transaction in transactions:
            if transaction.day is None:
                self.one_off_expenses.append(transaction)
            else:
                self.monthly_bills.append(transaction)

    def calculate_total_monthly_bills(self) -> float:
        '''
        What is the total of monthly bills for the duration of the budget?
        :return: total monthly bills
        '''
        total_monthly_bills = 0.0
        days_left = (self.end_date - datetime.now()).days
        for bill in self.monthly_bills:
            curr_date = datetime.now()
            for i in range(days_left):
                if bill.day == curr_date.day:
                    total_monthly_bills += bill.amount
                curr_date += timedelta(days=1)

        return total_monthly_bills

    def calculate_daily_budget(self) -> float:
        days_left = (self.end_date - datetime.now()).days
        if days_left < 0:
            return 0.0
        balance = self.calculate_remaining_balance()
        return balance / (days_left + 1)

    def calculate_total_one_off_expenses(self) -> float:
        if not self.one_off_expenses:
            return 0.0
        return sum(expense.amount for expense in self.one_off_expenses)

    def calculate_remaining_balance(self) -> float:
        return self.current_balance - self.calculate_total_monthly_bills() - self.calculate_total_one_off_expenses()

    def __str__(self):
        return (f"Current balance: {self.current_balance}\n"
                f"One-off expenses (total): {self.calculate_total_one_off_expenses()}\n"
                f"Monthly bills (monthly): {sum(bill.amount for bill in self.monthly_bills)}\n"
                f"Monthly bills (total): {self.calculate_total_monthly_bills()}\n"
                f"Remaining balance: {self.calculate_remaining_balance()}\n"
                f"Daily budget: {self.calculate_daily_budget()}")

