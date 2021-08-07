import unittest
from object_oriented_programming_in_python.banking_application.services.bankservice import BankService
from object_oriented_programming_in_python.banking_application.services.user_service import UserService

bank_service = BankService()
user_service = UserService()


class MyTestCase(unittest.TestCase):

    def tearDown(self) -> None:
        bank_service.view_all_accounts().clear()

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_bank_has_list_of_account(self):
        user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        print(bank_service.view_all_accounts())
        self.assertEqual(1, len(bank_service.view_all_accounts()))

    def test_that_can_find_customer_by_account_number(self):
        ehis = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        eseosa = user_service.register("Eseosa", "Edemakhiota", "eseosaedemakhiota@gmail.com")
        print(bank_service.view_all_accounts())
        self.assertEqual(2, len(bank_service.view_all_accounts()))

        account_number = ehis.get__accounts[0]
        user_to_find = bank_service.find_user_by_account_number(account_number)
        self.assertTrue(id(ehis) == id(user_to_find))
        account_number = eseosa.get__accounts[0]
        user_to_find = bank_service.find_user_by_account_number(account_number)
        self.assertTrue(id(eseosa) == id(user_to_find))


if __name__ == '__main__':
    unittest.main()
