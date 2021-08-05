def merge_the_tools(stringShadow, k):
    number_of_sub_strings = len(stringShadow)//k
    start = 0
    listOfSubStrings = list()
    for i in range(number_of_sub_strings):
        subString = stringShadow[start: start + k]
        listOfSubStrings.append(subString)
        start += k

    for subString in listOfSubStrings:
        string_without_duplicates = list()
        for character in subString:
            if string_without_duplicates.count(character) == 0:
                string_without_duplicates.append(character)

        print(''.join(string_without_duplicates))


if __name__ == '__main__':
    merge_the_tools('AABCAs', 3)