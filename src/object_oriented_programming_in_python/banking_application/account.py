def set_account_pin():
    # pin = input("Set Account Pin: ")
    pin = "1234"
    return pin


class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__pin = set_account_pin()

    @property
    def get_account_number(self):
        return self.__account_number

    @property
    def get_account_pin(self):
        return self.__pin

    def __str__(self):
        return self.__account_number

