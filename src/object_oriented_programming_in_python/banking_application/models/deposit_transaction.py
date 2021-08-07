from object_oriented_programming_in_python.banking_application.models.transaction import Transaction


class DepositTransaction(Transaction):
    def __init__(self, account_id, amount, purpose):
        super(DepositTransaction, self).__init__(account_id, amount, purpose)

