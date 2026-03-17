oxygenlevel=int(input("enter the oxygen level:"))

if oxygenlevel>=95:
    print("normal")

elif oxygenlevel>=90 and oxygenlevel<=94:
    print("mild concern")

elif oxygenlevel<90:
    print("critical")    



