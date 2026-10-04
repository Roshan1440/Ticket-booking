seats = []
for i in range(1,41):
    seats.append(i)
print("available seats are",seats)

trips = {
    "Mustang":1,
    "Pokhara":2
}

bookedSeats=[]
class Trip:
    def __init__ (self, dest, id, price):
        self.dest = dest
        self.id = id
        self.price = price

    def confirmedTrip(self):
        print("Your have selected trip to " + self.dest)


class Booking:
    def __init__(self, seatNo):
        self.seatNo = seatNo

    def checkSeat(self):
        if bookedSeats.contains(seatNo):
            print("Your chosen seat is already booked. Please pick another")
        bookedSeats.append(SeatNo)