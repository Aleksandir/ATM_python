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

    def check_balance(self):
        return self.balance


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def insert_card(self):
        pass  # Implement card insertion logic

    def enter_pin(self, pin):
        self.inc_count = 0
        if pin == self.bank_account.pin:
            return True
        else:
            return False

    def select_transaction(self):
        pass  # Implement transaction selection logic

    def dispense_cash(self, amount):
        self.bank_account.withdraw(amount)

    def eject_card(self):
        pass  # Implement card ejection logic


# Main program
account = BankAccount("john", 1000, 123)  # Create a bank account with $1000
atm = ATM(account)  # Insert the card into the ATM

while atm is not None:
    atm.insert_card()

    pin = input(f"hi {account.name}, please enter your pin: ")
    inc_count = 0
    while not atm.enter_pin(pin):
        if inc_count < 3:
            inc_count += 1
            print("Incorrect pin. Please try again")
        if inc_count == 3:
            print("You have entered the wrong pin 3 times. Your card is shredded")
            break
        pin = input(f"hi {account.name}, please enter your pin: ")

    atm.select_transaction()
    atm.dispense_cash(100)
    atm.eject_card()
    atm = None  # Stop the program
