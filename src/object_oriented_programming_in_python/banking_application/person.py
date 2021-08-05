from object_oriented_programming_in_python.banking_application.services.bankservice import BankService


class Person:
    def __init__(self, first_name, last_name, email):
        self.__list_of_accounts = list()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        account_number = BankService.create_account()
        self.__list_of_accounts.append(account_number)

    @property
    def get_first_name(self) -> str:
        return self.__first_name

    @property
    def get_last_name(self):
        return self.__last_name

    @property
    def get_email(self):
        return self.__email

    @property
    def get__accounts(self):
        return self.__list_of_accounts

    def __str__(self):
        return f"""First Name -> {self.__first_name}
Last Name -> {self.__last_name}
Email -> {self.__email}
Account Number -> {self.__list_of_accounts[0]}"""
