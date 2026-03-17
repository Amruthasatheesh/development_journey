"""w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""
def missing_positive_number(arr):
    arr.sort()
    for prev in range(0,len(arr)-1):
        next=prev+1
        difference=arr[next]-arr[prev]
        if difference!=1:
            print(arr[prev]+1 ,"is missing")
            break
    else:
        print(arr[-1]+1)
missing_positive_number([1,2,3,4,5])   
         
#method:2
lst=[2,3,4,5]
length=len(lst)
for i in range(1,length+1):
    if i not in lst:
       print(i)
       break
        