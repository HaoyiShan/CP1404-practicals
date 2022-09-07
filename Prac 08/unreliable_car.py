from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, {}km on current fare, reliability: {}".format(super().__str__(), self.current_fare_distance,
                                                                  self.reliability)

    def drive(self, distance):
        n = random.uniform(1, 100)
        if self.reliability > n:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven
        else:
            distance_driven = super().drive(0)
            return distance_driven
