def odd_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

odd_even(9)
odd_even(8)
odd_even(12)
# prime number function definition:
def is_prime(num):
    is_prime="True"
    for i in range(2,num):
        if num%i==0:
            is_prime="False"
    print(is_prime)
is_prime(6)
is_prime(3)
# rev a string function definition and calling with parameters and no return values
def rev_string(word):
    rev=word[::-1]
    print(rev)
rev_string("hello")  
rev_string("java")     

