# number=int(input("enter number:"))#7

# is_prime=True

# for i in range(2,number):
#     if number%i==0:
#         is_prime=False
#         break
# print(is_prime)        

#prime no
# num=int(input("enter the number"))
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#       is_prime=False
#       break
# print(is_prime)

def prime_number(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    return is_prime
n=int(input("enter the number:"))
print(prime_number(n))
    
# class
class Primenumber:
    def prime(n):
        is_prime=True
        for i in range(2,n):
          if n%i==0:
            is_prime=False
            break
        return is_prime
n=int(input("enter the number:"))
obj=Primenumber()
print(obj.prime(n))
