"""
.divisibleby9_forloop
"""

num=int(input("enter number:"))

for i in range(1,num+1):# if num is 9 range is(1,10)
    if num%i==0:
        print(i)