# Restaurant Order System
# ------------------------------------
# Task:
# - Ask for table number

# If table exists:
#     - Ask for food availability
#     - If food available:
#         "Order placed"
#     - Else:
#         "Item out of stock"
# Else:
#     "Invalid table number"

table_no=[10,11,12,13,14]
food_available="dosa","idli","biriyani","fried rice"
table_number=int(input("enter the table no:"))
if table_number in table_no:
    food=input("enter the food")
    if food_available in food:
        print("order placed")
    else:
        print("item out of stock ")
else:
    print("invalid table number")


                  

table_number=5,6,7,8

db_food=("biriyani,meals,chappathiandcurry,fried rice")

user_tablenumber=int(input("enter the table number:"))

if user_tablenumber in table_number:
    food=input("enter the food:")
    if food in db_food:
        print("order placed")
    else:
        print("item out of stock")
else:
    print("invalid table number")                    

