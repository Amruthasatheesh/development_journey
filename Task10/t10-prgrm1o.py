"""

 Write a program to find the sum of digits of a given number using a while loop.
"""
num=int(input("enter the num:"))#123
sum=0
while(num!=0):#123!=0,12!=0,1!=0,0==0(stop)
    last_digit=num%10#123%10=3,12%10=2,1%10=1.
    sum=sum+last_digit#0+3=3,3+2=5,5+1=6
    num=num//10#123//10=12,12//10=1,1//10=0
print(sum)    
