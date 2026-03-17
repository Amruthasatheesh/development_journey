"""
inheritance: child class Accessing the attributes and methods from the parent class
single inheritance
"""


class Parent:
    def house(self):
        print("parent class house method")

class Child(Parent):#here accessing from the parent class
    def mobile(self):
        print("child class mobile method")
child_instance=Child()
child_instance.mobile()
child_instance.house()