import random


def get_player_input():
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
    return random.randint(1, dice_size)


def roll():  # work in progress
    number, dice_size, modifier = get_player_input()

    rolls = [dice_roll(dice_size) for i in range(number)]
    result = sum(rolls) + modifier

    return f"""
Number of dices: {number} 
Dice size: {dice_size} 
Modifier: {modifier} 
Rolls: {rolls}
Result: {result}
"""


# test

# for i in range(0,10):
#   print(dice_roll(6))

# print(get_player_input())

print(roll())
