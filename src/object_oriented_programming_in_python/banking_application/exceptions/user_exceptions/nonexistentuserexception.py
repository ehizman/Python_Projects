class NonExistentUserException(Exception):
    def __init__(self, message):
        super(NonExistentUserException, self).__init__(message)
