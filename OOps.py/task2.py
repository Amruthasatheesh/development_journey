#create a class rectangle with a constructor that takes length and width.write a method to calculate the area of rectangle
class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.Area=length*width
    def display(self):
        print("length is",self.length,"width is",self.width,"Area of rectangle is",self.Area)

rect_instance=Rectangle(10,12)        
rect_instance.display()        

        
