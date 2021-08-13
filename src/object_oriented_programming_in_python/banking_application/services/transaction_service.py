from decimal import Decimal

from object_oriented_programming_in_python.banking_application.models.deposit_transaction import DepositTransaction
from object_oriented_programming_in_python.banking_application.models.transfer_transaction import TransferTransaction
from object_oriented_programming_in_python.banking_application.models.withdraw_transaction import WithdrawalTransaction
from object_oriented_programming_in_python.banking_application.repositories.transaction_repository import \
    TransactionRepository


class TransactionService:
    __transaction_repository = TransactionRepository()

    def __init__(self):
        pass

    def create_new_deposit_transaction(self, account_number: str, amount_to_deposit: Decimal, message: str) -> str:
        amount_to_deposit: Decimal = Decimal(amount_to_deposit)
        new_transaction: DepositTransaction = DepositTransaction(account_number, amount_to_deposit, message)
        self.__transaction_repository.save_transaction(new_transaction)
        return new_transaction.get__transaction_id

    def get_transactions_on_this(self, account_number: str) -> list:
        return self.__transaction_repository.find_transactions_on_this_(account_number)

    def create_new_withdraw_transaction(self, account_number: str, amount_to_withdraw: Decimal, message: str):
        amount_to_withdraw: Decimal = Decimal(amount_to_withdraw)
        new_transaction: WithdrawalTransaction = WithdrawalTransaction(account_number, amount_to_withdraw, message)
        self.__transaction_repository.save_transaction(new_transaction)
        return new_transaction.get__transaction_id

    def create_new_transfer_transaction(self, src_account_number: str, amount: Decimal, beneficiary_account_number: str,
                                        message: str):
        amount: Decimal = Decimal(amount)
        new_transaction: TransferTransaction = TransferTransaction(src_account_number, amount,
                                                                   message,
                                                                   beneficiary_account_number)
        self.__transaction_repository.save_transaction(new_transaction)
        return new_transaction.get__transaction_id
