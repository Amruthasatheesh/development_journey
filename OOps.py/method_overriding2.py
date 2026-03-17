class Shapes:
    def area(self):
        print("calculating the area of shape")

class Square(Shapes):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("area of square is:",self.side**2)
class Rectangle(Shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area of rectangle is",self.l*self.b)

sq_instance=Square(4)
sq_instance.area()
rect_instance=Rectangle(4,5)
rect_instance.area()