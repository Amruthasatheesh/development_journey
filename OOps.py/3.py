#3.create a class Employee with a constructor  that initializes employee name and salary.display the emplolyee details
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name,self.salary)
emp_instance=Employee("Anil kumar",50000)
emp_instance=Employee("pradeep",340000)
emp_instance.display()
