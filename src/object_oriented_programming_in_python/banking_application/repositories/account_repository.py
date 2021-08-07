from typing import Optional

from object_oriented_programming_in_python.banking_application.models.account import Account


class AccountRepository:
    __list_of_accounts: list = list()

    def __init__(self):
        pass

    @property
    def get__list_of_accounts(self):
        return

    def save_account_to_repository(self, new_account: Account):
        self.__list_of_accounts.append(new_account)

    def find_account_with_number(self, account_number: str) -> Optional[Account]:
        for account in self.__list_of_accounts:
            if account.get_account_number == account_number:
                return account
        return None
