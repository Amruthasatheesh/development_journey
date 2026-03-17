#create a class student with a constructor that initialize name  and age.create an object and dispaly the details
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
Student_instance1=Student("Arya",24)
Student_instance1.display()




