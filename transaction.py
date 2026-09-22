from decimal import Decimal, InvalidOperation
from database import get_connection


def deposit_money():
    account_id = int(input("Enter account ID: "))

    try:
        amount = Decimal(input("Enter deposit amount: "))
    except InvalidOperation:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute(
        """
        SELECT account_id, balance
        FROM accounts
        WHERE account_id = %s
        """,
        (account_id,)
    )

    account = cursor.fetchone()

    if account is None:
        print("Account not found.")
        cursor.close()
        connection.close()
        return

    cursor.execute(
        """
        UPDATE accounts
        SET balance = balance + %s
        WHERE account_id = %s
        """,
        (amount, account_id)
    )

    cursor.execute(
        """
        INSERT INTO transactions
        (account_id, transaction_type, amount)
        VALUES (%s, %s, %s)
        """,
        (account_id, "DEPOSIT", amount)
    )

    connection.commit()

    new_balance = account[1] + amount

    print("\nDeposit successful!")
    print("Deposited amount:", amount)
    print("New balance:", new_balance)

    cursor.close()
    connection.close()


def withdraw_money():
    account_id = int(input("Enter account ID: "))

    try:
        amount = Decimal(input("Enter withdrawal amount: "))
    except InvalidOperation:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT account_id, balance
        FROM accounts
        WHERE account_id = %s
        """,
        (account_id,)
    )

    account = cursor.fetchone()

    if account is None:
        print("Account not found.")
        cursor.close()
        connection.close()
        return

    current_balance = account[1]

    if amount > current_balance:
        print("\nInsufficient balance!")
        print("Current balance:", current_balance)

        cursor.close()
        connection.close()
        return

    cursor.execute(
        """
        UPDATE accounts
        SET balance = balance - %s
        WHERE account_id = %s
        """,
        (amount, account_id)
    )

    cursor.execute(
        """
        INSERT INTO transactions
        (account_id, transaction_type, amount)
        VALUES (%s, %s, %s)
        """,
        (account_id, "WITHDRAWAL", amount)
    )

    connection.commit()

    new_balance = current_balance - amount

    print("\nWithdrawal successful!")
    print("Withdrawn amount:", amount)
    print("New balance:", new_balance)

    cursor.close()
    connection.close()


def transaction_history():
    account_id = int(input("Enter account ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT account_id
        FROM accounts
        WHERE account_id = %s
        """,
        (account_id,)
    )

    account = cursor.fetchone()

    if account is None:
        print("Account not found.")
        cursor.close()
        connection.close()
        return

    cursor.execute(
        """
        SELECT
            transaction_id,
            transaction_type,
            amount,
            transaction_date
        FROM transactions
        WHERE account_id = %s
        ORDER BY transaction_date DESC
        """,
        (account_id,)
    )

    transactions = cursor.fetchall()

    print("\n========== TRANSACTION HISTORY ==========")

    if not transactions:
        print("No transactions found.")
    else:
        print(
            f"{'ID':<5}"
            f"{'TYPE':<15}"
            f"{'AMOUNT':<15}"
            f"{'DATE'}"
        )

        print("-" * 60)

        for transaction in transactions:
            print(
                f"{transaction[0]:<5}"
                f"{transaction[1]:<15}"
                f"{transaction[2]:<15}"
                f"{transaction[3]}"
            )

    print("=========================================")

    cursor.close()
    connection.close()
