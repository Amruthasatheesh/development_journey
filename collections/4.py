# Write a program to find the largest element in a list.
number=[10,12,14,20,35,22]
largest=0
for num in number:
    if num>largest:
        largest=num
print(largest)        