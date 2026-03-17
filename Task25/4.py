
#4. Write a Python program to sort a list of tuples based on the second element using a lambda function.
data=[(1,5),(3,2),(2,8)]# indexing is 0,1 based to each tuples ,here the second element based sorting that is,5,2,8==>n[1]
sorted_data=sorted(data,key=lambda n:n[1])
print("sorted_list is",sorted_data)

#sir's version
students=[
    ("hari",145),
    ("dev",135),
    ("ram",125),
    ("kumar",175),
    ("viswa",165),

]
print(sorted(students,key=lambda tp:tp[1],reverse=True))#here the default value customization is done through key=lambda