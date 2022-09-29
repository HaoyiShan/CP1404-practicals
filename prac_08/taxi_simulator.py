from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
bill = 0.00
current_taxi = None


def main():
    print("Let's drive!")
    while menu() is True:
        print("...")
    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    n = 0
    for car in taxis:
        print("{} - {}".format(n, car))
        n += 1


def menu():
    print("q)uit, c)hoose taxi, d)rive")
    choose = input(">>>")

    if choose == "q":
        return False

    elif choose == "c":
        n = 0
        print("Taxis available:")
        for car in taxis:
            print("{} - {}".format(n, car))
            n += 1
        try:
            num_car = int(input("Choose taxi: "))
            car = taxis[num_car]
            print("Bill to date: ${}".format(bill))
            global current_taxi
            current_taxi = num_car
            return True
        except IndexError:
            print("Invalid taxi choice")
            print("Bill to date: ${}".format(bill))
            return True
        except ValueError:
            print("Invalid taxi choice")
            print("Bill to date: ${}".format(bill))
            return True

    elif choose == "d":
        driving(current_taxi)
        return True

    else:
        print("Invalid option")
        print("Bill to date: ${}".format(bill))
        return True


def driving(num_car):
    if num_car is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far?"))
        c = taxis[num_car]
        c.drive(distance)
        global bill
        try:
            bill = bill + c.get_fare() + c.flagfall
            print("Your {} trip cost you ${}".format(c.name, c.get_fare()))
            print("Bill to date: ${}".format(bill))
        except AttributeError:
            bill = bill + c.get_fare()
            print("Your {} trip cost you ${}".format(c.name, c.get_fare()))
            print("Bill to date: ${}".format(bill))

main()
