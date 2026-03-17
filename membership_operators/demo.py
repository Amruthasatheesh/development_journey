# num=int(input("enter number:"))
# i=1
# fact=1
# while(i<=num):
#     fact=fact*i
#     i=i+1
# print(fact)   


fact=1
num=int(input("enter the number:"))
for i in range(1,num+1):
    fact=fact*i
print(fact)