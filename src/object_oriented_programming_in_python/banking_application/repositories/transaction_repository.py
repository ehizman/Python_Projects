from object_oriented_programming_in_python.banking_application.models.transfer_transaction import TransferTransaction
from object_oriented_programming_in_python.banking_application.models.withdraw_transaction import WithdrawalTransaction


class TransactionRepository:
    __list_of_transactions = list()

    def __init__(self):
        pass

    def save_transaction(self, transaction):
        self.__list_of_transactions.append(transaction)

    def find_transactions_on_this_(self, account_number: str) -> list:
        list_of_transactions_on_account_number: list = list()
        for transaction in self.__list_of_transactions:
            print(transaction.__str__())
            if isinstance(transaction, TransferTransaction):
                if transaction.get__beneficiary_account == account_number:
                    list_of_transactions_on_account_number.append(transaction)
                elif transaction.get__account_number_initiated_from == account_number:
                    list_of_transactions_on_account_number.append(transaction)
                else:
                    pass
            elif isinstance(transaction, WithdrawalTransaction):
                if transaction.get__account_number_initiated_from == account_number:
                    list_of_transactions_on_account_number.append(transaction)
            else:
                if transaction.get__account_number_initiated_from == account_number:
                    list_of_transactions_on_account_number.append(transaction)

        return list_of_transactions_on_account_number
