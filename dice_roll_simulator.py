import random


def get_player_input():
    """
    Prompts used to input string data defining parameters of dice rolls.
    Takes string in format: xDy+z
    where:
    x - number of dice (optional, default = 1)
    y - size of the single dice from set [3, 4, 6, 8, 10, 12, 20, 100]
    z - modifier (optional, default = 0)
    :return: tuple of int values (number, dice_size, modifier)
    """
    print("Enter a dice you'd like to roll: ")
    while True:
        input_str = input().lower()

        # test for empty input
        if not input_str:
            print("Invalid input. Try again.")
            continue

        # test for 'd'
        if 'd' not in input_str:
            print("Invalid input. Try again.")
            continue

        try:
            # number of dice to roll
            number = input_str.split('d')[0]
            if number == '':
                number = 1
            else:
                number = int(number)

            # modifier
            if "+" in input_str:
                modifier = int(input_str.split('+')[-1])
            elif "-" in input_str:
                modifier = - int(input_str.split('-')[-1])
            else:
                modifier = 0

            # dice size
            dice_size = int(input_str.replace('d', ' ').replace('+', ' ').replace('-', ' ').split(' ')[1])
            if dice_size in [3, 4, 6, 8, 10, 12, 20, 100]:
                return number, dice_size, modifier
            else:
                print("Invalid dice size. Try again.")

        except ValueError:
            print("Invalid input. Try again.")


def dice_roll(dice_size=6):
    """
    Takes dice size as input (default value = 6), returns the result of the random roll.
    :param dice_size: int - size of the dice
    :return: int - result of a single dice roll
    """
    return random.randint(1, dice_size)


def roll():
    """
    Calls external function get_player_input to generate input data: number (int) - number of dice, dice_size (int) - size of the dice, modifier (int) - result modifier.
    Returns the sum of all dice rolls modified by modifier value.
    :return: int - sum of all rolls modified by modifier value
    """
    number, dice_size, modifier = get_player_input()

    rolls = ([dice_roll(dice_size) for i in range(number)])
    result = sum(rolls) + modifier
    return result


# # for detailed information about the dice rolls uncomment 6 lines below
#     return f"""Number of dices: {number}
# Dice size: {dice_size}
# Modifier: {modifier}
# Rolls: {rolls_str}
# Result: {result}
# """


print(roll())
