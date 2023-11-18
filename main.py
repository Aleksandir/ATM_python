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


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def enter_pin(self, pin):
        if int(pin) == self.bank_account.pin:
            return True
        else:
            return False


# Main program
# Create a bank account with $1000
# Insert the card into the ATM
account = BankAccount("john", 1000, 123)
atm = ATM(account)

print("Please insert your card")

inc_count = 0
while True:
    pin = input(f"hi {atm.bank_account.name}, please enter your pin: ")
    if atm.enter_pin(pin):
        print("Pin accepted!")
        break
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
        "\nWhat would you like to do? withdraw(w)/deposit(d)/check_balance(c)/quit and eject card(q): "
    )

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
            break
        case _:
            print("Invalid choice")
    if exit_flag:
        break
