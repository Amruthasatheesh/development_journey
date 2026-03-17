# Write a program to count positive and negative numbers in a list.

list=[10,-1,-2,3,4,6]
pos_count=0
neg_count=0
for lst in list:
    if lst>0:
        pos_count+=1
    elif lst<0:
        neg_count+=1
print("positve count is",pos_count)
print("negative count is",neg_count)            
