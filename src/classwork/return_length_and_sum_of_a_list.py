def get_mean(number_list):
    index: int = 0
    total: int = 0
    for number in enumerate(number_list):
        index += 1
        total += number[1]
    return index, total


if __name__ == "__main__":
    list_of_numbers: list = [1, 4, 5, 6, 7, 8, 8]
    (length_of_list, sum_of_numbers) = get_mean(list_of_numbers)
    print("{} is: {:.6f}".format("The mean of numbers in the list", sum_of_numbers / length_of_list))
