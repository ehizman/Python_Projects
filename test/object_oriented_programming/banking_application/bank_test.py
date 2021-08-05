import unittest
from object_oriented_programming_in_python.banking_application.person import Person
from object_oriented_programming_in_python.banking_application.services.bankservice import BankService


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_bank_has_list_of_account(self):
        ehis = Person("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        self.assertEqual(1, len(BankService.view_all_accounts()))

    def test_that_two_customers_do_not_have_the_same_account(self):
        ehis = Person("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        eseosa = Person("Eseosa", "Edemakhiota", "edemaeseosa@gmail.com")
        self.assertNotEqual(ehis.get__accounts[0], eseosa.get__accounts[0])

    def test_that_can_find_customer_by_account_number(self):
        ehis = Person("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        account_number = ehis.get__accounts[0]
        BankService.find_user_by_account_number(account_number)
        self.assertEquals(f"""First Name -> Ehis
Last Name -> Edemakhiota
Email -> edemaehiz@gmail.com
Account Number -> {account_number}""", ehis.__str__())


if __name__ == '__main__':
    unittest.main()
