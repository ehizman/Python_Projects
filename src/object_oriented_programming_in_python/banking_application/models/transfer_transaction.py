from object_oriented_programming_in_python.banking_application.models.transaction import Transaction


class TransferTransaction(Transaction):
    def __init__(self, src_account_id, amount, message, beneficiary_account):
        super(TransferTransaction, self).__init__(src_account_id, amount, message)
        self.__beneficiary_account = beneficiary_account

    @property
    def get__beneficiary_account(self):
        return self.__beneficiary_account

    def __str__(self):
        return f"""Beneficiary account number : {self.get__beneficiary_account}
Source account number : {self.get__account_number_initiated_from}
Amount = {self.get__transaction_amount}"""

