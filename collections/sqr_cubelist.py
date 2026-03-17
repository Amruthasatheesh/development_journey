#w.a.p to create two list squares_list and cube_list
numbers=[2,4,5,6,12,13]
sqr_list=[]
cube_list=[]
for num in numbers:
    square=num*num
    sqr_list.append(square)
    cube=num**3
    cube_list.append(cube)
print("square list",sqr_list)
print("cube list",cube_list)    

