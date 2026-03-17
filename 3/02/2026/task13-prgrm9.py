#Write a program using match–case to perform addition, subtraction, multiplication, or division based on user choice.
num1=int(input("enter number:"))
num2=int(input("enter number:"))
operation=(input("enter ur choice:"))

match operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2) 
    case "*":
        print(num1*num2) 
    case "/":
        print(num1/num2)        
           
    
