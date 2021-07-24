import string


def string_rangoli(size):
    global new_string
    alphabet_string: str = string.ascii_lowercase
    range_of_alphabets = [alphabet_string[a] for a in range(size)]
    range_of_alphabets = range_of_alphabets[::-1]

    for i in range(size):
        new_list = [range_of_alphabets[a] for a in range(i+1)]
        new_string = "-" * (((size - i) * 2) - 2) + '-'.join(map(str, new_list))
        print(new_string + new_string[-2::-1])
    size -= 1

    for i in range(size):
        new_list = [range_of_alphabets[a] for a in range(size-i)]
        new_string = "-" * ((i * 2) + 2) + '-'.join(map(str, new_list))
        print(new_string + new_string[-2::-1])


if __name__ == "__main__":
    number_of_rows: int = int(input("Enter the number of rows you want in the string rangoli"))
    string_rangoli(number_of_rows)
