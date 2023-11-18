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
        else:
            print("Insufficient balance")
            return False

    def check_balance(self):
        return self.balance


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def insert_card(self):
        pass  # Implement card insertion logic

    def enter_pin(self, pin):
        if int(pin) == self.bank_account.pin:
            return True
        else:
            return False

    def select_transaction(self, action, amount=0):
        match action:
            case "w":
                return self.bank_account.withdraw(amount)
            case "d":
                return self.bank_account.deposit()
            case "c":
                return self.bank_account.check_balance()
            case "q":
                return "transaction cancelled"
            case _:
                return "invalid action"

    def dispense_cash(self, amount):
        if self.bank_account.withdraw(amount) != False:
            print(f"Please take your cash: {amount}")
            print(f"Your new balance is: {self.bank_account.check_balance()}")
        else:
            print("Insufficient balance, transaction cancelled")

    def eject_card(self):
        pass  # Implement card ejection logic


# Main program
account = BankAccount("john", 1000, 123)  # Create a bank account with $1000
print(f"debug info: {account.name} {account.balance} {account.pin}")
atm = ATM(account)  # Insert the card into the ATM

while atm is not None:
    exit_flag = False
    atm.insert_card()

    # Enter pin logic
    inc_count = 0
    while True:
        pin = input(f"hi {account.name}, please enter your pin: ")
        if atm.enter_pin(pin):
            print("Pin accepted! \n")
            break
        else:
            inc_count += 1
            print("Incorrect pin. Please try again")
            if inc_count == 3:
                print("You have entered the wrong pin 3 times. Your card is shredded")
                exit_flag = True
                break

    # Exit the program if the card is shredded
    if exit_flag:
        break

    # Select transaction logic
    action = input(
        "What would you like to do? (withdraw(w)/deposit(d)/check_balance(c)/cancel_transaction(q)): "
    )
    match action:
        case "w":
            while True:
                try:
                    amount = int(input("How much would you like to withdraw? "))
                    break  # If the input is valid, break the loop
                except ValueError:
                    print("Please enter a valid amount")
                    # If the input is not valid, the loop will continue
            atm.select_transaction(action, int(amount))

    while atm.select_transaction(action) == "invalid action":
        action = input("What would you like to do? (withdraw/deposit/check_balance): ")
    if atm.select_transaction(action) == "transaction cancelled":
        break

    atm.dispense_cash(100)
    atm.eject_card()
    atm = None  # Stop the program
