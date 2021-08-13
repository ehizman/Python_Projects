from typing import Optional

from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.invalid_user_details_exception import \
    InvalidUserException
from object_oriented_programming_in_python.banking_application.models.user import User


class UserRepository:
    __set_of_users = set()
    __f = open("users.txt", mode='a+', encoding='utf-8')

    def __init__(self):
        pass

    def add_new_user(self, user: User) -> None:
        if user is not None:
            self.__set_of_users.add(user)
            self.__f.write(f'{user.get_email}\n')
        else:
            raise InvalidUserException("Invalid user details")

    @property
    def get_set_of_users(self) -> set:
        self.__f.seek(0)
        print(self.__f.readline())
        return self.__set_of_users

    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.__set_of_users:
            if user.get_email == email:
                return user
        return None

