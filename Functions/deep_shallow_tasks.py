#Task 31 || Shallow Copy & Deep Copy || 17-03-2026

1.# Write a Python program to create a list and make a shallow copy of it using the copy() method.
# neenu_fvt_color=["green","purple","black"]

# appu_fvt_color=(neenu_fvt_color).copy()
# print("neenu's color",neenu_fvt_color)
# print("appu's color",appu_fvt_color)

#2 Write a program to demonstrate shallow copy using the copy module.
# neenu_fvt_color=["green","purple","black"]

# appu_fvt_color=(neenu_fvt_color).copy()
# neenu_fvt_color[1]="navyblue"
# print("neenu's color",neenu_fvt_color)
# print("appu's color",appu_fvt_color)
#3Create a list containing nested lists. Perform a shallow copy and modify the inner list. Print both lists and observe the result.
# arun_fvt_foods=[
#     ["dosa","fried rice","masala dosa","ghee roast","maggi"
#      "meals","aapam","noolputtu"]
#     ]
# kavya_fvt_food=arun_fvt_foods.copy()
# arun_fvt_foods[0][1]="poori masala"
# print(arun_fvt_foods)
# print(kavya_fvt_food)
#4. Write a Python program to perform deep copy using the deepcopy() function from the copy module.
# from copy import deepcopy
# arun_fvt_foods=[
#     {"mealtype":"breakfast","meal":"dosa"},
#     {"mealtype":"lunch","meal":"fish meal"},
#     {"mealtype":"dinner","meal":"friedrice"},
# ]
# sravan_fvt_food=deepcopy (arun_fvt_foods)
# print(arun_fvt_foods)
# print(sravan_fvt_food)
#5 Create a nested list and perform deep copy. Modify the inner list and show that the original list remains unchanged.
# from copy import deepcopy
# lst = [["apple", "banana"], ["cat", "dog"], ["red", "blue"]]
# lst2=deepcopy (lst)
# lst2[1][0]="lion"
# print(lst)
# print(lst2)
# #6Write a program to compare shallow copy and deep copy using nested lists.
# lst = [["apple", "banana"], ["cat", "dog"], ["red", "blue"]]
# lst2=lst.copy()
# print(lst)
# from copy import deepcopy
# print(lst2)
# lst = [["apple", "banana"], ["cat", "dog"], ["red", "blue"]]
# lst2=deepcopy (lst)
# print(lst)
# print(lst2)
#7Create a dictionary containing a list as a value. Perform shallow copy and modify the list. Print both dictionaries.
# data = {
#     "fruits": ["apple", "banana", "mango"],
#     "colors": ["red", "blue", "green"],
#     "animals": ["dog", "cat", "cow"]
# }

# data2=data.copy()
# print("data is",data)
# print("data 2 is",data2)

# data3=data["fruits"]=["cherry","banana","mango"]
# print("data 3 is",data3)

#8 Write a Python program that uses deepcopy() to copy a dictionary with nested data.
# from copy import deepcopy
# students = {
#     "class": [
#         {"name": "Anu", "marks": 80},
#         {"name": "Ravi", "marks": 90}
#     ]
# }
# student2=deepcopy (students)
# print(students)
# print(student2)
#9 Create a list of lists and perform shallow copy using slicing. Modify an element and observe the effect
# lst = [[1, 2], [3, 4], [5, 6]]
# lst2=lst[:2].copy()
# lst[0][1]=8
# print(lst)
#10 Write a program to check the memory address of original list and copied list using id().

# from copy import deepcopy
# arun_fvt_foods=[
#     {"mealtype":"breakfast","meal":"dosa"},
#     {"mealtype":"lunch","meal":"fish meal"},
#     {"mealtype":"dinner","meal":"friedrice"},
# ]
# hari_fvt_foods=deepcopy (arun_fvt_foods)
# hari_fvt_foods[0]["meal"]="idly"

# print(arun_fvt_foods is hari_fvt_foods)
# #11 Create a class object and perform shallow copy of the object using the copy module.
# import copy

# class Car:
#     def __init__(self, name):
#         self.name = name
# c1 = Car("BMW")
# c2 = copy.copy(c1)

# print("Original:", c1.name)
# print("Copy:", c2.name)
# #12Create a program that demonstrates shallow copy using the assignment operator (=) and explain the output.

# arun_fvt_foods=["idly","dosa","poorimasala"]
   
# hari_fvt_foods=arun_fvt_foods.copy

# print(hari_fvt_foods==arun_fvt_foods)

# #14 Write a program where a nested dictionary is copied using deepcopy() and modified without affecting the original dictionary.
# from copy import deepcopy
# words = {
#     "fruits": {
#         "apple": "red",
#         "banana": "yellow"
#     },
#     "animals": {
#         "dog": "barks",
#         "cat": "meows"
#     }
# }
# words2=deepcopy (words)
# words2["fruits"]["apple"]="green"
# print("original list",words)
# print("modified list",words2)
# #15 Write a Python program to demonstrate the difference between shallow copy and deep copy with a practical example.

from copy import deepcopy
arun_fvt_foods=[
    {"mealtype":"breakfast","meal":"dosa"},
    {"mealtype":"lunch","meal":"fish meal"},
    {"mealtype":"dinner","meal":"friedrice"},
]
hari_fvt_foods=deepcopy (arun_fvt_foods)
hari_fvt_foods[0]["meal"]="idly"

print(arun_fvt_foods)
print(hari_fvt_foods)
#shallow copy


arun_fvt_foods=[
    {"mealtype":"breakfast","meal":"dosa"},
    {"mealtype":"lunch","meal":"fish meal"},
    {"mealtype":"dinner","meal":"friedrice"},
]
hari_fvt_foods= (arun_fvt_foods).copy


print(arun_fvt_foods)
print(hari_fvt_foods)


