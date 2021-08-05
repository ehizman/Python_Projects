def minion_game(string):
    kevin = 0
    stuart = 0
    for index,element in enumerate(string):
        if element in 'AEIOU':
            kevin += len(string) - index
        else:
            stuart += len(string) - index
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game("BANANAS")