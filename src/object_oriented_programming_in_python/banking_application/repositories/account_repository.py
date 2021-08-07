from typing import Optional

from object_oriented_programming_in_python.banking_application.models.account import Account


class AccountRepository:
    def __init__(self):
        self.__list_of_accounts: list = list()

    @property
    def get__list_of_accounts(self):
        return self.__list_of_accounts

    def save_account_to_repository(self, new_account):
        self.__list_of_accounts.append(new_account)

    def find_account_with_number(self, account_number: str) -> Optional[Account]:
        for account in self.__list_of_accounts:
            if account.get_account_number == account_number:
                return account
        return None
