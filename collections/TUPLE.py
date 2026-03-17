#TUPLE
"""

def count(self,values)
def index(self, value)
* orderd
* Duplicate values are allowed
* immutable:changes not possible in tuple

"""

prices=(200,300,400,300)
print(prices.count(300))

print(prices.index(200))

#create a tuple and store your age only
age=(24)
print(type(age)) # need to put a coma ',' here otherwise its treat/considered as a int data type
age=(24,)
print(type(age))# tuple data type