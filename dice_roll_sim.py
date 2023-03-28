import random


def get_player_input():
    print("Enter a dice you'd like to roll: ")
    input_str = input()

    number = int(input_str.split('d')[0])

    if "+" in input_str:
        modifier = int(input_str.split('+')[-1])
    elif "-" in input_str:
        modifier = - int(input_str.split('-')[-1])
    else:
        modifier = 0

    dice_size = int(input_str.replace("d", " ").replace("+", " ").replace("-", " ").split(' ')[1])

    return number, dice_size, modifier


def dice_roll(size=6):
    if size in [3, 4, 6, 8, 10, 12, 20, 100]:
        return random.randint(1, size)
    else:
        return f"{size}-sided dice doesn't exist."


def multiple_dices(number):
    return [dice_roll() for i in range(number)]


def roll():  # work in progress
    number, dice_size, modifier = get_player_input()

    rolls = [dice_roll(dice_size) for i in range(number+1)]

    return number, dice_size, modifier, rolls


# test

# for i in range(0,10):
#   print(dice_roll(6))

# for i in range(0,10):
#   print(multiple_dices(4))

# print(get_player_input())

print(roll())
