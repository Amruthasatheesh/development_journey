
#19. Write a class "Student" with attributes (name, marks) and a method to display details.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("student details",self.name,self.marks)
# student_instance=Student("arya",35)
# student_instance.display()

# 20. Extend Student class to calculate grade based on marks.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def calculate_grade(self):
#         if self.marks>90:
#             return "A+"
#         elif self.marks>80:
#             return "A"
#         elif self.marks>70:
#             return "B+"
#         elif self.marks>60:
#             return "B"
#         else:
#             return "failed"
#     def display(self):
#         print("name",self.name)
#         print("marks",self.marks)
#         print("grade",self.calculate_grade())
# student_instance=Student("Amrutha",91)
# print(student_instance.display())

# # 21. Write a program to handle exceptions (division by zero, invalid input).
# try:
#     num1=int(input("enter number"))
#     num2=int(input("enter number"))
#     result=num1/num2
#     print(result)
# except Exception as e:
#     print("division by zero not possible")
# except Exception as e:
#     print("pls enter invalid number")
# finally:
#     print("all code executed")


# 22. Write a program to read a file and store word frequency using dictionary.
# fr=open("OOps.py\\task-30\\read_file_t22.txt","r")
# word=fr.read()
# word_frequency={w:word.count(w)for w in word.split(" ")}
# result=word_frequency
# print(result)
# 23. Write a program using lambda, map, and filter to process a list of numbers.
# lst=[10,22,13,14,16,17]
# even_nums=list(filter(lambda num: num%2==0,lst))
# square_nums=list(map(lambda num:num**2,lst))
# print(even_nums)
# print(square_nums)

# 24. Write a program to demonstrate inheritance and method overriding.
# class Vehicle:
#     def start(self):
#         print("every vehicle have start method")
# class Bike(Vehicle):
#     def start(self):
#         print("bike's start method")
# class Jeep(Vehicle):
#     def start(self):
#         print("jeep have an start method")
# vehicle_instance=Vehicle()
# Bike_instance=Bike()
# Jeep_instance=Jeep()
# vehicle_instance.start()
# Bike_instance.start()
# Jeep_instance.start()

# # 25. Write a program to simulate a simple login system (username & password check).
db_password="ammu@123"
db_user_name="ammu"
user_name=input("enter your name")
if db_user_name==user_name:
    user_password=input("enter your password")
    if db_password==user_password:
        print("login succesfull")
    else:
        print("invalid password")
else:
    print("invalid login credentials")




