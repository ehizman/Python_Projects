import uuid
from decimal import Decimal

from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_account_exception import \
    InvalidAccountException
from object_oriented_programming_in_python.banking_application.exceptions.transaction_exceptions.invalid_deposit_amount_exception import \
    InvalidDepositAmountException
from object_oriented_programming_in_python.banking_application.exceptions.transaction_exceptions.invalid_withdrawal_amount_exception import \
    InvalidWithdrawalAmountException
from object_oriented_programming_in_python.banking_application.models.account import Account
from object_oriented_programming_in_python.banking_application.models.deposit_transaction import DepositTransaction
from object_oriented_programming_in_python.banking_application.models.transfer_transaction import TransferTransaction
from object_oriented_programming_in_python.banking_application.models.withdraw_transaction import WithdrawalTransaction
from object_oriented_programming_in_python.banking_application.repositories.account_repository import AccountRepository
from object_oriented_programming_in_python.banking_application.services.transaction_service import TransactionService


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

    def withdraw(self, account_number: str, amount_to_withdraw: Decimal, message: str) -> None:
        if amount_to_withdraw < 0.0:
            raise InvalidWithdrawalAmountException("Invalid deposit amount")
        balance: Decimal = self.find_balance_on(account_number)
        if amount_to_withdraw > balance:
            raise InvalidWithdrawalAmountException("Invalid deposit amount")
        else:
            account: Account = self.__account_repository.find_account_with_number(account_number)
            if account is not None:
                transaction_id: str = self.__transaction_service.create_new_withdraw_transaction(account_number,
                                                                                                 amount_to_withdraw,
                                                                                                 message)
                account.add_new_transaction_to_account(transaction_id)
            else:
                raise InvalidAccountException("Account does not exist")

    def update_list_of_customer_accounts(self, account_number):
        self.__account_repository.get__list_of_accounts.append(account_number)

    def find_balance_on(self, account_number: str) -> Decimal:
        list_of_transactions_on_account_number: list = self.__transaction_service.get_transactions_on_this \
            (account_number)
        balance = Decimal("0")
        for transaction in list_of_transactions_on_account_number:
            if isinstance(transaction, TransferTransaction) and transaction.get__account_number_initiated_from == \
                    account_number:
                balance = balance - transaction.get__transaction_amount
            elif isinstance(transaction, TransferTransaction) and transaction.get__beneficiary_account == account_number:
                balance = balance + transaction.get__transaction_amount
            elif isinstance(transaction, WithdrawalTransaction):
                balance = balance - transaction.get__transaction_amount
            elif isinstance(transaction, DepositTransaction):
                balance = balance + transaction.get__transaction_amount
        return balance

    def save_account(self, user_account: Account):
        self.__account_repository.save_account_to_repository(user_account)

    def find_account(self,account_number: str) -> Account:
        return self.__account_repository.find_account_with_number(account_number)

    def transfer(self, source_account_number: str, beneficiary_account_number: str, amount_to_transfer: float, message: str):
        if amount_to_transfer < 0.0:
            raise InvalidWithdrawalAmountException("Invalid withdrawal amount")
        balance: Decimal = self.find_balance_on(source_account_number)
        if amount_to_transfer > balance:
            raise InvalidWithdrawalAmountException("Invalid withdrawal amount")
        else:
            source_account: Account = self.__account_repository.find_account_with_number(source_account_number)
            beneficiary_account: Account = self.__account_repository.find_account_with_number(
                beneficiary_account_number)
            if beneficiary_account is not None:
                transaction_id: str = self.__transaction_service.create_new_transfer_transaction(source_account_number,
                                                                                                 amount_to_transfer,
                                                                                                 beneficiary_account_number,
                                                                                                 message)
                source_account.add_new_transaction_to_account(transaction_id)
                beneficiary_account.add_new_transaction_to_account(transaction_id)
            else:
                raise InvalidAccountException("Account does not exist")
