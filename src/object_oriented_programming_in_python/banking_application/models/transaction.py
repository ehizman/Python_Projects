import abc
import datetime
import uuid
from decimal import Decimal


class Transaction(abc.ABC):
    def __init__(self, account_id, amount, purpose=""):
        self.__initiated_from = account_id
        self.__transaction_id = str(uuid.uuid4())
        self.__date_time: str = str(datetime.datetime.now())
        self.__amount: Decimal = amount
        self.__withdrawal_purpose = purpose

    @property
    def get__transaction_id(self):
        return self.__transaction_id
