fasting_bloodsugar=int(input("enter the sugarlevel"))

if fasting_bloodsugar<100:
    print("normal")

elif fasting_bloodsugar<125:
    print("prediabetics")

else:
    print("diabets")        