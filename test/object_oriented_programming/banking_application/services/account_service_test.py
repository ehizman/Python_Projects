import unittest
from decimal import Decimal

from object_oriented_programming_in_python.banking_application.exceptions.transaction_exceptions.invalid_deposit_amount_exception import \
    InvalidDepositAmountException
from object_oriented_programming_in_python.banking_application.exceptions.transaction_exceptions.invalid_withdrawal_amount_exception import \
    InvalidWithdrawalAmountException
from object_oriented_programming_in_python.banking_application.models.user import User
from object_oriented_programming_in_python.banking_application.services.account_service import AccountService
from object_oriented_programming_in_python.banking_application.services.user_service import UserService


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_can_deposit_into_account(self):
        user_service = UserService()
        account_service = AccountService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        account_number_to_deposit: str = new_user.get__accounts[0].get_account_number
        account_service.deposit(account_number_to_deposit, Decimal(5000), "small thing for the weekend")
        self.assertEqual(5000, account_service.find_balance_on(account_number_to_deposit))

    def test_can_withdraw_from_account(self):
        user_service = UserService()
        account_service = AccountService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        account_number: str = new_user.get__accounts[0].get_account_number
        account_service.deposit(account_number, Decimal(5000), "small thing for the weekend")
        account_service.withdraw(account_number, Decimal(3000), "for food")
        self.assertEqual(2000, account_service.find_balance_on(account_number))

    def test_raise_invalid_deposit_amount_exception(self):
        user_service = UserService()
        account_service = AccountService()
        new_user: User = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        account_number: str = new_user.get__accounts[0].get_account_number
        with self.assertRaises(InvalidDepositAmountException):
            account_service.deposit(account_number, Decimal(-5000), "small thing for the weekend")

    def test_raise_invalid_withdrawal_amount_exception(self):
        user_service = UserService()
        account_service = AccountService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        account_number: str = new_user.get__accounts[0].get_account_number
        account_service.deposit(account_number, Decimal(5000), "small thing for the weekend")
        with self.assertRaises(InvalidWithdrawalAmountException):
            account_service.withdraw(account_number, Decimal(6000), "for food")
        with self.assertRaises(InvalidWithdrawalAmountException):
            account_service.withdraw(account_number, Decimal(-3000), "for food")

    def test_user_can_transfer(self):
        user_service = UserService()
        account_service = AccountService()
        first_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        second_user = user_service.register("Eseosa", "Edemakhiota", "eseosaedemakhiota@gmail.com")
        first_user_account_number = first_user.get__accounts[0].get_account_number
        second_user_account_number = second_user.get__accounts[0].get_account_number
        account_service.deposit(first_user_account_number, Decimal("50000"), "for lavish style")
        account_service.transfer(first_user_account_number, second_user_account_number, 5000, "for lavish style")
        self.assertEqual(account_service.find_balance_on(first_user_account_number), 45000)
        self.assertEqual(account_service.find_balance_on(second_user_account_number), 5000)


if __name__ == '__main__':
    unittest.main()
