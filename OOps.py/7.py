#create class product with a constructor that initializes product name and price.print the product details
class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name,self.price)
pro=Product("flask",450)
pro.display()