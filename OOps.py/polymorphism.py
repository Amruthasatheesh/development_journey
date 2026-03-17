"""
polymorphism: many forms/more than one forms
* method overloading: within same class having same method name and different number of parameters
to over come this ,use args,kwargs
* method overriding

"""

class Calculator:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
cal_instance=Calculator()
print(cal_instance.add(10,20,30,40))# only works the 4 numbers case 
print(cal_instance.add(10,20,30))# error 
print(cal_instance.add(10,20))# error 