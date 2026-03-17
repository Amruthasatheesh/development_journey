# Write a program using match–case to display the day name when the user enters a number (1–7).

day=int(input("enter day:"))

match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("friday")
    case 7:    
        print("saturday")
    case _:
        print("invalid")