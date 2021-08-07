
class TransactionRepository:
    def __init__(self):
        self.__list_of_transactions = list()

    def save_transaction(self, transaction):
        self.__list_of_transactions.append(transaction)

    def find_account(self, account_id):
        for transaction in self.__list_of_transactions:
            if transaction.get__transaction_id == account_id:
                print(transaction.get__transaction_id)



