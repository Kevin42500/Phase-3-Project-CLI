import finance

user_id = 1
date = "2023-10-15"
category_id = 1  
description = "Groceries shopping"
amount = 50.0

if finance.add_transaction(user_id, date, category_id, description, amount):
    print("Transaction added successfully.")
else:
    print("Failed to add the transaction.")

user_id_to_list = 1
transactions = finance.list_transactions(user_id_to_list)

if transactions:
    print(f"Transactions for User ID {user_id_to_list}:")
    for transaction in transactions:
        print(f"Transaction ID: {transaction['id']}, Date: {transaction['date']}, Category ID: {transaction['category_id']}, Amount: {transaction['amount']}")
else:
    print(f"No transactions found for User ID {user_id_to_list}.")

user_id_to_calculate = 1
total_expenses = finance.calculate_total_expenses(user_id_to_calculate)
total_income = finance.calculate_total_income(user_id_to_calculate)

print(f"Total Expenses for User ID {user_id_to_calculate}: {total_expenses}")
print(f"Total Income for User ID {user_id_to_calculate}: {total_income}")
