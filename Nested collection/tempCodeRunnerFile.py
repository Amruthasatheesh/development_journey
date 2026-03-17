class Animal:
    def eat(self):
        print("Animal have eat method")
class Lion(Animal):
    def eat(self):
        print("Lions are carnivores")
class Cow(Animal):
    def eat(self):
        print("Cows are herbivores")
a=Lion()
a.eat()
b=Cow()
b.eat()