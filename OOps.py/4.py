#4create a class car witha constructor thaat initializes brand and model.print the car details using a method
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(self.brand,self.model)
car=Car("Toyota","corolla 1.6")
car.display()