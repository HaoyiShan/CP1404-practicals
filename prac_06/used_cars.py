"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()


def limo():
    car_limo = Car(100)
    car_limo.add_fuel(20)
    print("fuel =", car_limo.fuel)
    car_limo.drive(115)
    print("odo =", car_limo.odometer)


limo()


def new_car():
    car_name = input("Please enter the name of the car:")
    car_furl = input("Please enter the initial fuel amount:")
    car = Car(car_name, car_furl)
    print(car)


new_car()
