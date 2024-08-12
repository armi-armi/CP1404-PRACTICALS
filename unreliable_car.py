from car import Car
import random

class UnreliableCar(Car):
    """An unreliable version of a Car that only drives successfully some of the time."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it's reliable enough."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
