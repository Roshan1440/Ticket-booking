import json
seats = []
for i in range(1,41):
    seats.append(i)
print("available seats are",seats)

trips = [ "Mustang", "Pokhara", "Chitwan"]

class Trip:
    def __init__ (self, dest):
        self.dest = dest




class Booking:
    def __init__(self, CustomerName, PhNo ,TripDest,SeatNo, IsPaid):
        self.CustomerName = CustomerName
        self.PhNo = PhNo
        self.TripDest = TripDest
        self.SeatNo = SeatNo
        self.IsPaid = IsPaid

    def validSeat(self,SeatNo):
        if (self.SeatNo in seats):
            return 0
        else:
            return 1




if __name__ == "__main__":
     name=input("Enter your name")
     ph = input("Enter your phone number")
     destination = input("Enter your preferred destination from:" )
     seatNo = int(input("select a valid seat no from :"))
     payment = input("are  you paying now or later? enter 1 or 0")

     b1 = Booking(name,ph, destination, seatNo, payment)

     if (b1.validSeat(seatNo) == 1):
        print("the seat has been already chosen. Please pick another one")

     if(b1.validSeat(seatNo) == 0):
         seats.remove(seatNo)
         print("booking confirmed with details",b1.CustomerName,b1.SeatNo,b1.TripDest)

     with open("bookingData.txt", "w") as file:
         file.write(json.dumps(b1.__dict__))


    