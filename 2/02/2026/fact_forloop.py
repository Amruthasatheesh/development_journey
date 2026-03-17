# num=int(input("enter the number:"))

# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f"factorial of {num} is  {fact}")    


# num=int(input("enter number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)
class Factorial:
    def solution(self,num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        return fact
fact_instance=Factorial()
num=int(input("enter number:"))
print("factorial is",fact_instance.solution(num))

