import random


def lotto_numbers(range_min=1, range_max=49):
    """
    Picks 6 random numbers in range 1-49
    :param range_min: int
    :param range_max: int
    :return: list[int] - sorted list of 6 int numbers
    """
    number_list = [i for i in range(range_min, range_max + 1)]
    random.shuffle(number_list)
    return sorted(number_list[:6])


def get_player_numbers(range_min=1, range_max=49):
    """
    Prompts user to enter 6 unique numbers from 1 to 49 and returns sorted list of numbers.
    :param range_min: int
    :param range_max: int
    :return: list[int] - sorted list of 6 int numbers
    """
    print("Enter numbers from 1 to 49")
    player_numbers = []

    while len(player_numbers) < 6:
        try:
            num = int(input())
            if num in range(range_min, range_max + 1):  # checking range
                if num not in player_numbers:  # checking repetitions
                    player_numbers.append(num)
                else:
                    print("You can't pick the same number twice!")
            elif num > (range_max + 1):
                print("Too big!")
            else:
                print("Too small!")
        except ValueError:
            print("It's not a number!")

    return sorted(player_numbers)


def compare():
    """
    Takes player bet and lotto numbers and compares the result
    :return: f string - text message
    """
    bet = get_player_numbers()
    win = lotto_numbers()

    bet_str = ", ".join([str(i) for i in bet])
    win_str = ", ".join([str(i) for i in win])

    print(f"Your numbers: {bet_str}")
    print(f"Winning numbers: {win_str}")

    result = [i for i in bet if i in win]

    if len(result) == 0:
        return "You hit nothing. Better luck next time."
    elif len(result) == 1:
        return f"You hit only {len(result)} number. Better luck next time."
    elif len(result) < 3:
        return f"You hit only {len(result)} numbers! Better luck next time."
    else:
        return f"You hit {len(result)} numbers! Congratulations!"


print(compare())
