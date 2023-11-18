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
        inc_count = 0

        while True:
            self.pin = input(f"hi {account.name}, please enter your pin: ")
            if atm.enter_pin(self.pin):
                print("Pin accepted! \n")
                break
            else:
                inc_count += 1
                print("Incorrect pin. Please try again")
                if inc_count == 3:
                    print(
                        "You have entered the wrong pin 3 times. Your card is shredded"
                    )
                    return True

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
        print("Card ejected")
        print("Thank you for using our ATM")
        return True


# Main program
# Create a bank account with $1000
# Insert the card into the ATM
account = BankAccount("john", 1000, 123)
# ! Debug info, remove later
print(f"debug info: {account.name} {account.balance} {account.pin}")
atm = ATM(account)

print("Please insert your card")
card_validated = atm.insert_card()

# TODO - add card insertion logic
# while not card_validated:
#     print("Invalid card. Please insert your card again")
#     card_validated = atm.insert_card()

while True:
    exit_flag = False
    # Rest of your code

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
        case "d":
            pass
        case "c":
            while True:
                withdraw_value = input("How much would you like to withdraw? ")
                if withdraw_value.isdigit():
                    atm.dispense_cash(int(withdraw_value))
                    break
                else:
                    print("Invalid input. Please enter a number.")

    while atm.select_transaction(action) == "invalid action":
        action = input("What would you like to do? (withdraw/deposit/check_balance): ")
    if atm.select_transaction(action) == "transaction cancelled":
        break

    stop = input("Would you like to continue? (y/n): ")
    if stop == "n":
        exit_flag = atm.eject_card()
    if exit_flag:
        break
