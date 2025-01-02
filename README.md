This program simulates an ATM system using object-oriented programming principles in Python. 
It allows users to create accounts, access accounts, and perform standard banking operations like checking balances, depositing money, and withdrawing funds.
Classes Used
1. Account Class
Represents an individual bank account.
Attributes:
account_number: A unique identifier for the account.
pin: A 4-digit PIN for secure authentication.
balance: The current balance of the account.
Methods:
check_balance(): Returns the current balance.
deposit(amount): Adds a specified amount to the balance if valid.
withdraw(amount): Deducts a specified amount from the balance if sufficient funds are available.
2. ATM Class
Manages the overall ATM system and user interactions.
Attributes:
accounts: A dictionary to store Account objects, keyed by account number.
Methods:
create_account(account_number, pin): Creates a new account with the provided account number and PIN.
authenticate(account_number, pin): Verifies the provided account number and PIN and returns the corresponding account object if valid.
start(): The main method to launch the ATM interface, handle user input, and manage operations.
