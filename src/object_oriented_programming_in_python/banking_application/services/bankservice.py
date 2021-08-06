import uuid
from object_oriented_programming_in_python.banking_application.account import Account
from object_oriented_programming_in_python.banking_application.models.bank import Bank


class BankService:
    def __init__(self):
        self.__bank = Bank()

    def view_all_accounts(self) -> set:
        return self.__bank.get__set_of_user_accounts

    def find_user_by_account_number(self, account_number) -> str:
        for user in self.__bank.get__set_of_user_accounts:
            if account_number in user.get__accounts:
                return user

    def create_account(self) -> str:
        account_number = str(uuid.uuid4().int)[:11]
        new_account = Account(account_number)
        return account_number

    def add_new_user(self, user):
        self.__bank.add_new_account(user)
