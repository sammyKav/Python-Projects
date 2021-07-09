
class Fleet:
    def __init__(self,veh_class,make,year,fuel_type):
        self.veh_class = veh_class
        self.make = make
        self.year = year
        self.fuel_type = fuel_type
    def replaceVehicle(self):
        if self.year <2015:
            print("replace unit")
        else:
            print("still operational")

class Forklift(Fleet):
    def __init__(self,veh_class,make,year,fuel_type,wheel_type):
        super().__init__(veh_class,make,year,fuel_type)
        self.wheel_type = wheel_type

    def replaceVehicle(self):
        if self.year < 2017 and self.fuel_type =='electric':
            print("replace unit")
        elif self.year < 2014:
            print("replace unit")
        else:
            print("still operational")

    
    def indoorOrOutdoor(self):
        if self.wheel_type =="tracks" and self.fuel_type !="electric":
           print("outdoor")
        else:
            print("indoor")




lift1 = Forklift("MHE Class 6","Toyota",2016,"electric","wheels")

lift1.replaceVehicle()

unit2 = Fleet("Class 2","Ford",2016,"Gasoline")

unit2.replaceVehicle()


