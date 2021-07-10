import sys
from random import random


def find_two_largest_numbers_in(a_list):
    largest_number = -sys.maxsize
    second_largest_number = -sys.maxsize

    for number in a_list:
        if number > largest_number:
            second_largest_number = largest_number
            largest_number = number
        if second_largest_number < number < largest_number:
            second_largest_number = number
        print(largest_number, second_largest_number)
    return largest_number, second_largest_number


if __name__ == "__main__":
    input_list = [int((random() + 1) * x) for x in range(10)]
    max_number, second_max_num = find_two_largest_numbers_in(input_list)
    print("Largest number: {} \nSecond largest number: {}".format(max_number, second_max_num))
