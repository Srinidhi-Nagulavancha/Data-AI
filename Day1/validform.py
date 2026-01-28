import re
email = input("Enter your email: ")
password = input("Enter your password: ")
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(email_pattern, email):
    email_valid = True
else:
    email_valid = False
if len(password) >= 5:
    password_valid = True
else:
    password_valid = False
if email_valid and password_valid:
    print("Email and password are valid ✅")
else:
    if not email_valid:
        print("Invalid email format ❌")
    if not password_valid:
        print("Password must be at least 5 characters long ❌")
