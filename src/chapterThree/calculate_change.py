purchase_price_of_item: int = int(input("Enter the item purchase price: "))

change: int = 100 - (purchase_price_of_item % 100)

value_of_a_quarter: int = 25
number_of_quarters: int = change//value_of_a_quarter
change %= value_of_a_quarter

value_of_a_dime: int = 10
number_of_dimes: int = change//value_of_a_dime
change %= value_of_a_dime

number_of_pennies: int = change

print("""
Your change is:
{} quarters
{} dimes
{} pennies""".format(number_of_quarters, number_of_dimes, number_of_pennies))
