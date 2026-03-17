#6.create a class person with a constr that initi..name and city.display the info
class Person():
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def display(self):
        print(self.name,self.city)

person=Person("vaishnav","kochi")
person1=Person("vishaal","thrissur")
person.display()
person1.display()
