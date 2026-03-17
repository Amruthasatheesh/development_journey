class Brand:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Product(Brand):
    def __init__(self,name,title,price):
        super().__init__(name)
        self.title=title
        self.price=price
    def display(self):
        super().display()
        print(self.title,self.price)
pr_instance1=Product("de construct","sunscreen",298)
pr_instance2=Product("Mars","lipstick",550)
pr_instance3=Product("lakme","kajol",150)
pr_instance1.display()
pr_instance2.display()
pr_instance3.display()