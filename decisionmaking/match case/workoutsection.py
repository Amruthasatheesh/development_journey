db_pin="1234"

db_balance=5000

user_pin=int(input("enter the pin:"))

if db_pin==user_pin:

    amount=int(input("enter the amount:"))

    if amount<=db_balance:
        print("withdrawal successfull")

    else:
        print("insufficient balance")

else:
    print("incorrect pin")            


