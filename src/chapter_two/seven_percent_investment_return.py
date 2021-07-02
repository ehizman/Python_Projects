import math

amount_invested: int = 1000
annual_rate_of_return: float = (7 / 100)
list_number_of_years = [10, 20, 30]

for i in list_number_of_years:
    amount_on_deposit_at_the_end_of_nth_year = amount_invested * math.pow(1 + annual_rate_of_return, i)
    print(f"The amount on deposit expected at the and of {i} years is {amount_on_deposit_at_the_end_of_nth_year}")
