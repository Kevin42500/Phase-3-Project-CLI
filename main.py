import click
from authentication import register_user, login_user
from finance import add_transaction, list_transactions, calculate_total_income, calculate_total_expenses

@click.command()
def main():
    while True:
        click.clear()
        click.echo("Welcome to My Wallet CLI\n")
        click.echo("1. Register")
        click.echo("2. Login")
        click.echo("3. Exit\n")

        choice = click.prompt("Enter your choice (1/2/3)", type=click.Choice(['1', '2', '3']))

        if choice == '1':
            username = click.prompt("Enter your username")
            password = click.prompt("Enter your password", hide_input=True)
            if register_user(username, password):
                click.echo("Registration successful.")
            else:
                click.echo("Registration failed. Username may already exist.")

        elif choice == '2':
            username = click.prompt("Enter your username")
            password = click.prompt("Enter your password", hide_input=True)
            user_data = login_user(username, password)
            if user_data:
                click.echo("Login successful.")
                user_id, _, _ = user_data
                while True:
                    click.echo("\nUser Menu:")
                    click.echo("1. Add Transaction")
                    click.echo("2. List Transactions")
                    click.echo("3. Calculate Total Income")
                    click.echo("4. Calculate Total Expenses")
                    click.echo("5. Logout\n")

                    user_choice = click.prompt("Enter your choice (1/2/3/4/5)", type=click.Choice(['1', '2', '3', '4', '5']))

                    if user_choice == '1':
                        date = click.prompt("Enter transaction date (YYYY-MM-DD)")
                        category = click.prompt("Enter transaction category")
                        description = click.prompt("Enter transaction description")
                        amount = click.prompt("Enter transaction amount", type=float)
                        
                        
                        category_id = 1  
                        if add_transaction(user_id, date, category_id, description, amount):
                            click.echo("Transaction added successfully.")
                        else:
                            click.echo("Transaction failed to add.")

                    elif user_choice == '2':
                        transactions = list_transactions(user_id)
                        if transactions:
                            click.echo("Transactions:")
                            for transaction in transactions:
                                click.echo(transaction)
                        else:
                            click.echo("No transactions found for the user.")

                    elif user_choice == '3':
                        total_income = calculate_total_income(user_id)
                        if total_income is not None:
                            click.echo(f"Total Income: ${total_income:.2f}")
                        else:
                            click.echo("Unable to calculate total income.")

                    elif user_choice == '4':
                        total_expenses = calculate_total_expenses(user_id)
                        if total_expenses is not None:
                            click.echo(f"Total Expenses: ${total_expenses:.2f}")
                        else:
                            click.echo("Unable to calculate total expenses.")

                    elif user_choice == '5':
                        break

                    else:
                        click.echo("Invalid choice. Please select a valid option.")

            else:
                click.echo("Login failed. Invalid username or password.")

        elif choice == '3':
            click.echo("Exiting My Wallet CLI. Goodbye!")
            break

        else:
            click.echo("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
