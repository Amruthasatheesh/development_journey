# num=int(input("enter the number:"))
# num_copy=num

# result=0

# number_length=len(str(num))

# while(num!=0):
#     digit=num%10
#     expo=digit**number_length
#     result=result+expo
#     num=num//10
# if num_copy==result:
#     print("armstrong")
# else:
#     print("not armstrong")    
# print(result)    



def armstrong(num):
   
   num_copy=num
   num_length=len(str(num))
   result=0
   while(num!=0):

    last_digit=num%10
    expo=last_digit**num_length
    result=result+expo
    num=num//10
   if num_copy==result:
       print("armstrong")
   else:
      print("not armstrong")
   return result
num=int(input("enter the number:"))
print(armstrong(num))
 
