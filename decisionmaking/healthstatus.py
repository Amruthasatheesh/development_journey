bp=int(input("enter the systolic bp:"))

if bp<120:
    print("Normal")

elif bp<=129:
    print("elevated") 

elif bp<=139:
    print("high bp stage1")

elif bp>=140:
    print("high bp stage2")       