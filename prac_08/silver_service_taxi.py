from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.flagfall = 4.50
        self.fanciness = fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)
