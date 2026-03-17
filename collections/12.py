#Write a program to print elements present at even index positions.
numbers=[10,20,25,17,19]
even_index=[]
for num in numbers:
    if num%2==0:
        even_index.index(num)
print(even_index)