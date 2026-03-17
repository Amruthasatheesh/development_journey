purchase_amount=int(input("enter the amount:"))

if purchase_amount>5000:
    print("20% discount")

elif purchase_amount>=2000 and purchase_amount<=5000:
    print("10% discount")

elif purchase_amount<2000:
    print("No discount")


