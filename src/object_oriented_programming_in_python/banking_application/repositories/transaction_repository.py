
class TransactionRepository:
    def __init__(self):
        self.__list_of_transactions = list()

    def save_transaction(self, transaction):
        self.__list_of_transactions.append(transaction)

    def find_transactions_on_this_(self, account_number: str) -> list:
        list_of_transactions_on_account_number: list = list()
        for transaction in self.__list_of_transactions:
            if transaction.get_account_number_initiated_from == account_number:
                print(type(transaction.get_account_number_initiated_from))
                print(type(account_number))
                list_of_transactions_on_account_number.append(transaction)
        return list_of_transactions_on_account_number





