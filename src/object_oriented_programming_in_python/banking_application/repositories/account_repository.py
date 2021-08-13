from typing import Optional

from object_oriented_programming_in_python.banking_application.models.account import Account


class AccountRepository:
    __list_of_accounts: list = list()
    __f = open("account.csv", mode='a+', encoding='utf-8')

    def __init__(self):
        pass

    @property
    def get__list_of_accounts(self):
        self.__f.seek(0)
        print(self.__f.readlines())
        return self.__list_of_accounts

    def save_account_to_repository(self, new_account: Account):
        self.__f.write(new_account.get_account_number + "\n")
        self.__list_of_accounts.append(new_account)

    def find_account_with_number(self, account_number: str) -> Optional[Account]:
        for account in self.__list_of_accounts:
            if account.get_account_number == account_number:
                return account
        return None
