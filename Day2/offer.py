bill = float(input("Enter bill amount: "))
membership = input("Are you a gold member? (yes/no): ").lower()
day = input("Enter day of visit (Monday-Sunday): ").lower()
if bill > 1000 and membership == "yes":
    weekend = ["saturday", "sunday"]
    if day in weekend:
        discount = bill * 0.20
        final_bill = bill - discount
        print(f"Original bill: Rs. {bill}")
        print(f"Discount (20%): Rs. {discount}")
        print(f"Final bill: Rs. {final_bill}")
    else:
        print(f"Final bill: Rs. {bill}")
        print(" offer not applicable")