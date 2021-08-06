from decimal import Decimal


def set_account_pin():
    # pin = input("Set Account Pin: ")
    pin = "1234"
    return pin


class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__pin = set_account_pin()
        self.__transactions = list()

    @property
    def get_account_number(self):
        return self.__account_number

    @property
    def get_account_pin(self):
        return self.__pin

    def add_new_transaction(self, new_transaction):
        self.__transactions.append(new_transaction)

    @property
    def get_account_balance(self):
        balance: Decimal = Decimal(0)
        for transaction in self.__transactions:
            balance = balance + transaction[1]
        return balance

    def __str__(self):
        return self.__account_number
