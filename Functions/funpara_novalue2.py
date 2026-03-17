def subtraction(num1,num2):
    result=num1-num2
    print(f"subtraction result is {result}")
subtraction(200,100)

# function to create a cube of number

def cube(num):
    result=num**3
    print(f"cube of a number is {result}")
cube(3)    
cube(5)    
# create function max_two with two parameter num1,num2
# display largest number

def max_two(num1,num2):
    if num1>num2:
        print(num1)
    else:
        print(num2)    
max_two(3,5)
max_two(200,140)

#create a fun last_digit_max with two parameter num1,num2
#display num1 if last_digit of num1 > last_digit of num2
#vice versa

def last_digit_max(num1,num2):
    last_digit_num1=num1%10
    last_digit_num2=num2%10
    if last_digit_num1>last_digit_num2:
        print(num1)
    else:
        print(num2)
last_digit_max(123,98)