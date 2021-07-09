#parent class
class Fleet:
    def __init__(self,veh_class,make,year,fuel_type):
        self.veh_class = veh_class
        self.make = make
        self.year = year
        self.fuel_type = fuel_type
    def replaceVehicle(self):   # utilizing polymorphism on this method. 
        if self.year <2015:
            print("replace unit")
        else:
            print("unit still operational")
#Child Class 

class Forklift(Fleet):
    def __init__(self,veh_class,make,year,fuel_type,wheel_type,fork_length,hours):
        super().__init__(veh_class,make,year,fuel_type)
        self.wheel_type = wheel_type
        self.fork_length = fork_length
        self.hours = hours
        
    def replaceVehicle(self):
        if (self.year < 2017 and self.wheel_type =="tracks") or self.hours >20000:
            print("replace forklift")
        elif self.year < 2014 or self.hours > 22000:
            print("replace forklift")
        else:
            print("lift still operational")

    def indoorOrOutdoor(self):
        if self.wheel_type =="tracks" and self.fuel_type !="electric":
           print("outdoor")
        else:
            print("indoor")

# 2nd child class 
class Truck(Fleet):
    def __init__ (self,veh_class,make,year,fuel_type,miles,bed_length):
        super().__init__(veh_class,make,year,fuel_type)
        self.miles = miles
        self.bed_length = bed_length
    def replaceVehicle(self):
        if self.year < 2015 or self.miles > 100000:
            print("replace truck")
        else:
            print("truck still operational")
        


lift1 = Forklift("MHE Class 6","Toyota",2016,"propane","tracks","48",21000) # calling child

lift1.replaceVehicle()


lift2 = Forklift("MHE Class 6","Toyota",2014,"electric","wheels","36",15000) # calling child checking condition. 

lift2.replaceVehicle()



unit1 = Fleet("Class 2","Ford",2016,"Gasoline")  

unit1.replaceVehicle()# calling parent


truck1 = Truck("Class 2","Chevy",2018,"Gasoline",109000,8)

truck1.replaceVehicle()

