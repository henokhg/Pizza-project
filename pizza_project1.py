import random


def size():
    global count
    pizza_size = {"s": 40,
                  "m": 50,
                  "l": 60,
                  "xl": 75}

    print(pizza_size)
    user = input("Enter pizza size: ")
    quantity = int(input("How much you need? "))
    count += pizza_size[user] * quantity
    return count


def extra():
    global count
    global spice
    extra_spice = input("Do you need extra? ")
    if extra_spice == "yes" or extra_spice == "y":
        count += spice
        return count
    else:
        return 0


def live():
    living = {
        "beersheva": 20,
        "b": 20,
        "a": 60,
        "another": 60}
    print(living)
    place = input("Where do you live? ")
    city = living[place]
    return city


def game():
    global net
    play = input("Do you what to play? ")
    while play == "yes" or play == "y":
        random1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        random2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        lot = random1 * random2
        discount = (net * lot) / 100
        print("Discount percent after playing Dices is:", discount, "%")
        return discount

    else:
        return 0


spice = 2
count = 0
net = 0
age = int(input("Enter your age: "))


if age >= 18:
    print("\n\n\t\t\t\t\t\t\t**** WELLCOME TO OUR PIZZA *****\n\n")
    net += size() + extra()
    total_net = (net + live())
    total_net_discount = (total_net - game())
    con = input("Do you want to continue? ")
    if con == "no" or con == "n":
        print("Total price is: ", total_net)
        print("Total price after discount: ", round(total_net_discount, 2))
        print("*********THANKS YOUR BUYING!!!****** ")

    else:
        while True:
            net += size() + extra()
            con = input("Do you want to continue? ")
            if con == "no" or con == "n":
                print("Total price is: ", total_net)
                print("Total price after discount: ", round(total_net_discount, 2))
                print("*********THANKS YOUR BUYING!!!****** ")
                break

else:
    print("sorry, your are under age!")





