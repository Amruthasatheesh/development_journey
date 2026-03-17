class Student:
    name:str
    course:str
    roll_no=int
    def __init__(self,name,course,roll_no):
        self.name=name
        self.course=course
        self.roll_no=roll_no
    def display(self):
        print(self.name,self.course,self.roll_no)
Student_instance=Student("Anu","DS and ML",101)
Student_instance.display()


Student_instance2=Student("Sreelakshmi","Cybersecurity",112)
Student_instance2.display()