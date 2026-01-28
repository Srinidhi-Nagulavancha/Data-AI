correct_username = "admin"
correct_password = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect credentials. Attempts remaining: {remaining}")
        else:
            print("Account is blocked! Too many failed attempts.")