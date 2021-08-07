class InvalidAccountException(Exception):
    def __init__(self, message):
        super(InvalidAccountException, self).__init__(message)