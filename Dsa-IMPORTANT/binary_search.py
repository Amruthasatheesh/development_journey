"""
algorithm:







"""
# arr=[10,11,12,13,14,15]
# element=int(input("enter the element:"))
# low=0
# upp=len(arr)-1
# is_present=False
# while(low<=upp):
#     mid=(low+upp)//2
#     if (element==arr[mid]):
#         is_present=True
#         break
#     elif element<arr[mid]:
#         upp=mid-1
#     elif element>arr[mid]:
#         low=mid+1
# print(is_present)




class BinarySearch():
    def solution(self,arr,element):
        low=0
        upp=len(arr)-1
        is_present=False
        while(low<=upp):
            mid=(low+upp)//2
            if element==arr[mid]:
                is_present=True
                break
            elif element<arr[mid]:
                upp=arr[mid]+1

            elif element>arr[mid]:
                low=arr[mid]-1
        return (is_present)
obj=BinarySearch()
arr=[10,11,12,13,14,15]
element=int(input("enter the element:"))
print(obj.solution(arr,element))

