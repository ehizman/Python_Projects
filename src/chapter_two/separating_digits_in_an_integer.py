try:
    five_digit_integer: int = int(input("Enter a five digit integer: "))
    if five_digit_integer < 0 and (five_digit_integer < -99999 or five_digit_integer > -10000):
        raise ValueError("Invalid input! Number should be a 5 digit integer")
    if five_digit_integer > 0 and (five_digit_integer < 10000 or five_digit_integer > 99999):
        raise ValueError("Invalid input! Number should be a 5 digit integer")
except ValueError as error:
    print(error)
else:
    five_digit_integer = abs(five_digit_integer)
    list_of_digits = str(five_digit_integer)
    for i in range(len(list_of_digits)):
        print(list_of_digits[i], end="   ")
