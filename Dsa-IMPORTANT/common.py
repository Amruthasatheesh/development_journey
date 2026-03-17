# #method-1
# lst1=[10,11,12,13,14]
# lst2=[8,11,14,15,16]
# # st=set(lst1)
# # st2=set(lst2)
# # i_inter=st.intersection(st2)
# # print(i_inter)

# # method:2
# # for num in lst1:
# #     if num in lst2:
# #         print(num)
# #Method:3 -using extend()
# lst1=[10,11,12,13,14]
# lst2=[8,11,14,15,16]
# lst1.extend(lst2)
# print(lst1)
# lst1.sort()
# for prev in range(0,len(lst1)-1):
#     next=prev+1
#     difference=lst1[next]-lst1[prev]
#     if difference==0:
#         print(lst1[next])
# #method:4




#display the common elements from this 2 lists

def common_elements(arr):
    arr.sort()
    for prev in range(0,len(arr)-1):
        next=prev+1
        difference=arr[next]-arr[prev]
        if difference==0:
           print(arr[next])
common_elements([10,11,12,13,14,11,10,11,10,13,15,13])



