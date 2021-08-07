from decimal import Decimal


class Account:
    def __init__(self, name, initial_deposit):
        if initial_deposit < 0.0:
            raise ValueError("Invalid deposit amount")
        else:
            self.balance = initial_deposit
            self.name = name

    def deposit(self, deposit_amount):
        if deposit_amount < 0.0:
            raise ValueError("Invalid amount!")
        else:
            self.balance += deposit_amount
            print(f"${deposit_amount} has been deposited successfully into account")

    def withdraw(self, amount_to_withdraw):
        if 0.0 < amount_to_withdraw <= self.balance:
            self.balance -= amount_to_withdraw
            print(f"f${amount_to_withdraw} has successfully been withdrawn form account")
        else:
            raise ValueError("Invalid amount")
