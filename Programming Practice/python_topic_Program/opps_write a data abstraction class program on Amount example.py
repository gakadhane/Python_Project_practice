from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class SavingsAccount(Account):
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid or insufficient funds for withdrawal")

    def get_balance(self):
        return self._balance


# Create an instance of SavingsAccount
account = SavingsAccount(1000)

# Demonstrate data abstraction
account.deposit(500)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1500
account.withdraw(200)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1300

# Explanation:
# Abstract Base Class Account:
# Account is an abstract base class (ABC) that defines three abstract methods: deposit, withdraw, and get_balance.
# These methods must be implemented by any subclass inheriting from Account.
#
# Concrete Class SavingsAccount:
# SavingsAccount is a concrete class that inherits from the Account class and provides implementations for the abstract methods.
# The __init__ method initializes the account with an initial balance.
# The deposit method adds the specified amount to the balance if the amount is valid.
# The withdraw method subtracts the specified amount from the balance if there are sufficient funds.
# The get_balance method returns the current balance.
#
# Instance Creation and Demonstration:
# An instance of SavingsAccount is created with an initial balance of 1000.
# The deposit method is called to add 500 to the balance.
# The get_balance method is called to retrieve the current balance.
# The withdraw method is called to subtract 200 from the balance.
# The get_balance method is called again to retrieve the updated balance.
#
# This example demonstrates data abstraction by defining an abstract base class with abstract methods
# and providing specific implementations in a concrete subclass. The internal details of the account
# (e.g., balance calculation) are hidden, and only the essential operations are exposed.
