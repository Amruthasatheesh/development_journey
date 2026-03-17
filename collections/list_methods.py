"""
class list:
    def append(self,object) add object at end of the list
    def insert(self,index,object) insert new object at specified index
    def pop(self,index) remove and return specified element at index (default value:-1 or removes the last element as default value)
    def remove(self,object) removal based on object
    def count(self,object ) frequency of object in this list
    def copy(self) points to the different objects and returns the copy( also introducing the methods "is" and "==")
    def sort (self,reverse=False) #by default ascending order
    def reverse()
    def extend(self,iterable)

"""
# colors=["red","green","violet"]
# colors.append("black")
# print(colors)
# colors=["red","green","violet"]
# colors.insert(2,"yellow")
# print(colors)
colors=["red","green","violet"]
colors.pop(1)
print(colors)
# colors=["red","green","violet"]
# colors.remove("green")
# print(colors)

# colors=["red","violet","black","red","yellow","red"]
# print(colors.count("red"))
sreeyesh_fvt_colors=["red","violet","black","red","green"]
akash_favt_colors=sreeyesh_fvt_colors.copy()
print("sreeyeshcolors",sreeyesh_fvt_colors)
print("aksh colors",akash_favt_colors) #bcos copy method points to the different method otherwise it returns ssame object in both variable objects

# print(sreeyesh_fvt_colors is akash_favt_colors) # is used for compares the  memory location
# print(sreeyesh_fvt_colors==akash_favt_colors)# == used for compare the values
# numbers=[11,12,1,5,2]
# numbers.sort() #by default ascending order takes here
# print(numbers)
 
# numbers=[11,12,1,5,2]
# numbers.sort(reverse=True)
# print(numbers)
# colors=["red","white","blue","black"]
# colors.reverse()
# print(colors)
colors=["red","white","blue","black"]
new_colors=["navyblue","darkred"]
colors.extend(new_colors)
print(colors)