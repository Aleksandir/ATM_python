import json
import sys


class BankAccount:
    def __init__(self, name, balance=0, pin=0):
        self.balance = balance
        self.name = name
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance


# TODO refactor ATM class to take in file, and update file on exit
# ATM should hold onto the file so it only has to read once, find the account and create an account class for it
# research if we can save the file so it does not have to be read every time
class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def enter_pin(self, pin):
        if int(pin) == self.bank_account.pin:
            return True
        else:
            return False


# Main program
name = input("Please enter your name: ").lower()

with open("accounts.json", "r") as f:
    accounts = json.load(f)

    account = None
    for acc in accounts:
        if acc["name"] == name:
            account = BankAccount(name, acc["balance"], int(acc["pin"]))
            break

    if account is None:
        print("Account not found")
        new_account = input("Would you like to create a new account? (y/n) ").lower()
        if new_account == "y":
            pin = input("Please enter a pin: ")
            account = BankAccount(name, 0, int(pin))
            accounts.append(
                {"name": name, "balance": account.balance, "pin": str(account.pin)}
            )
            print("Account created!")
        else:
            sys.exit()

print(f"debug info: {account.name} {account.balance} {account.pin}")
atm = ATM(account)

print("Please insert your card\n")

inc_count = 0
while True:
    pin = input(
        f"hi {atm.bank_account.name.capitalize()}, please enter your pin (q to quit): "
    )
    if atm.enter_pin(pin):
        print("Pin accepted!")
        break
    elif pin == "q":
        print("Thank you for using our ATM")
        sys.exit()
    else:
        inc_count += 1
        print("Incorrect pin. Please try again")
        if inc_count == 3:
            print("You have entered the wrong pin 3 times. Your card is shredded")
            sys.exit()

while True:
    exit_flag = False
    # Rest of your code

    # Select transaction logic
    action = input(
        """
Please select a transaction:
w - withdraw
d - deposit
c - check_balance
q - quit and eject card
=> """
    ).lower()

    match action:
        case "w":
            # withdraw
            while True:
                try:
                    amount = int(input("How much would you like to withdraw? "))
                    break  # If the input is valid, break the loop
                except ValueError:
                    print("Please enter a valid amount")
                    # If the input is not valid, the loop will continue
            if atm.bank_account.withdraw(amount):
                print(f"Please take your cash: ${amount}")
                print(f"Your new balance is: ${atm.bank_account.check_balance()}")
            else:
                print(
                    f"Insufficient funds, your current balance is: ${atm.bank_account.check_balance()}"
                )
        case "d":
            # deposit
            while True:
                try:
                    amount = int(input("How much would you like to deposit? "))
                    break  # If the input is valid, break the loop
                except ValueError:
                    print("Please enter a valid amount")
                    # If the input is not valid, the loop will continue
            atm.bank_account.deposit(amount)
            print(f"We have now deposited ${amount} into your account")
            print(f"Your new balance is: ${atm.bank_account.check_balance()}")
        case "c":
            # check balance
            print(f"Your current balance is: ${atm.bank_account.check_balance()}")
        case "q":
            # quit and eject card
            exit_flag = True
            print("Thank you for using our ATM")
            print("Please take your card")
        case _:
            print("Invalid choice")
    if exit_flag:
        with open("accounts.json", "w") as f:
            for acc in accounts:
                if acc["name"] == name:
                    acc["balance"] = atm.bank_account.balance
                    break
            else:
                # for debugging purposes
                print("Account not found.")
            # write the updated accounts list to the file
            json.dump(accounts, f, indent=4)
        break
