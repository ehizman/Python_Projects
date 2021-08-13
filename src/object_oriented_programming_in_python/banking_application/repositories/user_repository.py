from typing import Optional

from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.invalid_user_details_exception import \
    InvalidUserException
from object_oriented_programming_in_python.banking_application.models.user import User


class UserRepository:
    __set_of_users = set()

    def __init__(self):
        pass

    def add_new_user(self, user: User) -> None:
        if user is not None:
            self.__set_of_users.add(user)
        else:
            raise InvalidUserException("Invalid user details")

    @property
    def get_set_of_users(self) -> set:
        return self.__set_of_users

    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.__set_of_users:
            if user.get_email == email:
                return user
        return None

