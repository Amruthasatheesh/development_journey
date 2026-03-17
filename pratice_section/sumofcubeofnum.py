num=int(input("enter the number:"))#123

sum=0
while(num!=0):#123!=0,!2!=0,1!=0,0==0(stop here)
    last_digit=num%10#123%10=3,12%10=2,1%10=1
    cube=last_digit**3#3^3=27,2^3=8,1^3=1
    sum=sum+cube#0+27=27,27+8=35,35+1=36
    num=num//10#123//10=12,12//10=1,1//10=0
print(sum)    




