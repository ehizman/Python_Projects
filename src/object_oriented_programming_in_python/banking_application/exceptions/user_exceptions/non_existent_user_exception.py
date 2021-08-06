class Non_Existent_User_Exception(Exception):
    def __init__(self, message):
        super(Non_Existent_User_Exception, self).__init__(message)
