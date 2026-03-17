"""
Multilevel inheritance:one by one
"""


class GrandParent:
    def properties(self):
        print("grand parent properties")
class Parent(GrandParent):
    def house(self):
        print("parent house method")

class Child(Parent):
    pass
child_instance=Child()
child_instance.properties()
child_instance.house()
