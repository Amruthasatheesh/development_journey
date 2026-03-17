grade=input("enter the grade:")

match grade:

    case "A":
        print("Excellent")

    case "B":
        print("good")  

    case "C":
        print("average") 

    case "D":
        print("below average")    

    case "F":
        print("fail")

    case _:
        print("invalid")             