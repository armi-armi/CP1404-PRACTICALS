from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Old Clunker", 100, 50)

    for i in range(10):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempted to drive 10 km. Drove {distance_driven} km. Odometer: {unreliable_car.odometer}")


if __name__ == "__main__":
    main()
