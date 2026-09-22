from database import get_connection


def create_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers (name, phone, email)
        VALUES (%s, %s, %s)
    """

    values = (name, phone, email)

    cursor.execute(query, values)
    connection.commit()

    print("\nCustomer created successfully!")
    print("Customer ID:", cursor.lastrowid)

    cursor.close()
    connection.close()