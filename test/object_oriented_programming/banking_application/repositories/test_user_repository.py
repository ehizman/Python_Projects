from unittest import TestCase

from object_oriented_programming_in_python.banking_application.repositories.user_repository import UserRepository
from object_oriented_programming_in_python.banking_application.services.user_service import UserService


class TestUserRepository(TestCase):

    def test_can_add_new_user(self):
        user_service = UserService()
        user_repository = UserRepository()
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        user_service.register("Eseosa", "Edemakhiota", "edemaehis@gmail.com")
        self.assertEqual(3, len(user_repository.get_set_of_users))
