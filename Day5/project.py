class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder 
        self.account_number = account_number 
        self._balance = initial_balance       
        self.__pin = "1234"                   
    def get_balance(self):
        return self._balance
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            return "✅ PIN changed successfully!"
        return "❌ PIN must be 4 digits!"
    def verify_pin(self, pin):
        return self.__pin == pin
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0):
        super().__init__(account_holder, account_number, initial_balance)
        self.min_balance = 500
        self.interest_rate = 0.05  
    def display_info(self):
        print("\n" + "="*40)
        print("SAVINGS ACCOUNT DETAILS")
        print("="*40)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"Minimum Balance: ${self.min_balance}")
        print(f"Interest Rate: {self.interest_rate*100}% per year")
        print(f"Interest Earned: ${self._balance * self.interest_rate:.2f}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0):
        super().__init__(account_holder, account_number, initial_balance)
        self.overdraft_limit = 1000
    def display_info(self):
        print("\n" + "="*40)
        print("CURRENT ACCOUNT DETAILS")
        print("="*40)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"Overdraft Limit: ${self.overdraft_limit}")
        print(f"Available Balance: ${self._balance + self.overdraft_limit:.2f}")
class BankingSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        print("\n" + "="*40)
        print("CREATE NEW ACCOUNT")
        print("="*40)
        
        name = input("Enter your full name: ")
        account_type = input("Enter account type (savings/current): ").lower()
        initial_deposit = float(input("Enter initial deposit: $"))
        account_number = input("Enter 5-digit account number: ")
        
        if account_number in self.accounts:
            return "❌ Account number already exists!"
        
        if account_type == "savings":
            account = SavingsAccount(name, account_number, initial_deposit)
        elif account_type == "current":
            account = CurrentAccount(name, account_number, initial_deposit)
        else:
            return "❌ Invalid account type!"
        
        self.accounts[account_number] = account
        return f"✅ Account created successfully!\nAccount Number: {account_number}"
    
    def deposit(self):
        print("\n" + "="*40)
        print("DEPOSIT MONEY")
        print("="*40)
        
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            return "❌ Account not found!"
        
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            return "❌ Amount must be positive!"
        
        pin = input("Enter your PIN: ")
        if not self.accounts[account_number].verify_pin(pin):
            return "❌ Invalid PIN!"
        
        self.accounts[account_number]._balance += amount
        return f"✅ ${amount:.2f} deposited successfully!\nNew Balance: ${self.accounts[account_number]._balance:.2f}"
    
    def withdraw(self):
        print("\n" + "="*40)
        print("WITHDRAW MONEY")
        print("="*40)
        
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            return "❌ Account not found!"
        
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            return "❌ Amount must be positive!"
        
        pin = input("Enter your PIN: ")
        if not self.accounts[account_number].verify_pin(pin):
            return "❌ Invalid PIN!"
        
        account = self.accounts[account_number]

        if isinstance(account, SavingsAccount):
            if account._balance - amount < account.min_balance:
                return f"❌ Cannot go below minimum balance of ${account.min_balance}!"
        elif isinstance(account, CurrentAccount):
            if account._balance - amount < -account.overdraft_limit:
                return f"❌ Exceeded overdraft limit of ${account.overdraft_limit}!"
        
        account._balance -= amount
        return f"✅ ${amount:.2f} withdrawn successfully!\nNew Balance: ${account._balance:.2f}"
    
    def check_balance(self):
        account_number = input("\nEnter account number: ")
        if account_number not in self.accounts:
            return "❌ Account not found!"
        
        pin = input("Enter your PIN: ")
        if not self.accounts[account_number].verify_pin(pin):
            return "❌ Invalid PIN!"
        
        self.accounts[account_number].display_info()
        return ""
class Transaction:
    def process(self, amount, *args):
        if len(args) == 0:
            return f"Processing payment of ${amount}"
        elif len(args) == 1:
            return f"Processing transfer of ${amount} to account {args[0]}"
        elif len(args) == 2:
            return f"Processing transfer of ${amount} to {args[0]} (Account: {args[1]})"
        else:
            return f"Processing transaction of ${amount} with details: {args}"
def main():
    bank = BankingSystem()
    transaction = Transaction()
    
    while True:
        print("\n" + "="*40)
        print("🏦 WELCOME TO PYTHON BANK")
        print("="*40)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Change PIN")
        print("6. Process Transaction (Overloading Demo)")
        print("7. View All Accounts")
        print("8. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            result = bank.create_account()
            print(result)
        
        elif choice == "2":
            result = bank.deposit()
            print(result)
        
        elif choice == "3":
            result = bank.withdraw()
            print(result)
        
        elif choice == "4":
            result = bank.check_balance()
            if result:
                print(result)
        
        elif choice == "5":
            print("\n" + "="*40)
            print("CHANGE PIN")
            print("="*40)
            account_number = input("Enter account number: ")
            if account_number in bank.accounts:
                old_pin = input("Enter current PIN: ")
                if bank.accounts[account_number].verify_pin(old_pin):
                    new_pin = input("Enter new 4-digit PIN: ")
                    result = bank.accounts[account_number].set_pin(new_pin)
                    print(result)
                else:
                    print("❌ Invalid current PIN!")
            else:
                print("❌ Account not found!")
        
        elif choice == "6":
            print("\n" + "="*40)
            print("METHOD OVERLOADING DEMONSTRATION")
            print("="*40)
            amount = float(input("Enter amount: $"))
            print("\nChoose transaction type:")
            print("1. Simple Payment")
            print("2. Transfer to Account")
            print("3. Transfer with Name")
            
            trans_choice = input("Enter choice (1-3): ")
            if trans_choice == "1":
                print(transaction.process(amount))
            elif trans_choice == "2":
                acc_num = input("Enter account number: ")
                print(transaction.process(amount, acc_num))
            elif trans_choice == "3":
                name = input("Enter recipient name: ")
                acc_num = input("Enter account number: ")
                print(transaction.process(amount, name, acc_num))
        
        elif choice == "7":
            print("\n" + "="*40)
            print("ALL BANK ACCOUNTS")
            print("="*40)
            if not bank.accounts:
                print("No accounts found!")
            else:
                for acc_num, account in bank.accounts.items():
                    account.display_info()
                    print()
        
        elif choice == "8":
            print("\nThank you for banking with us! 👋")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-8")
        
        input("\nPress Enter to continue...")
if __name__ == "__main__":
    main()