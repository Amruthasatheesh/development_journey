#find the duplicate numbers without using any predefined methods
# lst=[10,11,12,11,13,15,14,13]
# def find_duplicates(arr):
#     arr.sort()
#     for prev in range(0,len(arr)-1):#bcos the previous is always -1 step beforeso,length -1 of previous 
#         next=prev+1
#         difference=arr[prev]-arr[next]
#         if difference==0:
#             print(arr[prev])
# find_duplicates([10,11,12,11,13,15,14,13])
# #same method without using function()
# lst=[10,11,12,11,13,15,14,13]
# lst.sort()
# for prev in range(0,len(lst)-1):
#     next=prev+1
#     difference=lst[next]-lst[prev]
#     if difference==0:
#         print(lst[prev])


# def two_pair_sum(arr,target):
#     arr.sort()
#     left=0
#     right=len(arr)-1
    
#     while(left<right):
#         current_sum=arr[left]+arr[right]
#         if current_sum==target:
#             print(arr[left],arr[right])
#             return
#         elif current_sum<target:
#             left+=1

#         else:
#             current_sum>target

#             right=-1

#     print("no pair found")

# two_pair_sum([2,3,4,5,8],12)
#find the duplicate numbers without using any predefined methods
# lst=[10,11,12,11,13,15,14,13]
# def duplicate_num(arr):
#     arr.sort()
#     for prev in range(0,len(arr)-1):
#         next=prev+1
#         difference=arr[next]-arr[prev]
#         if difference==0:
#             print(arr[next])
# duplicate_num([10,11,12,11,14,15,14])

#missing number

def missing_num(arr):
    arr.sort()
    if arr[0]!=1:
        print("1")
        return
    for prev in range(0,len(arr)-1):
        next=prev+1
        difference=arr[next]-arr[prev]
        if difference!=1:
            print(arr[prev]+1)
            break
    else:
        print(arr[-1]+1)
missing_num([1,2,3,5])





