import sqlite3

conn = sqlite3.connect("financial_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT NOT NULL,
        category_id INTEGER NOT NULL,  -- Updated column name
        description TEXT,
        amount REAL
    )
''')
conn.commit()

def add_transaction(user_id, date, category, description, amount):
    
    cursor.execute("INSERT INTO transactions (user_id, date, category_id, description, amount) VALUES (?, ?, ?, ?, ?)",
                   (user_id, date, category, description, amount))  # Updated column name to category_id
    conn.commit()
    return True

def list_transactions(user_id):
    
    cursor.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
    transactions = cursor.fetchall()

    transaction_list = []
    for transaction in transactions:
        transaction_dict = {
            "id": transaction[0],
            "user_id": transaction[1],
            "date": transaction[2],
            "category_id": transaction[3],  # Updated column name to category_id
            "description": transaction[4],
            "amount": transaction[5]
        }
        transaction_list.append(transaction_dict)

    return transaction_list

def calculate_total_expenses(user_id):
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id=? AND amount < 0", (user_id,))
    total_expenses = cursor.fetchone()[0] or 0.0

    return round(total_expenses, 2)

def calculate_total_income(user_id):
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id=? AND amount > 0", (user_id,))
    total_income = cursor.fetchone()[0] or 0.0

    return round(total_income, 2)

if __name__ == "__main__":
    conn.close()
