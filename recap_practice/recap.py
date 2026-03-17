x = 5
y = 10
temp=0
#swap  the elements
temp=x
x=y
y=temp
print("x is",x)
print("y is",y)
#Store length and width of a rectangle. Find and print the area.
l=10
w=5
area=l*w
print("area of an rectangle is",area)
# Store a number and check:

# Even or Odd

# Store marks of 3 subjects. Find the average.

num=10
if num%2==0:
    print("even")
else:
    print("odd")

sub1=30
sub2=35
sub3=40


avg=(sub1+sub2+sub3)/3
print(avg)
# Store a number and print:

# Its cube

# Its half

num=10
cube=num**3
half=num/2
print(cube)
print(half)

#tore a number in a variable num
# 👉 Check and print:

# If number is positive

# If number is negative

# If number is zero
num=25
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#Store two numbers and print the largest
# a = 10
# b = 20
# Output: 20 is larger
a = 10
b = 20
if a>b:
    largest=a
else:
    largest=b
print("largest of two numbers is",largest)
#
#largwst among three numbers
a=10
b=15
c=35
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print("largest among three numbers is",c)
#palindrome
def is_palindrome(num):
   

    result=0
    num_copy=num
    while(num!=0):

       digit=num%10
       result=result*10+digit
       num=num//10
    if num_copy==result:
       result=True
    else:
        result=False
    return result
print(is_palindrome(121))
print(is_palindrome(123))
print(is_palindrome(7))
print(is_palindrome(1001))

"""
assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(7) == True
assert is_palindrome(1001) == True
"""