hours_sleep=int(input("enter the hours of sleep:"))

if hours_sleep<6:
    print("sleep deprived")

elif hours_sleep>=6 and hours_sleep<=8:
    print("healthy sleep")    

elif hours_sleep>8:
    print("oversleeping")    