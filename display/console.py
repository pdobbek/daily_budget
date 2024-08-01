from datetime import datetime, timedelta

from core.budget import Budget
from core.transaction import Transaction
from core.transaction_factories import CSVTransactionFactory


def after_budget_created_choice(budget):
    while True:
        options = ("Change budget amount (a)"
                   "\nChange budget duration (d)"
                   "\nSave budget (s)"
                   "\nCancel (c)")
        choice = get_user_input(options)
        if choice == 'a':
            change_budget_amount(budget)
        elif choice == 'd':
            change_budget_duration(budget)
        elif choice == 's':
            # TODO: implement saving the budget
            print("Saving budget is not yet implemented.")
        elif choice == 'c':
            pass
        else:
            print("Invalid choice.")


def get_user_input(prompt):
    """Gets user input from the console."""
    print(prompt, end="")
    return input("\n> ")


def get_transaction_data(manual_input=True):
    """Gets transaction data from the user, either manually or from a CSV file."""
    transactions = []
    if manual_input:
        while True:
            name = get_user_input("Enter transaction name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            amount = float(get_user_input("Enter transaction amount: "))
            day = int(get_user_input("Enter transaction day (or leave blank for one-off): ")) if name.lower() != 'done' else None
            transactions.append(Transaction(name, amount, day))
    else:
        file_path = get_user_input("Enter path to CSV file: ")
        factory = CSVTransactionFactory()
        transactions = factory.load_transactions_from_csv(file_path)
    return transactions


def change_budget_amount(budget):
    """Changes the budget amount and updates the budget object."""
    new_amount = float(get_user_input("Enter new budget amount: "))
    budget.current_balance = new_amount
    display_budget(budget)


def change_budget_duration(budget):
    """Changes the budget duration and updates the budget object."""
    new_days = int(get_user_input("Enter new budget duration in days: "))
    budget.end_date = datetime.now() + timedelta(days=new_days)
    display_budget(budget)


def create_budget():
    """Creates a new budget based on user input."""
    current_balance = float(get_user_input("Enter current balance: "))
    days = int(get_user_input("Enter budget duration in days: "))
    end_date = datetime.now() + timedelta(days=days)

    input_method = get_user_input("Enter data manually (m) or from CSV (c): ").lower()
    if input_method == 'm':
        transactions = get_transaction_data()
    else:
        transactions = get_transaction_data(manual_input=False)

    budget = Budget(current_balance, end_date, transactions)
    return budget


def display_budget(budget):
    """Displays the budget information."""
    print(f"\n{budget}\n")


def main():
    """Main function for the CLI menu."""
    while True:
        choice = get_user_input("Create new budget (n) or display saved budget (d)? ").lower()
        if choice == 'n':
            budget = create_budget()
            display_budget(budget)
            after_budget_created_choice(budget)
        elif choice == 'd':
            # TODO: Implement loading a saved budget
            print("Loading saved budget is not yet implemented.")
        else:
            print("Invalid choice.")

        continue_choice = get_user_input("Continue (y/n)? ").lower()
        if continue_choice != 'y':
            break


if __name__ == "__main__":
    main()
