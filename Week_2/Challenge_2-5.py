import random


def dice():
    while True:
        print(random.randint(1, 6))
        answer = input("Do you want to roll again? Y/N>> ").lower()
        if str(answer) == "y":
            return dice()
        elif str(answer) == "n":
            return "Program Ended"
        else:
            return"Wrong Answer"


print(dice())
