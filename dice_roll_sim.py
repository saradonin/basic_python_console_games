import random


def dice_roll(size=6):
    if size in [3, 4, 6, 8, 10, 12, 20, 100]:
        return random.randint(1, size)
    else:
        return f"{size}-sided dice doesn't exist."


for i in range(0, 10):
    print(dice_roll(6))
