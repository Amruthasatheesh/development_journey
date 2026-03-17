prompt=input("enter the prompt:")

match prompt:

    case "start":
        print("system starting")

    case "stop":
        print("system stopping")

    case "restart":
        print("system restarting")

    case _:
        print("invalid")            