"""

Write a Python program to print each digit of a number separately using a while loop
"""

num=int(input("enter the num:"))

while(num!=0):
    last_digit=num%10
    print(last_digit)
    num=num//10
    