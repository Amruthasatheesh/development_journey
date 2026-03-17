"""
mapping():can apply on all objects a particular function
filtering():when an certain condition appears
reducing:reduced entire elemets in to single 

"""


lst=[10,11,12,14,15]
map_squares=list(map(lambda n:n**2,lst))
print(map_squares)

#cube
map_cube=list(map(lambda n:n**3,lst))
print(map_cube)

#comprehension
com_sqr=[num**2 for num in lst]
print(com_sqr)
#filter()
evens=list(filter(lambda n:n%2==0,lst))
print(evens)
#even comprehension

even_com=[num for num in lst if num%2==0]
print(even_com)