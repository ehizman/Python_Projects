def factorial(number):
    while number > 0:
        return number * factorial(number - 1)


def main():
    number: int = int(input("Enter a non-negative integer -> "))
    if number < 0:
        raise ValueError
    else:
        print(factorial(number))


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Invalid parameter")
