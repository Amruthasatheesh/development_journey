


num=int(input("enter number"))
for i in range(1,num+1):
    if num%i==0:
        print(i)

#using function
# def common_divisor(num):
#     result=0
#     for i in range(1,num+1):
#         if num%i==0:
#             print(i)
# common_divisor(12)

# common_divisor(10)

# common_divisor(6)

#class function in common divisor
class CommonDivisor:
    def solution(self,num):
        for i in range(1,num+1):
            if num%i==0:
                print(i)
    
common_instance=CommonDivisor()
common_instance.solution(12)



                   