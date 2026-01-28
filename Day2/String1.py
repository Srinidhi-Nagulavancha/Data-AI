full_name = input("Enter full name: ")
parts = full_name.split()
if len(parts) >= 2:
    first_char = parts[0][0].upper()
    last_char = parts[-1][0].upper()
    result = first_char + last_char
    print(result)
else:
    print("Please enter a full name with at least first and last name")