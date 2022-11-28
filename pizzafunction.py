
def size():
    size_count = 0
    pizza_size = {"s": 40,
                  "m": 50,
                  "l": 60,
                  "xl": 75}

    print(pizza_size)
    user = input("Enter pizza size: ")
    quantity = int(input("How much you need? "))
    size_count += pizza_size[user] * quantity
    return size_count


spice = 2


def extra():

    global spice
    extra_count = 0
    extra_spice = input("Do you need extra? ")
    if extra_spice == "yes" or extra_spice == "y":
        extra_count += spice
        return extra_count
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
    live_city = living[place]
    return live_city
