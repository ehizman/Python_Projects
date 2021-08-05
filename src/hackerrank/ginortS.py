string = 'Sorting154234'

list_of_odd_numbers = [x for x in string if x.isdigit() and int(x) % 2 == 1]
list_of_even_numbers = [x for x in string if x.isdigit() and int(x) % 2 == 0]
list_of_odd_numbers.sort()
list_of_even_numbers.sort()

list_of_lowercase_letters = [x for x in string if x.islower()]
list_of_lowercase_letters.sort()

list_of_uppercase_letters = [x for x in string if x.isupper()]
list_of_uppercase_letters.sort()

str_of_lowercase_letters = "".join(list_of_lowercase_letters)
str_of_uppercase_letters = "".join(list_of_uppercase_letters)
str_of_odd_digits = "".join(list_of_odd_numbers)
str_of_even_digits = "".join(list_of_even_numbers)
print(str_of_lowercase_letters + str_of_uppercase_letters + str_of_odd_digits + str_of_even_digits)