import re
username = input("Enter your username: ")
password = input("Enter your password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password")
