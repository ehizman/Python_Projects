def factorial(number) -> int:
    if number < 0:
        raise ValueError("Invalid parameter")
    else:
        factorial_of_number: int = 1
        while number > 0:
            factorial_of_number *= number
            number -= 1
        return factorial_of_number
