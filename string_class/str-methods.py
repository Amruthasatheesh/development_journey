# name="Luminar technolab"
# print(name.capitalize()) # returns the capitilized version of the string(ist letter only changes to capital)
# print(name.casefold()) # returns the lowercase of the ist letter only

"""
class str
def capitalize(self,substr)=>return ist substr as capital or uppercase
def casefold(self,substr)=> return the ist substr as lowercase
def index(self,substr)=>return index of substr
def find(self,substr)=> return the first index of substr
# but in find =>the error shows as -1
def rfind(self,substr)=> return the right first index of substr
def count(self,substr)=> returns the number of time substr appears

"""

     #01234567890123456
# name="luminar technolab"

# print(name.index("ch")) # returns the ist index of the string even if there is two string characters are asked
# print(name.index("lab"))# returns the ist index of str labs of "l"
# print(name.find("ch"))# also returns the ist index of that substr

# name="luminarch technolab"# both have ch in str so find method returns the index of ist ch
# print(name.find("ch"))

# name="luminar technolab"
# print(name.find("labs)")) # here the str"labs is not here so,instead of error it shows"-1" here in find method

name="luminarch technolab"
print(name.rfind("ch"))# returns index of right side str in "ch"returns the last occurence here

name="luminarch Technolab Technohub"
print(name.count("Tech"))# two times tech sub str appears here,no of occurences
