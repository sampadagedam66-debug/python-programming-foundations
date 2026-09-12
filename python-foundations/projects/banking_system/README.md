# Banking System

A console-based banking system built in Python. Supports account creation, PIN-protected transactions, and fund transfers between accounts, with balances saved to a CSV file between runs.

## Features
- Create a new account with an auto-generated account number (e.g. `ACC1001`)
- Deposit money into any account
- Withdraw money — requires correct PIN, blocks withdrawal if funds are insufficient
- Check balance — requires correct PIN
- Transfer funds between two accounts — requires sender's PIN, blocks self-transfers and insufficient balance
- View transaction history for the current session (deposits, withdrawals, transfers)
- Balances automatically saved to `bank_accounts.csv` on exit, reloaded on next run

## Concepts Used
- Object-Oriented Programming (`Account` and `Bank` classes)
- PIN-based authentication for sensitive actions
- File handling with CSV for balance persistence
- Menu-driven program loop
- Conditional logic for transaction validation
- Exception handling for invalid numeric input

## How to Run
```
python banking.py
```

## Project Structure
```
banking_system/
├── banking.py
├── bank_accounts.csv   (created automatically after first run)
└── README.md
```

## Known Limitations / Future Improvements
- Transaction history is session-only and resets when the program closes — not yet persisted to file
- PINs are stored in plain text in the CSV file — fine for a learning project, but not how real banking systems would handle it
