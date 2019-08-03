import random


def dice():
    while True:
        print(random.randint(1, 6))
        answer = input("Do you want to roll again? Y/N>> ").lower()
        if str(answer) == "y":
            print(dice())
        elif str(answer) == "n":
            print("Program Ended")
        else:
            print("Wrong Answer")
        break


dice()
