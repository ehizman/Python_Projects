import datetime
from decimal import Decimal

from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_deposit_amount_exception import \
    InvalidDepositAmountException
from object_oriented_programming_in_python.banking_application.exceptions.account_exceptions.invalid_withdrawal_amount_exception import \
    InvalidWithdrawalAmountException


def deposit(account, amount_to_deposit):
    if amount_to_deposit < 0.0:
        raise InvalidDepositAmountException("Invalid deposit amount")
    else:
        transaction = ("DEPOSIT", Decimal(amount_to_deposit), datetime.datetime.now().__str__())
        account.add_new_transaction(transaction)


def withdraw(account, amount_to_withdraw):
    if amount_to_withdraw < 0.0 or amount_to_withdraw > account.get_account_balance:
        raise InvalidWithdrawalAmountException("Invalid withdrawal amount")
    else:
        transaction = ("WITHDRAWAL", Decimal(-amount_to_withdraw), datetime.datetime.now())
        account.add_new_transaction(transaction)


class AccountService:
    pass
