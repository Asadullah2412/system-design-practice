# Design a parking lot 
from datetime import datetime
# parking lot

class ParkingLot:

    def __init__(self,parkingSpots = 10):
        self.parkingSpots = parkingSpots
        self.space = []

    def checkVacant(self):

        if self.parkingSpots > len(self.space):
            return True
        else:
            return False

    def parkVehicle(self,vehicle):
        
        self.space.append(vehicle)
        return "vehicle parked"
    
        
    def removeVehicle(self,vehicle):
        if vehicle in self.space:

            self.space.remove(vehicle)
            return "True"
        return False

    def showParking(self):
        for vehicle in self.space:
            print(f" - {vehicle.numberPlate}")


class Vehicle:

    def __init__(self,numberPlate,):

        self.numberPlate = numberPlate
        self.entryTime = None
        self.exitTime = None



class Ticket:

    @staticmethod
    def issueTicket(vehicle):
        vehicle.entryTime = datetime.now()
        Ticket = f"{vehicle.numberPlate} at {vehicle.entryTime}"
        return Ticket
    @staticmethod
    def exitTicket(vehicle):
        vehicle.exitTime = datetime.now()
        

        Ticket = f"{vehicle.numberPlate} at {vehicle.exitTime}"
        return Ticket


class ParkingManager:

    def __init__(self, parkingSpots=10,):
        self.parking_lot = ParkingLot(parkingSpots)
        
    def emptyParkingLot(self):
        self.parking_lot.space = []
        return True
    
    def newVehicle(self,numberPlate):
          # 1. vehicle enters
        if self.parking_lot.checkVacant() == True:
            vehicle = Vehicle(numberPlate=numberPlate)
            ticket = Ticket.issueTicket(vehicle=vehicle)
            self.parking_lot.parkVehicle(vehicle)
        else: 
            return "Parking is full"

        return ticket

    
    def exitVehicle(self,numberPlate):
        for v in self.parking_lot.space:
            if v.numberPlate == numberPlate:

                ticket = Ticket.exitTicket(vehicle=v)
                self.parking_lot.removeVehicle(vehicle=v)
                return ticket
        
        return "not found"


pm = ParkingManager(parkingSpots=5)
pm.emptyParkingLot()

print("--- Trying to exit cars from an empty lot ---")
for i in range(1, 3):
    print(pm.exitVehicle(str(i)))

print("\n--- Parking 6 cars into 5 spots ---")
for i in range(1, 7):
    print(pm.newVehicle(str(i)))

print("\n--- Current Parked Vehicles ---")
pm.parking_lot.showParking()

print("\n--- Exiting vehicle 3 ---")
print(pm.exitVehicle("3"))

print("\n--- Current Parked Vehicles After Exit ---")
pm.parking_lot.showParking()