from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.invalid_user_details_exception import \
    InvalidUserException
from object_oriented_programming_in_python.banking_application.models.account import Account
from object_oriented_programming_in_python.banking_application.models.user import User
from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.nonexistentuserexception import \
    NonExistentUserException
from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.invalidloginexception import \
    InvalidLoginException
from object_oriented_programming_in_python.banking_application.repositories.user_repository import UserRepository
from object_oriented_programming_in_python.banking_application.services.account_service import AccountService


def validation(email, first_name, last_name):
    if str.isspace(first_name) or str.isspace(last_name) or str.isspace(email):
        raise InvalidUserException("Invalid user details")
    if first_name == "" or last_name == "" or email == "":
        raise InvalidUserException("Invalid user details")
    if str.isdigit(first_name) or str.isdigit(last_name) or str.isdigit(email):
        raise InvalidUserException("Invalid user details")


class UserService:
    def __init__(self):
        self.__account_service = AccountService()
        self.__user_repository = UserRepository()

    def register(self, first_name: str, last_name: str, email: str) -> User:
        validation(email, first_name, last_name)
        new_user: User = User(first_name, last_name, email)
        user_account: Account = self.__account_service.create_account()
        new_user.update_user_accounts(user_account)
        self.__user_repository.add_new_user(new_user)
        return new_user

    def create_new_account_for_existing_user(self, email: str) -> None:
        user = self.__user_repository.find_user_by_email(email)
        if user is not None:
            new_account = self.__account_service.create_account()
            user.update_user_accounts(new_account)

    def validate_login(self, email: str, account_pin: str) -> bool:
        user = self.__user_repository.find_user_by_email(email)
        if user is not None:
            for account in user.get__accounts:
                if account.get_account_pin == account_pin:
                    return True
            raise InvalidLoginException("Invalid login details")
        raise NonExistentUserException("User details does not exist")
