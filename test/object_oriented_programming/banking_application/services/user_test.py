import unittest

from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.invalid_login_exception import \
    Invalid_Login_Exception
from object_oriented_programming_in_python.banking_application.exceptions.user_exceptions.non_existent_user_exception import \
    Non_Existent_User_Exception
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
        user_service.create_new_account_for_existing_user("edemaehiz@gmail.com")
        self.assertEqual(2, len(ehis.get__accounts))

    def test_that_can_validate_user_login(self):
        user_service = UserService()
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        bool_ = user_service.validate_login("edemaehiz@gmail.com", "1234")
        self.assertTrue(bool_)

    def test_raises_invalid_login_exception(self):
        user_service = UserService()
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        with self.assertRaises(Invalid_Login_Exception):
            user_service.validate_login("edemaehiz@gmail.com", "5678")

    def test_raises_non_existent_user_exception(self):
        user_service = UserService()
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        with self.assertRaises(Non_Existent_User_Exception):
            user_service.validate_login("edemaehi@gmail.com", "5678")


if __name__ == '__main__':
    unittest.main()
