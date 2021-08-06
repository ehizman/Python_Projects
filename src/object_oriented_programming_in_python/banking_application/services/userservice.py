from object_oriented_programming_in_python.banking_application.models.user import User
from object_oriented_programming_in_python.banking_application.services.bankservice import BankService


class UserService:
    def __init__(self):
        self.__bank_service = BankService()

    def register(self, first_name, last_name, email):
        new_user = User(first_name, last_name, email)
        account_number = self.__bank_service.create_account()
        self.__bank_service.add_new_user(new_user)
        new_user.update_list_of_customer_accounts(account_number)
        return new_user


