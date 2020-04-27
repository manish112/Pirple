class Vehicle:

    def __init__(self):
        self.NeedsMaintenance=False
        self.TripsSinceMaintenance=0


    def setMake(self,make):
        self.make=make

    def setModel(self,model):
        self.model=model

    def setYear(self,year):
        self.year=year

    def setWeight(self,weight):
        self.weight=weight


class Cars(Vehicle):

    def Drive(self):
        self.isDriving=True

    def Stop(self):
        self.isDriving=False
        self.TripsSinceMaintenance+=1
        if self.TripsSinceMaintenance==100:
            self.NeedsMaintenance=True

    def Repair(self):
        self.TripsSinceMaintenance=0
        self.NeedsMaintenance=False

class Planes(Vehicle):
    def Flying(self):
        if self.NeedsMaintenance==False:
            self.isDriving=True
        else:
            return False

    def Landing(self):
        self.isDriving=False
        self.TripsSinceMaintenance+=1
        if self.TripsSinceMaintenance==100:
            self.NeedsMaintenance=True

    def Repair(self):
        self.TripsSinceMaintenance=0
        self.NeedsMaintenance=False

car1=Cars()
car1.setMake("Ford")
car1.setModel("X1")
car1.setYear(2019)
car1.setWeight("1200 KG")


car2=Cars()
car2.setMake("BMW")
car2.setModel("X4")
car2.setYear(2018)
car2.setWeight("16200 KG")

car3=Cars()
car3.setMake("Hyndai")
car3.setModel("Santro")
car3.setYear(2007)
car3.setWeight("1100 KG")




for i in range(80):
    car1.Drive()
    car1.Stop()

for i in range(110):
    car2.Drive()
    car2.Stop()

for i in range(50):
    car3.Drive()
    car3.Stop()


print("Car1-> Make: "+car1.make+", Model: "+car1.model+", Year: "+str(car1.year)+", Weight: "+car1.weight+", NeedsMaintenance: "+str(car1.NeedsMaintenance)+", TripsSinceMaintenance: "+str(car1.TripsSinceMaintenance))
print("Car2-> Make: "+car2.make+", Model: "+car2.model+", Year: "+str(car2.year)+", Weight: "+car2.weight+", NeedsMaintenance: "+str(car2.NeedsMaintenance)+", TripsSinceMaintenance: "+str(car2.TripsSinceMaintenance))
print("Car3-> Make: "+car3.make+", Model: "+car3.model+", Year: "+str(car3.year)+", Weight: "+car3.weight+", NeedsMaintenance: "+str(car3.NeedsMaintenance)+", TripsSinceMaintenance: "+str(car3.TripsSinceMaintenance))


plane=Planes()

plane.setMake("Boeing")
plane.setModel("737")
plane.setYear(2015)
plane.setWeight("9200 KG")

for i in range(110):
    status=plane.Flying()
    if status != False:
        plane.Landing()
    else:
        print("The plane can't fly until it's repaired.")


print("Plane-> Make: "+plane.make+", Model: "+plane.model+", Year: "+str(plane.year)+", Weight: "+plane.weight+", NeedsMaintenance: "+str(plane.NeedsMaintenance)+", TripsSinceMaintenance: "+str(plane.TripsSinceMaintenance))

plane.Repair()

print("Plane after repair-> Make: "+plane.make+", Model: "+plane.model+", Year: "+str(plane.year)+", Weight: "+plane.weight+", NeedsMaintenance: "+str(plane.NeedsMaintenance)+", TripsSinceMaintenance: "+str(plane.TripsSinceMaintenance))
