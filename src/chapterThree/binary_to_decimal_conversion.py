binary_number: int = int(input("Enter a binary number: "))
decimal_equivalent: int = 0
count: int = 0
while binary_number != 0:
    remainder: int = binary_number % 10
    decimal_equivalent = decimal_equivalent + remainder * int(pow(2, count))
    binary_number = binary_number//10
    count += 1

print("The decimal equivalent of is {}".format(decimal_equivalent))