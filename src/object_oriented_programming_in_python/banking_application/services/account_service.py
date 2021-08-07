import uuid
from decimal import Decimal

from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_account_exception import \
    InvalidAccountException
from object_oriented_programming_in_python.banking_application.exceptions.transaction_exceptions.invalid_deposit_amount_exception import \
    InvalidDepositAmountException
from object_oriented_programming_in_python.banking_application.models.account import Account
from object_oriented_programming_in_python.banking_application.repositories.account_repository import AccountRepository
from object_oriented_programming_in_python.banking_application.services.transaction_service import TransactionService


# def withdraw(account, amount_to_withdraw):
#     if amount_to_withdraw < 0.0 or amount_to_withdraw > account.get_transactions_on_this:
#         raise InvalidWithdrawalAmountException("Invalid withdrawal amount")
#     else:
#         transaction = ("WITHDRAWAL", Decimal(-amount_to_withdraw), datetime.datetime.now())
#         account.add_new_transaction(transaction)
#
#
# def get_account_balance(account):
#     balance: Decimal = Decimal(0)
#     for transaction_id in account.__transactions:
#         balance = balance + transaction_service.get_transactions_on_this()
#     return balance


def _account_generator():
    account_number = str(uuid.uuid4().int)[:11]
    return account_number


class AccountService:
    def __init__(self):
        self.__account_repository = AccountRepository()
        self.__transaction_service = TransactionService()

    def create_account(self) -> Account:
        newly_generated_account_number: str = _account_generator()
        new_account: Account = Account(newly_generated_account_number)
        self.__account_repository.save_account_to_repository(new_account)
        return new_account

    def deposit(self, account_number: str, amount_to_deposit: Decimal, message: str):
        if amount_to_deposit < 0.0:
            raise InvalidDepositAmountException("Invalid deposit amount")
        else:
            account: Account = self.__account_repository.find_account_with_number(account_number)
            if account is not None:
                transaction_id: str = self.__transaction_service.create_new_deposit_transaction(account_number,
                                                                                                amount_to_deposit,
                                                                                                message)
                account.add_new_transaction_to_account(transaction_id)
            else:
                raise InvalidAccountException("Account does not exist")

    # def view_all_accounts(self) -> set:
    #     return self.__bank.get__set_of_user_accounts
    #
    # def find_user_by_account_number(self, account_number) -> str:
    #     for user in self.__bank.get__set_of_user_accounts:
    #         if account_number in user.get__accounts:
    #             return user
    #     return str()
    #
    # def add_new_user(self, user):
    #     self.__bank.add_new_account(user)
    #
    # def find_user_by_email(self, email):
    #     for user in self.__bank.get__set_of_user_accounts:
    #         if user.get_email == email:
    #             return user
    #     return None

    def update_list_of_customer_accounts(self, account_number):
        self.__account_repository.get__list_of_accounts.append(account_number)

    def find_balance_on(self, account_number: str) -> Decimal:
        list_of_transactions_on_account_number: list = self.__transaction_service.get_transactions_on_this \
            (account_number)
        balance = Decimal("0")
        for transaction in list_of_transactions_on_account_number:
            balance = balance + transaction.get__transaction_amount
        return balance

    def save_account(self, user_account: Account):
        self.__account_repository.save_account_to_repository(user_account)
