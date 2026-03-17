#w.a.p to cretae two list positive list,negative list
numbers=[10,-12,4,9,-3,-2,15]
pos_list=[]
neg_list=[]
for num in numbers:
    if num>0:
        pos_list.append(num)
    elif num<0:
        neg_list.append(num)
print("positive list",pos_list)
print("negative list",neg_list)            