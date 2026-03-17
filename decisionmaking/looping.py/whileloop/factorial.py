#print the factorial of a number 


num=int(input("enter the number:"))

i=1

result=1

while(i<=num):# after checking the condition it goes to the next part of result(to multiply the i value with already stored result value)
    result=result*i#(here)
    i=i+1#i incremented
print(num,"factorial is ",result)    #print the result in result var
