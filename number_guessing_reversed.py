def guess(min=1, max=1000):
    """
     Play a game where the computer guesses a number in given range (between 1 and 1000 by default) in 10 tries or fewer
     Answer the questions with 'Y' for yes and 'N' for no.
     Returns 'I won!' if the computer guesses the number correctly, or an error message if the user cheats.
    :param min: int - the smallest number in range
    :param max: int - the biggest number in range
    :return: str
    """

    print("""Let's play a game. 
Think of a number between 1 and 1000 and I'll guess it in 10 tries or fewer. 
Answer my questions by pressing keys: 
'Y' for Yes or 'N' for No. 
  """)
    count = 0
    while True:
        guess = int((max - min) / 2 + min)

        print(f"My guess is: {guess}")
        print("Did I guess? [y/n]")
        count += 1

        answer_1 = input().lower()
        if answer_1 not in ('y', 'n'):
            print("Please answer with: 'y' for Yes or 'n' for No")
            continue
        elif answer_1 == 'y':
            return "I won!"
        elif answer_1 == 'n':
            print("Too big? [y/n]")
            answer_2 = input().lower()

            if answer_2 not in ('y', 'n'):
                print("Please answer with: 'y' for Yes or 'n' for No")
                continue
            elif answer_2 == 'y':
                max = guess
            elif answer_2 == 'n':
                print("Too small? [y/n]")
                answer_3 = input().lower()

                if answer_3 not in ('y', 'n'):
                    print("Please answer with: 'y' for Yes or 'n' for No")
                    continue
                elif answer_3 == 'y':
                    min = guess
                elif answer_3 == 'n':
                    print("Don't cheat!")


print(guess())
