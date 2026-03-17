#Task 29 || OOP – Polymorphism || 12-03-2026

# Task 29 || OOP – Polymorphism || 12-03-2026

#Create two classes Dog and Cat. Both classes should have a method sound(). Print different sounds for each animal.

# class Dog:
#     def sound(self):
#         print("bow")
# class Cat():
#     def sound(self):
#         print("meow")
# dog_obj=Dog()
# cat_obj=Cat()

# dog_obj.sound()
# cat_obj.sound()


2#Create two classes Rectangle and Circle. Both classes should have a method area(). Calculate the area for each shape.

# class Rectangle:
#     def area(self,l,b):
#         print("Area of Rectangle:", l*b)

# class Circle:
#     def area(self,r):
#         print("Area of Circle:", 3.14*r*r)

# rec=Rectangle()
# rec.area(5,4)
# cir=Circle()
# cir.area(3)

# 3#Create a class Bird with a method fly(). Create subclasses Sparrow and Ostrich that override the fly() method with different behavior

# class Bird:
#     def fly(self):
#         print("fly method of a bird")
# class Sparrow(Bird):
#     def fly(self):
#         print("sparrow flies high")
# class Ostrich(Bird):
#     def fly(self):
#         print("ostrich can't fly")
# obj=Sparrow()
# obj.fly()
# obj1=Ostrich()
# obj1.fly()
# #4 Create two classes Car and Bike. Both classes should have a method start() that prints different messages.
# class Vehicle:
#     def start(self):
#         print("all vehicle have start method")
# class Car(Vehicle):
#     def start(self):
#         print("car's start method")
# class Bike(Vehicle):
#     def start(self):
#         print("bikes's start method")       

# car=Car()
# car.start()
# bike=Bike()
# bike.start()
# #5Create a class Employee with a method work(). Create subclasses Developer and Manager that override the work() method.

# class Employee:
#     def work(self):
#         print("All employee,s work method")
# class Developer(Employee):
#     def work(self):
#         print("developer's work method")
# class Manager(Employee):
#     def work(self):
#         print("manager work method")
# dev=Developer()
# manager=Manager()
# dev.work()
# manager.work()
# #6 Create two classes India and USA with a method capital(). Print the capital city of each country.
# class Country:
#     def capital(self):
#         print("All country's have their own capital city")
# class India(Country):
#     def capital(self):
#         print("capital city of india is delhi")
# class Usa(Country):
#     def capital(self):
#         print("usa's capital  city is washington")

# a=India()
# a.capital()
# b=Usa()
# b.capital()
# #7Create a class Shape with a method draw(). Create subclasses Square and Triangle that override the draw() method.

# class Shape:
#     def draw(self):
#         print("All shapes have an draw method")
# class Square(Shape):
#     def draw(self):
#         print("square draw method")
# class Triangle(Shape):
#     def draw(self):
#         print("traingle draw method")
# a=Square()
# a.draw()
# b=Triangle()
# b.draw()
# #8Create a class Payment with a method pay(). Create subclasses CreditCard and UPI that override the pay() method.

# class Payment:
#     def pay(self):
#         print("All payment methods")
# class CreditCard(Payment):
#     def pay(self):
#         print("SBI'S credit card")
# class UPI(Payment):
#     def pay(self):
#         print("google pay is an UPI's method")
# a=CreditCard()
# a.pay()
# b=UPI()
# b.pay()
# 9# Create a class Animal with a method eat(). Create subclasses Lion and Cow that override the eat() method.
# class Animal:
#     def eat(self):
#         print("Animal have eat method")
# class Lion(Animal):
#     def eat(self):
#         print("Lions are carnivores")
# class Cow(Animal):
#     def eat(self):
#         print("Cows are herbivores")
# a=Lion()
# a.eat()
# b=Cow()
# b.eat()
# #10. Create a class Vehicle with a method move(). Create subclasses Car and Airplane that override the move() method.
class Vehicle:
    def move(self):
        print("All vehicles have move method")
class Car(Vehicle):
    def move(self):
        print("moves on roads")
class Airplane(Vehicle):
    def move(self):
        print("moves in the air")
a=Car()
a.move()
b=Airplane()
b.move()


