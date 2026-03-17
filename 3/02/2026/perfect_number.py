# num=int(input("enter number:"))#6 except that number take from 1 to upto 5

# sum=0


# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# print("perfect number" if num==sum else "not perfect number")        

# num=int(input("enter the number:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# print("sum is",sum)
# if num==sum:
#     print("perfect number")
# else:
#     print("not perfect number")

def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
         sum=sum+i
    if num==sum:
      print("perfect number")
    else:
      print("not a perfect number")
    return sum
num=int(input("enter the number:"))

print(perfect_number(num))


