#Write a function that takes a number as a parameter and returns the factorial of that number.

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(6))  
print(factorial(5))  

