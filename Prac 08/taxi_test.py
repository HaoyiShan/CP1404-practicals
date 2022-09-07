from taxi import Taxi

taxi = Taxi("Prius 1", 100)
taxi.drive(40)
print("{}\nfare: ${}".format(taxi, taxi.get_fare()))

taxi.start_fare()

taxi.drive(100)
print("{}\nfare: ${}".format(taxi, taxi.get_fare()))
