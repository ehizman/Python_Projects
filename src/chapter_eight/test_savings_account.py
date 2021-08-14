from unittest import TestCase

from chapter_eight.savings_account import SavingsAccount


class savings_account_test(TestCase):
    def test_constructor(self):
        saver1: SavingsAccount = SavingsAccount(2000.0)
        saver2: SavingsAccount = SavingsAccount(3000.0)
        self.assertEqual(2000, saver1.get__savingsBalance)
        self.assertEqual(3000, saver2.get__savingsBalance)

    def test_can_calculate_monthly_interest_rate(self):
        saver1: SavingsAccount = SavingsAccount(2000.0)
        self.assertEqual(6.667, saver1.calculateMonthlyInterest())

    def test_modifyInterestRate(self):
        SavingsAccount.modifyInterestRate(0.05)
        self.assertEqual(0.05, SavingsAccount.get__annualInterestRate())

    def test_can_print_next_months_interest_rate(self):
        saver1: SavingsAccount = SavingsAccount(2000.0)
        SavingsAccount.modifyInterestRate(0.05)
        interest_for_current_month: float = saver1.calculateMonthlyInterest()
        saver1.updateSavingsBalance(interest_for_current_month)
        self.assertEqual(8.368, saver1.calculateMonthlyInterest())

    # def test_can_calculate_compound_interest(self):
    #     saver1: SavingsAccount = SavingsAccount(2000.0)
    #     SavingsAccount.modifyInterestRate(0.05)
    #     self.assertEqual(8.368, saver1.calculate_compound_interest(1)




