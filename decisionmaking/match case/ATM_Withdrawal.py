db_pin=1020

db_balance=1000

user_pin=int(input("enter the pin:"))

if db_pin==user_pin:

    user_amount=int(input("enter the withdrwal amount:"))
    if user_amount<=db_balance:
        print("withdrwal success")
    else:
        print("insufficient balance")

else:
    print("incorrect pin")        


    

