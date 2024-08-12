from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        print(f"q)uit, c)hoose taxi, d)rive\nBill to date: ${bill:.2f}")
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


if __name__ == "__main__":
    main()
