num1=int(input("enter the number:"))

num2=int(input("enter the number:"))

operation=input("enter the operation:")

match operation:

    case "+":
        print(num1+num2)

    case "-":
        print( num1-num2)

    case "*":
        print( num1*num2)

    case "/":
        print( num1/num2)

    case "//":
        print(num1//num2)

    case "%":
        print(num1%num2)

    case "**":
        print(num1*num2) 

    case _:
        print("invalid")                          
