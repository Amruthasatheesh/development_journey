#Write a program to create a new list containing squares of all elements.
numbers=[5,10,15,20,4]
squares=[]
for num in numbers:
    square=num**2
    squares.append(square)
print(squares)
