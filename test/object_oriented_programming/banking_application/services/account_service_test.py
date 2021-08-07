import unittest
from decimal import Decimal

from object_oriented_programming_in_python.banking_application.models.account import Account
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

    # def test_can_withdraw_from_account(self):
    #     user_service = UserService()
    #     new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
    #     deposit(new_user.get__accounts[0], 5000)
    #     withdraw(new_user.get__accounts[0], 2000)
    #     self.assertEqual(3000, new_user.get__accounts[0].get_transactions_on_this)

    # def test_raise_invalid_deposit_amount_exception(self):
    #     user_service = UserService()
    #     new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
    #     with self.assertRaises(InvalidDepositAmountException):
    #         deposit(new_user.get__accounts[0], -5000)

    # def test_raise_invalid_withdrawal_amount_exception(self):
    #     user_service = UserService()
    #     new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
    #     deposit(new_user.get__accounts[0], 5000)
    #     with self.assertRaises(InvalidWithdrawalAmountException):
    #         withdraw(new_user.get__accounts[0], -6000)
    #     with self.assertRaises(InvalidWithdrawalAmountException):
    #         withdraw(new_user.get__accounts[0], 6000)
    #
    # def test_customer_can_select_account_to_transfer_from(self):
    #     user_service = UserService()
    #     new_user = user_service.register("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
    #     user_service.create_new_account_for_existing_user("edemaehiz@gmail.com")
    #

if __name__ == '__main__':
    unittest.main()
