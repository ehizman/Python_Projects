class InvalidLoginException(Exception):
    def __init__(self, message):
        super(InvalidLoginException, self).__init__(message)
