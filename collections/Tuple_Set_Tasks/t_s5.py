#Write a program to find the maximum and minimum value in a tuple.
numbers=(5,10,15,20)
max_value=numbers[0]
min_value=numbers[0]
for num in numbers:
    if num>max_value:
        max_value=num
        
    if num<min_value:
        min_value=num 
print(f"maximum value is {max_value}")
print(f"minimum value is {min_value}")