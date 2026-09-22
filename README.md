# Banking Management System
A console-based Banking Management System developed using Python and MySQL.
The application allows users to manage customers, create bank accounts, perform deposits and withdrawals, check account balances, and view transaction history.

## Project Overview
The Banking Management System is a Python-based application connected to a MySQL relational database.
The project demonstrates how a Python application can interact with a database to perform CRUD operations and manage banking-related data.
The application provides a menu-driven interface for performing banking operations.

## Features
- Create customer
- Create Savings or Current account
- Deposit money
- Withdraw money
- Check account balance
- View transaction history
- Validate customer and account IDs
- Prevent withdrawals exceeding available balance
- Store transaction records in MySQL
- Handle invalid user input
- Secure database credentials using environment variables

## Technologies Used
- Python 3.12
- MySQL
- MySQL Connector/Python
- Python-dotenv
- SQL
- Git/GitHub

## Project Structure
BANKING_MGMT_SYSTEM/
│
├── account.py
├── customer.py
├── database.py
├── main.py
├── transaction.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md