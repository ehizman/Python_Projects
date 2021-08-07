from decimal import Decimal

from object_oriented_programming_in_python.banking_application.models.deposit_transaction import DepositTransaction
from object_oriented_programming_in_python.banking_application.repositories.transaction_repository import \
    TransactionRepository


class TransactionService:
    def __init__(self):
        self.amount_to_deposit: Decimal = Decimal(0)
        self.__transaction_repository = TransactionRepository()

    def create_new_deposit_transaction(self, account_number: str, amount_to_deposit: Decimal, message: str) -> str:
        self.amount_to_deposit: Decimal = Decimal(amount_to_deposit)
        new_transaction: DepositTransaction = DepositTransaction(account_number, self.amount_to_deposit, message)
        self.__transaction_repository.save_transaction(new_transaction)
        return new_transaction.get__transaction_id

    def get_transactions_on_this(self, account_number: str) -> list:
        transaction_list: list = self.__transaction_repository.find_transactions_on_this_(account_number)
        return transaction_list
