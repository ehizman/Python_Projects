class InvalidUserException(Exception):
    def __init__(self, message):
        super(InvalidUserException, self).__init__(message)