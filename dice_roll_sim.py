import random


def dice_roll(size=6):
    if size in [3, 4, 6, 8, 10, 12, 20, 100]:
        return random.randint(1, size)
    else:
        return f"{size}-sided dice doesn't exist."

def multiple_dices(number):
  return [dice_roll() for i in range(number)]


# test
# for i in range(0,10):
#   print(dice_roll(6))


for i in range(0,10):
  print(multiple_dices(4))