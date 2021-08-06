from object_oriented_programming_in_python.banking_application.models.user import User
from object_oriented_programming_in_python.banking_application.services.bankservice import BankService


class UserService:
    def __init__(self):
        self.__bank_service = BankService()

    def register(self, first_name, last_name, email):
        new_user = User(first_name, last_name, email)
        user_account = self.__bank_service.create_account_for_new_user()
        self.__bank_service.add_new_user(new_user)
        new_user.update_list_of_customer_accounts(user_account)
        return new_user

    def create_new_account_for_existing_user(self, email):
        user = self.__bank_service.find_user_by_email(email)
        if user is not None:
            new_account = self.__bank_service.create_account_for_existing_user()
            user.update_list_of_customer_accounts(new_account)




