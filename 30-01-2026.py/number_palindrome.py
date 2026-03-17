"""
w.a.p to check the given number is palindrome or not
"""
# number=int(input("enter the number:"))#121

# result=0
# number_copy=number
# while(number!=0):#121!=0
#     digit=number%10#121%10=1,12%10=2,1%10=0.
#     result=result*10+digit#0*10+1=1,1*10+2=12,12*10+1=121
#     number=number//10
# if number_copy==result:
#     print("palindrome")
# else:
#     print("not palindrome")        



# num=int(input("enter number:"))
# result=0
# num_copy=num
# while(num!=0):
#     last_digit=num%10
#     result=result*10+last_digit#123=3=
#     num=num//10
# print(result)
# if num_copy==result:
#     print("palindrome")
# else:
#     print("not palindrome")


#using function
def palindrome(num):
    num_copy=num
    result=0
    while(num!=0):
        digit=num%10
        result=result*10+digit
        num=num//10
    if num_copy==result:
       
       print("palindrome")
    else:
      print("not palindrome")
    return result
num=int(input("enter number:"))
print(palindrome(num))

#using class function

