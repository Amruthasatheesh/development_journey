"""
number=2345
last_digit=num%10
display last_digit
floor=num/10

"""




num=int(input("enter the number:"))

while(num!=0):
    last_digit=num%10
    print(last_digit)
    num=num//10
   