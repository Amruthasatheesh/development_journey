"""
using#Constructor:__init__
no need to set that class name seperately ,
no need to call 
__init__ automatically invoked during object creation
constructors are used to initialize the attributes inside a class

"""

class Mobile:
    def __init__(self,image,name,price,rating):
        self.image=image
        self.name=name
        self.price=price
        self.rating=rating
    def display(self):
        print(self.image,self.name,self.price,self.rating)

Mobile_instance=Mobile("iphpne16.png","iphone16",1200000,4.5)
Mobile_instance.display()