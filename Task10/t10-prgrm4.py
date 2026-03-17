"""
4. Write a program to calculate the sum of even numbers between 1 and 100 using a while loop.



"""
num=int(input("enter the number:"))#100

i=1
sum_even=0
while(i<=num):#1<=100
    if i%2==0:#1%2!=0,2%2==0......100
        sum_even=sum_even+i#0+1=1...
    i=i+1#1+1=2,...
print(sum_even)   #    2550 
