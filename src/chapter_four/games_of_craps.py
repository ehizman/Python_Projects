import random
import sys

point: int = 0
should_continue_game: bool = True
result_of_rolling_dice_one: int = 0
result_of_rolling_dice_two: int = 0
count: int = 0

while should_continue_game:
    result_of_rolling_dice_one = random.randrange(1, 7)
    result_of_rolling_dice_two = random.randrange(1, 7)
    count = count + 1

    sum_of_results: int = result_of_rolling_dice_one + result_of_rolling_dice_two
    print("""
Result of Dice 1: {}
Result of Dice 2: {}""".format(result_of_rolling_dice_one, result_of_rolling_dice_two))
    if count == 1:
        if sum_of_results == 7 or sum_of_results == 11:
            print("You win!")
            print("Exiting game!")
            sys.exit(0)
        elif sum_of_results == 2 or sum_of_results == 3 or sum_of_results == 12:
            print("House wins!")
            print("Exiting game!")
            sys.exit(0)
        else:
            point = sum_of_results
            print("Your point is: {}".format(point))
    else:
        if sum_of_results == point:
            print("You win!")
            print("Exiting game!")
            should_continue_game = False
        elif sum_of_results == 7:
            print("House wins!")
            print("Exiting game!")
            should_continue_game = False
        else:
            print("Continue to next round")

