#9.cretae a class Laptop witha constructor that initi..brand and ram size.print the laptop specifications
class Laptop():
    def __init__(self,brand,Ramsize):
        self.brand=brand
        self.Ramsize=Ramsize
    def display(self):
        print(self.brand,self.Ramsize)
lap=Laptop("Acer","16GB")
lap.display()
