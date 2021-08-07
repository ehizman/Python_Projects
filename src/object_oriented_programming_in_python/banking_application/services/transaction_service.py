from object_oriented_programming_in_python.banking_application.models.deposit_transaction import DepositTransaction
from object_oriented_programming_in_python.banking_application.repositories.transaction_repository import \
    TransactionRepository


class TransactionService:
    def __init__(self):
        self.__transaction_repository = TransactionRepository()

    def create_new_deposit_transaction(self, account_id, amount_to_deposit, message):
        new_transaction = DepositTransaction(account_id, amount_to_deposit, message)
        self.__transaction_repository.save_transaction(new_transaction)
        return new_transaction.get__transaction_id

    def get_account_balance(self, account):
        self.__transaction_repository.find_account(account)
