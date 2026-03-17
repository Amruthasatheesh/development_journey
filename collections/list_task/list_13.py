#Write a program to merge two lists [1, 2, 3] and [4, 5, 6] and display the final list without modifying the original lists

list_a=[1,2,3]
list_b=[4,5,6]
new_list=[]
new_list=list_a+list_b
print(new_list)


#or another way using extend method

list_a=[1,2,3]
list_b=[4,5,6]
new_list=list_a.copy()
new_list.extend(list_b)
print(new_list)

