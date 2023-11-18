class BankAccount:
    def __init__(self, name, balance=0, pin=0):
        self.balance = balance

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

    def enter_pin(self):
        pass  # Implement PIN entry logic

    def select_transaction(self):
        pass  # Implement transaction selection logic

    def dispense_cash(self, amount):
        self.bank_account.withdraw(amount)

    def eject_card(self):
        pass  # Implement card ejection logic


# Main program
account = BankAccount("john", 1000, 123)  # Create a bank account with $1000
atm = ATM(account)  # Insert the card into the ATM
# Continue with the rest of the simulation
