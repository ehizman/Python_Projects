class InvalidWithdrawalAmountException(Exception):
    def __init__(self, message):
        super(InvalidWithdrawalAmountException, self).__init__(message)
