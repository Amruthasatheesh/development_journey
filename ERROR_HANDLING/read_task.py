#read a password
# if length of paassword is < 6 create a custom error ie password invalid

passwrd=input("enter the password")
length=len(passwrd)
if length<6:
    raise Exception("password is invalid")
else:
    print("crct passwrd")