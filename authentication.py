import sqlite3
import hashlib


conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

def register_user(username, password):
    
    
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return False 

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    return True

def login_user(username, password):
    

    cursor.execute("SELECT id, username, password FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()

    if user_data:
        user_id, stored_username, stored_password = user_data
    else:
        return None  

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == stored_password:
        return user_id, stored_username, stored_password  
    else:
        return None 

if __name__ == "__main__":
    conn.close()
