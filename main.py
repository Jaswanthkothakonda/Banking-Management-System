from customer import create_customer
from account import create_account, check_balance
from transaction import deposit_money, withdraw_money, transaction_history


def display_menu():
    print("\n")
    print("=" * 45)
    print("       BANKING MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_customer()

        elif choice == "2":
            create_account()

        elif choice == "3":
            deposit_money()

        elif choice == "4":
            withdraw_money()

        elif choice == "5":
            check_balance()

        elif choice == "6":
            transaction_history()

        elif choice == "7":
            print("\nThank you for using our Banking Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice.")
            print("Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()