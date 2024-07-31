from datetime import datetime, timedelta
from core.budget import Budget
from core.transaction import Transaction
from core.transaction_factories import CSVTransactionFactory


def get_user_input(prompt):
    """Gets user input from the console."""
    return input(prompt)


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


def create_budget():
    """Creates a new budget based on user input."""
    current_balance = float(get_user_input("Enter current balance: "))
    days = int(get_user_input("Enter budget duration in days: "))
    end_date = datetime.now() + timedelta(days=days)

    input_method = get_user_input("Enter data manually (m) or from CSV (c): ").lower()
    if input_method == 'm':
        monthly_bills = get_transaction_data()
        one_off_expenses = get_transaction_data()
    else:
        monthly_bills = get_transaction_data(manual_input=False)
        one_off_expenses = get_transaction_data(manual_input=False)

    budget = Budget(current_balance, end_date, monthly_bills, one_off_expenses)
    return budget


def display_budget(budget):
    """Displays the budget information."""
    print(budget)


def main():
    """Main function for the CLI menu."""
    while True:
        choice = get_user_input("Create new budget (n) or display saved budget (d)? ").lower()
        if choice == 'n':
            budget = create_budget()
            display_budget(budget)
            n_choice = get_user_input("Would you like to save the budget? (y/n) ").lower()
            if n_choice == 'y':
                # TODO: Implement saving the budget
                print("Saving budget is not yet implemented.")
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
