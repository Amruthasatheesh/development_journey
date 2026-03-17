#Write a function that takes two numbers and an operator (+, -, *, /) as parameters and returns the calculated result.

def cal(num1,num2,op="+"):
    if (op=="-"):
        return num1-num2
    elif (op=="*"):
        return num1*num2
    elif (op=="/"):
        return num1/num2
    elif (op=="+"):
        return num1+num2
print(cal(20,10,op="*")) 
print(cal(20,10,op="-"))
print(cal(20,10,op="/"))   
print(cal(20,10))   
