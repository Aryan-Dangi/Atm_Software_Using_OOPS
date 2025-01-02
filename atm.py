import sys

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, pin)
            return True
        return False

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def start(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                account_number = input("Enter a new account number: ")
                pin = input("Set a 4-digit PIN: ")
                if self.create_account(account_number, pin):
                    print("Account created successfully.")
                else:
                    print("Account number already exists.")

            elif choice == '2':
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                account = self.authenticate(account_number, pin)

                if account:
                    while True:
                        print("\n1. Check Balance")
                        print("2. Deposit Money")
                        print("3. Withdraw Money")
                        print("4. Exit")
                        sub_choice = input("Choose an option: ")

                        if sub_choice == '1':
                            print(f"Your balance is: {account.check_balance()}")

                        elif sub_choice == '2':
                            try:
                                amount = float(input("Enter amount to deposit: "))
                                if account.deposit(amount):
                                    print("Deposit successful.")
                                else:
                                    print("Invalid amount.")
                            except ValueError:
                                print("Please enter a valid number.")

                        elif sub_choice == '3':
                            try:
                                amount = float(input("Enter amount to withdraw: "))
                                if account.withdraw(amount):
                                    print("Withdrawal successful.")
                                else:
                                    print("Insufficient funds or invalid amount.")
                            except ValueError:
                                print("Please enter a valid number.")

                        elif sub_choice == '4':
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Authentication failed.")

            elif choice == '3':
                print("Thank you for using the ATM.")
                break
                

            else:
                print("Invalid option.")

atm = ATM()
atm.start()
