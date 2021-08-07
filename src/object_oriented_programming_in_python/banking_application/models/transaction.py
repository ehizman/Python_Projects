import abc
import datetime
import uuid
from decimal import Decimal


class Transaction(abc.ABC):
    def __init__(self, account_number: str, amount: Decimal, purpose: str=""):
        self.__transaction_id: str = str(uuid.uuid4())
        self.__account_number_initiated_from: str = account_number
        self.__date_time: str = str(datetime.datetime.now())
        self.__amount: Decimal = amount
        self.__withdrawal_purpose: str= purpose

    @property
    def get__transaction_id(self):
        return self.__transaction_id

    @property
    def get_account_number_initiated_from(self) -> str:
        return self.__account_number_initiated_from

    @property
    def get__transaction_amount(self) -> Decimal:
        return self.__amount
