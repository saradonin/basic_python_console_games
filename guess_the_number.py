from random import randint


def guess_the_number():
    """
    Prompts user to guess the number from 1 to 100.
    Returns feedback whether number is too small or too big.
    :return: str
    """
    answer = randint(1, 101)
    print("Guess the number from 1 to 100: ")

    while True:
        try:
            number = float(input())
            if number == answer:
                return "You win!"
            elif number > answer:
                print(f"Too big!")
            else:
                print(f"Too small!")
        except ValueError:
            print("It's not a number!")


print(guess_the_number())
