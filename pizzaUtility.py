from pizzaApp import net


import random


descount = 0


def game():
    play = input("Do you what to play? ")
    # net += size() + extra()
    while play == "yes" or play == "y":
        random1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        random2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        lot = random1 * random2
        discount = (net * lot) / 100
        print("Discount percent after playing Dices is:", discount, "%")
        return discount

    else:
        return 0


