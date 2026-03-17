class Biriyani():
    title:str
    category:str
    price:str#set_biriyani is intialization
    def __init__(self,title,category,price):
        self.title=title
        self.category=category
        self.price=price
     #initialize,set attribute,instance variables ie constructor
    def display(self):  
        print(self.title,self.category,self.price) 
Biriyani_instance=Biriyani("Hyderabadi","non-veg",250)
Biriyani_instance.display()

Biriyani_instance2=Biriyani("malabar","non-veg",350)
Biriyani_instance2.display()


# class Movie():
#     Director:str
#     actor:str
#     villan:str
#     def set_Movie(self,Direcor,actor,villan):
#         self.Director=Direcor
#         self.actor=actor
#         self.villan=villan
#     def dispaly(self):
#         print(self.Director,self.actor,self.villan)

# Movie_instance=Movie()
# Movie_instance.set_Movie("Basil Joseph","Tovino","Somasundar")
# Movie_instance.dispaly()

