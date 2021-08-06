class Bank:
    __set_of_user_accounts: set = set()

    @property
    def get__set_of_user_accounts(self):
        return self.__set_of_user_accounts

    def add_new_account(self, user):
        return self.__set_of_user_accounts.add(user)


