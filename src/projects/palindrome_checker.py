string = input("Enter a string to check if it is a palindrome: ")

if string[0] != string[-1]:
    print(string, "is not a palindrome")
else:
    print(string, "is a palindrome")
