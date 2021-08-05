import uuid
from object_oriented_programming_in_python.banking_application.account import Account
from object_oriented_programming_in_python.banking_application.models.bank import Bank


class BankService:

    @classmethod
    def view_all_accounts(cls) -> set:
        return Bank.get__set_of_user_accounts()

    @classmethod
    def find_user_by_account_number(cls, account_number) -> str:
        for user in Bank.get__set_of_user_accounts():
            if account_number in user.get__accounts:
                return user.__str__()

    @classmethod
    def create_account(cls) -> str:
        account_number = str(uuid.uuid4().int)[:11]
        newAccount: Account = Account(account_number)
        Bank.add_account_to_bank(newAccount)
        return account_number
