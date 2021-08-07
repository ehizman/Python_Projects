from unittest import TestCase

from object_oriented_programming_in_python.banking_application.repositories.user_repository import UserRepository
from object_oriented_programming_in_python.banking_application.services.userservice import UserService


class TestUserRepository(TestCase):
    def __init__(self):
        super().__init__()
        self.__userService = UserService()
        self.__userRepository = UserRepository()


    def test_user_repo(self):
        self.__userService.register("Ehis", "Edemakhiota", "1234")

