# class LinearSearch:

#     def solution(self,arr,element):

#         is_present=False

#         for num in arr:

#             if num==element:

#                 is_present=True

#         return (is_present)
    
# ls_instance=LinearSearch()

# arr=[10,11,12,13,14,15]

# element=17
# element=13

# print(ls_instance.solution(arr,element))



# arr=[10,11,12,13,14,15,16]
# element=int(input("enter the element:"))
# is_present=False
# for num in arr:
#     if num==element:
#         is_present=True

# print(is_present)

# class LinearSearch():
#     def solution(self,arr,element):
#         is_present=False
#         for num in arr:
#             if num==element:
#                 is_present=True
#         return (is_present)
# obj=LinearSearch()
# arr=[10,11,12,13,14,15,16,17]
# element=int(input("enter the element:"))
# print(obj.solution(arr,element))






class Linear_Search:
    def solution(self,arr,element):
        is_present=False
        for num in arr:
            if num==element:
                is_present=True
        return is_present
ls_instance=Linear_Search()
arr=[10,11,12,13,14,15]
element=int(input("enter element:"))
print(ls_instance.solution(arr,element))

           
    