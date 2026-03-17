"""
prgrm for display the sum of cube of a number
#123 is 36 is sum of the cubes
"""



num=int(input("enter the number:"))
sum=0
while(num!=0):
    last_digit=num%10#123%10=3
    cube=last_digit**3#find the last digit cube, 3^3=9
    sum=sum+cube
    num=num//10# add the cube with sum
print(sum)    
    

