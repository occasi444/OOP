class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The " +self.model+ " is driving")

    def stop(self):
        print("The " +self.model+ " has stopped")

class Audi(Car):

    def __init__ (self, make, model, year, color, speed):

        super().__init__ (make, model, year, color)

        self.speed = speed

A6 = Audi("Audi", "A6", 2012, "silver", 270)

print (A6.speed)