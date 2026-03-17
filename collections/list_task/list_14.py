#Given the list [2, 4, 6, 8, 10], create a new list where each element is multiplied by 3.
numbers=[2, 4, 6, 8, 10]
new_list=[]
for num in numbers:
    mul=num*3
    new_list.append(mul)
print(new_list)