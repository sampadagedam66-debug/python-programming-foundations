"""
banking.py

Project: Banking System
Covers: classes & objects | PIN-based authentication | fund transfers |
        in-session transaction history | file persistence (CSV) | menu-driven loop |
        basic exception handling
"""

import csv
import os

DATA_FILE = "bank_accounts.csv"


class Account:
    def __init__(self, account_number, holder_name, pin, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []  # session-only, not saved to file

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited Rs {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrew Rs {amount}")
        return True


class Bank:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.accounts = []
        self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = Account(
                    account_number=row["account_number"],
                    holder_name=row["holder_name"],
                    pin=row["pin"],
                    balance=float(row["balance"]),
                )
                self.accounts.append(account)

    def save_accounts(self):
        with open(self.data_file, "w", newline="") as file:
            fieldnames = ["account_number", "holder_name", "pin", "balance"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts:
                writer.writerow({
                    "account_number": account.account_number,
                    "holder_name": account.holder_name,
                    "pin": account.pin,
                    "balance": account.balance,
                })

    def generate_account_number(self):
        next_number = 1001 + len(self.accounts)
        return f"ACC{next_number}"

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def authenticate(self, account_number, pin):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return None
        if account.pin != pin:
            print("Incorrect PIN.")
            return None
        return account

    def create_account(self, holder_name, pin, initial_deposit):
        account_number = self.generate_account_number()
        new_account = Account(account_number, holder_name, pin, initial_deposit)
        self.accounts.append(new_account)
        print(f"Account created successfully! Your account number is {account_number}")

    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        account.deposit(amount)
        print(f"Rs {amount} deposited. New balance: Rs {account.balance}")

    def withdraw_from_account(self, account_number, pin, amount):
        account = self.authenticate(account_number, pin)
        if account is None:
            return

        success = account.withdraw(amount)
        if success:
            print(f"Rs {amount} withdrawn. New balance: Rs {account.balance}")
        else:
            print(f"Insufficient balance. Current balance: Rs {account.balance}")

    def check_balance(self, account_number, pin):
        account = self.authenticate(account_number, pin)
        if account is None:
            return
        print(f"Account Holder: {account.holder_name}")
        print(f"Current Balance: Rs {account.balance}")

    def transfer_funds(self, from_account_number, pin, to_account_number, amount):
        sender = self.authenticate(from_account_number, pin)
        if sender is None:
            return

        receiver = self.find_account(to_account_number)
        if receiver is None:
            print("Receiver account not found.")
            return

        if sender.account_number == receiver.account_number:
            print("Cannot transfer to the same account.")
            return

        if amount > sender.balance:
            print(f"Insufficient balance. Current balance: Rs {sender.balance}")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)
        sender.transaction_history.append(f"Transferred Rs {amount} to {receiver.account_number}")
        receiver.transaction_history.append(f"Received Rs {amount} from {sender.account_number}")
        print(f"Rs {amount} transferred to {receiver.account_number} successfully.")
        print(f"Your new balance: Rs {sender.balance}")

    def view_transaction_history(self, account_number, pin):
        account = self.authenticate(account_number, pin)
        if account is None:
            return

        if len(account.transaction_history) == 0:
            print("No transactions yet in this session.")
            return

        print(f"\nTransaction history for {account.account_number}:")
        for entry_number, entry in enumerate(account.transaction_history, start=1):
            print(f"  {entry_number}. {entry}")


def display_menu():
    print("\n----- BANKING SYSTEM -----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Funds")
    print("6. View Transaction History (this session)")
    print("7. Save & Exit")


def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            holder_name = input("Enter your name: ")
            pin = input("Set a 4-digit PIN: ")
            try:
                initial_deposit = float(input("Enter initial deposit amount: Rs "))
                bank.create_account(holder_name, pin, initial_deposit)
            except ValueError:
                print("Deposit amount must be a valid number. Account not created.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter deposit amount: Rs "))
                bank.deposit_to_account(account_number, amount)
            except ValueError:
                print("Deposit amount must be a valid number.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            try:
                amount = float(input("Enter withdrawal amount: Rs "))
                bank.withdraw_from_account(account_number, pin, amount)
            except ValueError:
                print("Withdrawal amount must be a valid number.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            bank.check_balance(account_number, pin)

        elif choice == "5":
            from_account = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            to_account = input("Enter receiver's account number: ")
            try:
                amount = float(input("Enter amount to transfer: Rs "))
                bank.transfer_funds(from_account, pin, to_account, amount)
            except ValueError:
                print("Transfer amount must be a valid number.")

        elif choice == "6":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            bank.view_transaction_history(account_number, pin)

        elif choice == "7":
            bank.save_accounts()
            print("Account data saved. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
