class Invalid_Login_Exception(Exception):
    def __init__(self, message):
        super(Invalid_Login_Exception, self).__init__(message)
