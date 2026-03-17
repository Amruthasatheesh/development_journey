"""
Multiple inheritance
Accessing from both parents class(father and mother class)
"""


class Father:
    def coaching_skill(self):
        print("coaching skill")
class Mother:
    def cooking_skill(self):
        print("cooking skill")
class Child(Father,Mother):
    pass

child_instance=Child()
child_instance.coaching_skill()
child_instance.cooking_skill()