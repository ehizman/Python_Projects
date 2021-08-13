
class SavingsAccount:
    __annualInterestRate = 0.04

    def __init__(self, amount: float):
        self.__savingsBalance = amount

    @property
    def get__savingsBalance(self) -> float:
        return self.__savingsBalance

    def calculateMonthlyInterest(self) -> float:
        return round(((self.__savingsBalance * self.__annualInterestRate) / 12), 3)

    @classmethod
    def modifyInterestRate(cls, interest_rate: float) -> None:
        cls.__annualInterestRate = interest_rate

    @classmethod
    def get__annualInterestRate(cls):
        return cls.__annualInterestRate

    def updateSavingsBalance(self, interest) -> None:
        self.__savingsBalance += interest


