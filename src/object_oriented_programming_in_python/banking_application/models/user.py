from object_oriented_programming_in_python.banking_application.models.account import Account


class User:
    def __init__(self, first_name, last_name, email):
        self.__list_of_accounts = list()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

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
    def get__accounts(self) -> list:
        return self.__list_of_accounts

    def update_user_accounts(self, account: Account):
        self.__list_of_accounts.append(account)

    def __str__(self):
        return f"""First Name -> {self.__first_name}
Last Name -> {self.__last_name}
Email -> {self.__email}
Accounts -> {self.__list_of_accounts}"""
