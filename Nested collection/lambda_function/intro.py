"""
Anonymous function with single expression
lambda p1,p2:expression

"""

add_num=lambda n1,n2:n1+n2
print(add_num(10,12))

sub_num=lambda n1,n2:n1-n2
print(sub_num(10,5))

cube_num=lambda num:num**3
print(cube_num(2))
#odd or even
odd_even_num=lambda num:"even" if num%2==0 else "odd"
print(odd_even_num(20))
#create a lambda function is_positive return true if num is positive else return false
is_positive=lambda num:True if num>0 else False
print(is_positive(45))
print(is_positive(-12))