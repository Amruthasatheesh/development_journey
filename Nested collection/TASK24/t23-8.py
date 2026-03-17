# TASK 23 || List Slicing & List Comprehension || 25-02-2026

# 8. From a given list of numbers, create a new list containing only numbers greater than 50 using list comprehension.
lst=[10,20,30,50,55,68,70]

num_fifty=[num for num in lst if num>50]
print(num_fifty)