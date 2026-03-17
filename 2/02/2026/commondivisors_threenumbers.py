# num1=int(input("enter the number:"))
# num2=int(input("enter number:"))
# num3=int(input("enter number:"))

# if num1<num2 and num1<num3:
#     smallest=num1

# elif num2<num1 and num2<num3:
#     smallest=num2
# else:
#     smallest=num3   

# for i in range(1,smallest+1):
#     if num1%i==0 and num2%i==0 and num3%i==0:

#         print(i)





n1=int(input("enter the numbner:"))
n2=int(input("enter the numbner:"))
n3=int(input("enter the numbner:"))
smallest=0
gcd=1
if n1>n2 and n1>n3:
    smallest=n1
elif n2>n1 and n2>n3:
    smallest=n2
elif n3>n1 and n3>n2:
    smallest=n3
for i in range(1,smallest+1):
    if n1%i==0 and n2%i==0 and n3%i==0:
        gcd=i
print(gcd)

# #using class function:
# class Common_Divisor:
#     def common(self,n1,n2,n3):
#         smallest=0
#         if n1>n2 and n1>n3:
#             smallest=n1
#         elif n2>n1 and n2>n3:
#             smallest=n2
#         elif n3>n1 and n3>n2:
#             smallest=n3
#         for i in range(1,smallest+1):
#             if n1%i==0 and n2%i==0 and n3%i==0:
#                 print(i)
# obj=Common_Divisor()
# obj.common(10,11,12)            


 

