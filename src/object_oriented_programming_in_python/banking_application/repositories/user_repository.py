from typing import Optional

from object_oriented_programming_in_python.banking_application.models.user import User


class UserRepository:
    def __init__(self):
        self.__set_of_users = set()

    @property
    def get_set_of_users(self) -> set:
        return self.__set_of_users

    def add_new_user(self, user: User) -> None:
        if user is not None:
            self.__set_of_users.add(user)
        else:
            raise InvalidUserException("Invalid user details")

    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.__set_of_users:
            if user.get_email == email:
                return user
        return None

