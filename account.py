from decimal import Decimal, InvalidOperation
from database import get_connection


def create_account():
    try:
        customer_id = int(input("Enter customer ID: "))
    except ValueError:
        print("Invalid customer ID. Please enter a number.")
        return

    account_type = input(
        "Enter account type (Savings/Current): "
    ).strip().title()

    if account_type not in ["Savings", "Current"]:
        print("Invalid account type. Please choose Savings or Current.")
        return

    try:
        initial_balance = Decimal(
            input("Enter initial balance: ")
        )
    except InvalidOperation:
        print("Invalid balance. Please enter a valid number.")
        return

    if initial_balance < 0:
        print("Initial balance cannot be negative.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    # Check whether customer exists
    cursor.execute(
        """
        SELECT customer_id
        FROM customers
        WHERE customer_id = %s
        """,
        (customer_id,)
    )

    customer = cursor.fetchone()

    if customer is None:
        print("Customer not found.")
        cursor.close()
        connection.close()
        return

    # Create account
    cursor.execute(
        """
        INSERT INTO accounts
        (customer_id, account_type, balance)
        VALUES (%s, %s, %s)
        """,
        (customer_id, account_type, initial_balance)
    )

    connection.commit()

    print("\nAccount created successfully!")
    print("Account ID:", cursor.lastrowid)

    cursor.close()
    connection.close()


def check_balance():
    try:
        account_id = int(input("Enter account ID: "))
    except ValueError:
        print("Invalid account ID. Please enter a number.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            account_id,
            customer_id,
            account_type,
            balance
        FROM accounts
        WHERE account_id = %s
        """,
        (account_id,)
    )

    account = cursor.fetchone()

    if account is None:
        print("Account not found.")
    else:
        print("\n========== ACCOUNT DETAILS ==========")
        print("Account ID   :", account[0])
        print("Customer ID  :", account[1])
        print("Account Type :", account[2])
        print("Balance      :", account[3])
        print("=====================================")

    cursor.close()
    connection.close()