import unittest

from object_oriented_programming_in_python.banking_application.models.user import User
from object_oriented_programming_in_python.banking_application.services.userservice import UserService


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_constructor(self):
        user_service = UserService()
        ehis = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        self.assertEqual("Ehis", ehis.get_first_name)
        self.assertEqual("Edemakhiota", ehis.get_last_name)
        self.assertEqual("edemaehiz@gmail.com", ehis.get_email)

    def test_person_has_account_upon_creation(self):
        user_service = UserService()
        ehis = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        self.assertEqual(1, len(ehis.get__accounts))

    def test_that_two_customers_do_not_have_the_same_account(self):
        user_service = UserService()
        ehis = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        eseosa = user_service.register("Eseosa", "Edemakhiota", "edemaeseosa@gmail.com")
        self.assertNotEqual(ehis.get__accounts[0], eseosa.get__accounts[0])

    def test_that_a_customer_can_have_two_accounts(self):
        user_service = UserService()
        ehis = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        user_service.create_new_account_for_existing_user(ehis.get_email)
        print(ehis.get__accounts)
        self.assertEqual(2, len(ehis.get__accounts))
    # def test_that_can_validate_user_login(self):
    #     user_service = UserService()
    #     user_service.validateLogin("edemaehiz@gmail.com")


if __name__ == '__main__':
    unittest.main()
