import unittest

from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_deposit_amount_exception import \
    InvalidDepositAmountException
from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_withdrawal_amount_exception import \
    InvalidWithdrawalAmountException
from object_oriented_programming_in_python.banking_application.services.account_service import AccountService, deposit, \
    withdraw
from object_oriented_programming_in_python.banking_application.services.userservice import UserService


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_can_deposit_into_account(self):
        user_service = UserService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        deposit(new_user.get__accounts[0], 5000, "small thing for the weekend")
        self.assertEqual(5000, get)

    def test_can_withdraw_from_account(self):
        user_service = UserService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        deposit(new_user.get__accounts[0], 5000)
        withdraw(new_user.get__accounts[0], 2000)
        self.assertEqual(3000, new_user.get__accounts[0].get_account_balance)

    def test_raise_invalid_deposit_amount_exception(self):
        user_service = UserService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        with self.assertRaises(InvalidDepositAmountException):
            deposit(new_user.get__accounts[0], -5000)

    def test_raise_invalid_withdrawal_amount_exception(self):
        user_service = UserService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        deposit(new_user.get__accounts[0], 5000)
        with self.assertRaises(InvalidWithdrawalAmountException):
            withdraw(new_user.get__accounts[0], -6000)
        with self.assertRaises(InvalidWithdrawalAmountException):
            withdraw(new_user.get__accounts[0], 6000)

    def test_customer_can_select_account_to_transfer_from(self):
        user_service = UserService()
        new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        user_service.create_new_account_for_existing_user("edemaehiz@gmail.com")


if __name__ == '__main__':
    unittest.main()
