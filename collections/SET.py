#SET
"""
def add(self,value)=> to add a value to the set
def union(self,set)=> combine all values with out repitition
def intersectioon(self,set)=> common values only
def difference(self,set)=> remove elements from set a ,if it is in set a 
def issuperset(self,set)=> set a is the superset if seb ,bcos set B is created from set A
def issubset(self,set)=> set B is subset of set A 
"""
foods={"dosa","idli","friedrice"}
print(foods.add("biriyani"))
#st=set()=>empty set
#set={}=> empty dictionary


st={10,20,30,40,50}
print(st) # unordered

st={10,20,30,40,40}
print(st) # duplicates are not allowed here,but mutable

colors={"green","red","blue","black"}
print(colors)
# to print one by one
colors={"green","red","blue"}
for c in colors:
    print(c)

foods={"dosa","idli","friedrice"}
foods.add("biriyani")
print(foods)   

set_a={10,20,40,50,100}
set_b={40,50,200,300}
u_set=set_a.union(set_b)
print(u_set)

i_set=set_a.intersection(set_b)
print(i_set)

d_set=set_a.difference(set_b)
print(d_set)

set_a={100,200,10,15,30,40}
set_b={15,30,40}
print(set_a.issuperset(set_b)) #set A is superset of set b
print(set_b.issubset(set_a)) # set b is subset of set A
