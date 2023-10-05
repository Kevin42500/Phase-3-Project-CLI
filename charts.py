import matplotlib.pyplot as plt
from finance import list_transactions

def create_expense_pie_chart(user_id):
 
    transactions = list_transactions(user_id)

    expense_categories = {}
    for transaction in transactions:
        print(f"Processing transaction: {transaction}")  
        if 'amount' in transaction and 'category' in transaction:
            amount = transaction['amount']
            category = transaction['category']
            
            if amount < 0:  
                if category in expense_categories:
                    expense_categories[category] += abs(amount)
                else:
                    expense_categories[category] = abs(amount)

    if not expense_categories:
        print("No expense data found.")  
        return None  

    print("Expense categories and amounts:", expense_categories) 

    plt.figure(figsize=(8, 8))
    plt.pie(expense_categories.values(), labels=expense_categories.keys(), autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    plt.title('Expense Breakdown by Category')

    plt.savefig('expense_pie_chart.png')  
    plt.show() 

if __name__ == "__main__":
    create_expense_pie_chart(1)
