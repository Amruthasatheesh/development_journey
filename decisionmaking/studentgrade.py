m1=int(input("enter the marks:"))
m2=int(input("enter the marks:"))
m3=int(input("enter the marks:"))

total=m1+m2+m3


if total>140:
    print("A")

elif  total>130 and total<=140:
    print("B")

elif total>120 and total<=130:
    print("C")       

else:
    print("fail")    

percentage=2
gracemark_total=(percentage/100*total)+total

print(gracemark_total)