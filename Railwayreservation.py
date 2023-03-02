import threading
import time


class Train:
    def __init__(self, train_number, train_name, source, destination, seats):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.seats = seats


class Passenger:
    def __init__(self, name, age, seat_number):
        self.name = name
        self.age = age
        self.seat_number = seat_number


class ReservationSystem:
    def __init__(self):
        self.trains = []
        self.passengers = []
        self.lock = threading.Lock()

    def add_train(self, train):
        self.trains.append(train)

    def reserve_seat(self, train_number, passenger):
        for train in self.trains:
            if train.train_number == train_number:
                with self.lock:
                    if train.seats > 0:
                        train.seats -= 1
                        self.passengers.append(passenger)
                        print(f"Seat booked for {passenger.name} on Train {train_number}")
                    else:
                        print(f"Train {train_number} is sold out")
                break
        else:
            print(f"Invalid train number {train_number}")


# Example usage
if __name__ == '__main__':
    train1 = Train(1, "Express", "Delhi", "Mumbai", 100)
    train2 = Train(2, "Shatabdi", "Chennai", "Bangalore", 50)

    system = ReservationSystem()
    system.add_train(train1)
    system.add_train(train2)

    passenger1 = Passenger("John", 25, 1)
    passenger2 = Passenger("Lisa", 30, 2)

    t1 = threading.Thread(target=system.reserve_seat, args=(1, passenger1))
    t2 = threading.Thread(target=system.reserve_seat, args=(1, passenger2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
