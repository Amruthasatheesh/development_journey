#5.cretae a class circle with a constructor that takes radius.write a method to calculate the area of the circle
class Circle():
    def __init__(self,radius):

        self.radius=radius
        self.area=3.14*radius*radius
    def display(self):
        print("radius is",self.radius,"area of circle is",self.area)
cir=Circle(3)
cir.display()
        
