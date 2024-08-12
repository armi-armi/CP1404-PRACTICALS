from taxi import Taxi


def main():
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

    # Restart the meter and drive another 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")


if __name__ == "__main__":
    main()
