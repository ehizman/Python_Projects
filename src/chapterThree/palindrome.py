def is_palindrome(number) -> bool:
    if len(str(number)) != 5:
        print("{} is not of length 5")
        return False
    else:
        reverse_number: int = 0
        remaining_number: int = number
        for _ in range(len(str(number))):
            remainder: int = remaining_number % 10
            reverse_number = (reverse_number * 10) + remainder
            remaining_number = remaining_number // 10
        return reverse_number == number
