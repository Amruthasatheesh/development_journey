char=input("enter the character:")

asci_value=ord(char)

if asci_value in range(97,123) or  asci_value in range(65,91):

    print("alphabet")

else:
    print("not alphabet")    