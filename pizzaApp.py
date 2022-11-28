spice = 2
count = 0
net = 0
total_net = 0
total_net_discount = 0


def pizza():

    age = int(input("Enter your age: "))
    while age >= 18:
        global net, total_net_discount
        print("\n\n\t\t\t\t\t\t\t**** WELLCOME TO OUR PIZZA *****\n\n")
        global total_net
        from pizzafunction import size
        from pizzafunction import extra
        from pizzafunction import live
        from pizzaUtility import game
        net += size() + extra()
        con = input("Do you want to continue? ")
        print(net)
        if con == "no" or con == "n":
            total_net += net + live()
            total_net_discount = total_net - game()
            print("Total price is: ", total_net)
            print("Total price after discount: ", round(total_net_discount, 2))
            print("*********THANKS YOUR BUYING!!!****** ")

        else:
            while True:
                from pizzafunction import size
                net += size() + extra()
                con = input("Do you want to continue? ")
                if con == "no" or con == "n":
                    print("Total price is: ", total_net)
                    print("Total price after discount: ", round(total_net_discount, 2))
                    print("*********THANKS YOUR BUYING!!!****** ")
                    break

    else:
        print("sorry, your are under age!")
        # exit()


# pizza()
