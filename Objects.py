class Car:
    def __init__(self,colour, model, company):
        self.colour = colour
        self.model = model
        self.company = company
    
    def setCar(self):
        print("SetCar function has begun")

    def getCar(self):
        print("Car")
    
redCar = Car("red","model1","companyA")
blueCar = Car("blue","model2","companyB")
redCar.setCar()
blueCar.setCar()

