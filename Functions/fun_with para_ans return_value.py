def addition(num1,num2):
    result=num1+num2
    return result
print(addition(100,200)) 
# if there is return fun should use the print() when function calling time otherwise no need to use print fun just fun calling only
# ssub
def sub(n1,n2):
    result=n1-n2
    print(result)
print(sub(200,100))
# create fun smart_sub with n1,n2.....
def smart_sub(n1,n2):
    if n1>n2:
        result=n1-n2
        return result
    else:
        result=n2-n1
        return result
print(smart_sub(10,3))    
print(smart_sub(3,10))    