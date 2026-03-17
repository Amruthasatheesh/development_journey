w_in_kg=int(input("enter the weight in kilogram:"))

h_in_cm=int(input("enter the height  centimeter:"))

h_in_m=h_in_cm/100

bmi=(w_in_kg/h_in_m**2)

bmi=round(bmi)
print(bmi)

if bmi<20:
    print("underweight")

elif bmi<25:
    print("normal")

elif bmi<30:
    print("overweight") 

else:
    print("obese")          
