#Write a program to find the smallest element in a list.
number=[10,12,14,20,35,22]
smallest=number[0]
for num in number:
    if num<smallest:
        smallest=num
print(smallest)        