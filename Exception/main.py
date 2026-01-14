import sys


# -------- Custom Exceptions --------
class ATMError(Exception):
    """Base exception for ATM errors."""


class InvalidPinError(ATMError):
    pass


class InsufficientBalanceError(ATMError):
    pass


class InvalidAmountError(ATMError):
    pass


# -------- Utility Functions --------
def read_int(prompt: str) -> int:
    """Safely read an integer from user."""
    try:
        return int(input(prompt))
    except ValueError:
        raise InvalidAmountError("Please enter a valid number.")


# -------- ATM Operations --------
def authenticate(correct_pin: int, attempts: int = 3) -> None:
    """Authenticate user PIN."""
    for attempt in range(1, attempts + 1):
        pin = read_int("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("PIN verified.\n")
            return

        remaining = attempts - attempt
        if remaining > 0:
            print(f"Incorrect PIN. Attempts left: {remaining}\n")

    raise InvalidPinError("Card blocked due to multiple incorrect PIN attempts.")


def withdraw(balance: int) -> int:
    """Withdraw amount and return updated balance."""
    amount = read_int("Enter amount to withdraw: ")

    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be greater than zero.")

    if amount % 100 != 0:
        raise InvalidAmountError("Amount must be in multiples of 100.")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    balance -= amount
    print(f"\nWithdrawal successful. Amount: {amount}")
    print(f"Remaining balance: {balance}\n")
    return balance


def deposit(balance: int) -> int:
    """Deposit money and return updated balance."""
    amount = read_int("Enter amount to deposit: ")

    if amount <= 0:
        raise InvalidAmountError("Deposit amount must be greater than zero.")

    balance += amount
    print(f"\nDeposit successful. Amount: {amount}")
    print(f"Updated balance: {balance}\n")
    return balance


# -------- Main Program --------
def main():
    correct_pin = 1234
    balance = 10000

    print("----- Welcome to ATM -----\n")

    try:
        authenticate(correct_pin)
    except InvalidPinError as err:
        print(err)
        sys.exit(0)

    while True:
        try:
            print("ATM Menu")
            print("1. Withdraw")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Exit\n")

            choice = read_int("Enter your choice (1-4): ")
            print()

            if choice == 1:
                balance = withdraw(balance)
            elif choice == 2:
                print(f"Your current balance is: {balance}\n")
            elif choice == 3:
                balance = deposit(balance)
            elif choice == 4:
                print("Thank you for using ATM. Goodbye.")
                break
            else:
                print("Invalid choice. Please select 1 to 4.\n")

        except InvalidAmountError as err:
            print(f"Error: {err}\n")

        except InsufficientBalanceError as err:
            print(f"Error: {err}\n")

        except ATMError as err:
            print(f"ATM error: {err}\n")

        except Exception as err:
            # Catch unexpected bugs
            print("Unexpected system error:", err)
            break


if __name__ == "__main__":
    main()
