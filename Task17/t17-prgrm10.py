#. Write a function that takes a number as a parameter and returns True if it is a prime number, otherwise returns False

def is_prime(n):
    
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            return is_prime
        else:
            is_prime=True
            return is_prime
print(is_prime(7))
print(is_prime(12))
    