from silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Limo", 100, 2)

    silver_taxi.drive(18)
    print(silver_taxi)
    print(f"Fare: ${silver_taxi.get_fare()}")


if __name__ == "__main__":
    main()
