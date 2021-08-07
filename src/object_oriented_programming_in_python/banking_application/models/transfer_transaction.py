from object_oriented_programming_in_python.banking_application.models.transaction import Transaction


class TransferTransaction(Transaction):
    def __init__(self, src_account_id, amount, message, beneficiary_account):
        super(TransferTransaction, self).__init__(src_account_id, amount, message)
        self.__beneficiary_account = beneficiary_account
