class Bank:
    __set_of_user_accounts: set = set()

    @classmethod
    def get__set_of_user_accounts(cls):
        return cls.__set_of_user_accounts

    @classmethod
    def add_account_to_bank(cls, account):
        cls.__set_of_user_accounts.add(account)
