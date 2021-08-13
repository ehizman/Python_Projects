import abc
import datetime
import uuid
from decimal import Decimal


class Transaction(abc.ABC):
    def __init__(self, account_number: str, amount: Decimal, purpose: str = ""):
        self.__transaction_id: str = str(uuid.uuid4())
        self.__account_number_initiated_from: str = account_number
        self.__date_time: str = str(datetime.datetime.now())
        self.__amount: Decimal = amount
        self.__purpose: str = purpose

    @property
    def get__transaction_id(self):
        return self.__transaction_id

    @property
    def get__account_number_initiated_from(self) -> str:
        return self.__account_number_initiated_from

    @property
    def get__transaction_amount(self) -> Decimal:
        return self.__amount

    @property
    def get__purpose(self):
        return self.__purpose

    @property
    def get__date_time(self):
        return self.__date_time

    def __str__(self):
        return f"""Source account number : {self.get__account_number_initiated_from}
Amount = {self.get__transaction_amount}
Message = {self.get__purpose}
Date/Time = {self.get__date_time}

"""
