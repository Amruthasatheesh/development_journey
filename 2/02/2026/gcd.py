num1=int(input("enter number:"))#6
num2=int(input("enter number:"))#8

smallest=num1 if num1<num2 else num2
gcd=1

for i in range(1,smallest+1):#1,7
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)        #2