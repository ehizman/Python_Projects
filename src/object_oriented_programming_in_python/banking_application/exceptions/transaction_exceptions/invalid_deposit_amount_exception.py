class InvalidDepositAmountException(Exception):
    def __init__(self, message):
        super(InvalidDepositAmountException, self).__init__(message)