import authentication

username = "test_user"
password = "test_password"

if authentication.register_user(username, password):
    print(f"User '{username}' registered successfully.")
else:
    print(f"User '{username}' already exists. Registration failed.")

login_username = "test_user"
login_password = "test_password"

user_data = authentication.login_user(login_username, login_password)

if user_data:
    user_id, stored_username, stored_password = user_data
    print(f"Login successful for user '{stored_username}' (User ID: {user_id}).")
else:
    print("Login failed. Please check your credentials.")
