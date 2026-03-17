db_couponcode="456"

user_couponcode=input("enter the code:")

if user_couponcode==db_couponcode:

    cart_amount=int(input("enter the cart amount:"))
    if cart_amount>=1000:
        print("coupon applied")

    else:
        print("minimum purchase not met")

else:
    print("invalid coupon")            

