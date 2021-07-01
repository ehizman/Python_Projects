countOfZeros = 0
countOfNegativeValues = 0
countOfPositiveValues = 0
for i in range(5):
    number = int(input("Enter number %s " % (i+1)))
    if number == 0:
        countOfZeros = countOfZeros + 1
    else:
        if number < 0:
            countOfNegativeValues = countOfNegativeValues + 1
        else:
            countOfPositiveValues = countOfPositiveValues + 1

print(f"The count of zero values is {countOfZeros}")
print(f"The count of negative values is {countOfNegativeValues}")
print(f"The count of positive values is {countOfPositiveValues}")
