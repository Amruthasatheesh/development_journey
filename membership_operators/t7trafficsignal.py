signal=input("enter the signal color:")

match signal:

    case "red": # string/characters should be in " "
        print("stop")

    case "green":
        print("go")

    case "yellow":
        print("wait")

    case _:
        print("invalid")            
