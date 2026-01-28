recharge = int(input("Enter recharge amount: "))
databalance = int(input("Enter current data balance in MB: "))
if recharge >= 399 and databalance >=2:
    print("You are eligible for 2GB bonus data")
else:
    print("You are not eligible for bonus data")
    