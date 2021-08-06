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
        return str()

    def create_account_for_new_user(self) -> Account:
        new_account = self.account_number_generator()
        return new_account

    def account_number_generator(self):
        account_number = str(uuid.uuid4().int)[:11]
        new_account = Account(account_number)
        return new_account

    def add_new_user(self, user):
        self.__bank.add_new_account(user)

    def find_user_by_email(self, email):
        for user in self.__bank.get__set_of_user_accounts:
            if user.get_email == email:
                return user
        return None

    def create_account_for_existing_user(self):
        new_account = self.account_number_generator()
        return new_account
