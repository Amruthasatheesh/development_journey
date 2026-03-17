db_password="password@123"

db_otp="2121"

user_password=input("enter the password:")

if db_password==user_password:
    user_otp=input("enter the otp")
    if db_otp==user_otp:
        print("login succesfull")
    else:
        print("wrong otp")
else:
    print("incorrect password")        






    