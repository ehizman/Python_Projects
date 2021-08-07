class AccountRepository:
    def __init__(self):
        self.__list_of_accounts: list = list()

    @property
    def get__list_of_accounts(self):
        return self.__list_of_accounts

    def save_account_to_repository(self, new_account):
        self.__list_of_accounts.append(new_account)