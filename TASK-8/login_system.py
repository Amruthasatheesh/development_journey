db_username="amru"

db_password="amru@123"

username=input("enter the username:")

user_password=(input("enter the password:"))

if username==db_username and db_password==user_password:
    print("login successful")

else:
    print("invalid credentials")    


