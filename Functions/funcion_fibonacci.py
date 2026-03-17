#check 9 is fibonacci number ,if its true returns True,else False
# def is_fibonacci_number(number):
#     is_fibo=False
#     prev=0
#     curr=1
#     next=prev+curr
#     while(next<=number):
#         next=prev+curr
#         prev=curr
#         curr=next
#         if next==number:
#             is_fibo=True
#             break
#     return is_fibo
# print(is_fibonacci_number(9))
# print(is_fibonacci_number(2))
# print(is_fibonacci_number(5))
         
            
            
            
# num=int(input("enter number:"))   
# is_fibo=False    
# prev=0
# current=1
# next=prev+current
# while(next<=num):
#     next=current+prev
#     prev=current
#     current=next
#     if next==num:
#       is_fibo=True
# print(is_fibo)


class Fibonnaci:
   def solution(self,num):
      prev=0
      current=1
      next=prev+current
      is_fibo=False
      while(next<=num):
         next=prev+current
         prev=current
         current=next
         if next==num:
            is_fibo=True
      return is_fibo
fibo_instance=Fibonnaci()
num=int(input("enter the number:"))
print(fibo_instance.solution(num))

    