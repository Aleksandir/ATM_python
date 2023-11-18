# ATM Simulation

This is a simple Python program designed to simulate an ATM (Automated Teller Machine). The purpose of this project is to learn and understand the principles of Object-Oriented Programming (OOP).

## Classes

The program consists of two main classes:

1. `BankAccount`: This class represents a bank account with basic functionalities like deposit, withdraw, and check balance.

2. `ATM`: This class represents the ATM machine. It uses the `BankAccount` class and provides functionalities like insert card, enter pin, select transaction, dispense cash, and eject card.

## Usage

To use this program, create instances of the `BankAccount` and `ATM` classes and simulate transactions. The main program in [main.py](main.py) demonstrates how to use these classes. It creates a `BankAccount` instance, inserts the card into the `ATM`, and then enters a loop where the user can enter their pin, select a transaction (withdraw, deposit, check balance), and quit the program.

## Future Improvements

This is a basic implementation and does not include features like multiple accounts, account holders, transaction history, etc. These could be added in the future to make the simulation more realistic.

## License

This project is open source and available under the [MIT License](LICENSE).
