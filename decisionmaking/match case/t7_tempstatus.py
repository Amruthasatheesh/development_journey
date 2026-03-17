temp_status=int(input("enter the temperature status:"))

if temp_status<20:
    print("cold")

elif temp_status<=30:
    print("Normal")

else:
    print("hot")