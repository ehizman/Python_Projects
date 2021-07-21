import random


def roll_dice():
    result: tuple = (random.randrange(1, 7), random.randrange(1, 7))
    return result


def display_dice(result):
    print("You rolled {} and {} = {}".format(result[0], result[1], result[0] + result[1]))


def process_result_of_dice_roll(sum_of_rolls):
    if sum_of_rolls in (7, 11):
        print("You win!")
        return "ABORT"
    elif sum_of_rolls in (2, 3, 12):
        print("House wins!")
        return "ABORT"
    else:
        print("Your point is: {}".format(player_point))
        print()
        return "CONTINUE"


if __name__ == "__main__":
    print("Welcome to the game of craps")
    print("Prepare to roll dice")
    print()

    result_of_rolling_dice: tuple = roll_dice()
    display_dice(result_of_rolling_dice)
    sum_of_dice_results: int = sum(result_of_rolling_dice)
    player_point = sum_of_dice_results
    game_status = process_result_of_dice_roll(sum_of_dice_results)

    while game_status == "CONTINUE":
        result_of_rolling_dice = roll_dice()
        display_dice(result_of_rolling_dice)
        sum_of_dice_results = sum(result_of_rolling_dice)
        if sum_of_dice_results == 7:
            print("House wins!")
            game_status = "ABORT"
        elif sum_of_dice_results == player_point:
            print("You win!")
            game_status = "ABORT"
        else:
            print("Next Round....")
            print()

    print("Exiting game...")

