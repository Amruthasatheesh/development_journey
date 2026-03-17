P=50000# loan amount

annual_interest=12# interest of year

R=annual_interest/(12*100)# rate of interest per month

N=24 #total no of monthly EMI

EMI_Amount= ( P*R*(1+R)**N ) / ((1+R)**N-1) # (50000*12(1+R)**1)

print("EMI Amount is:",EMI_Amount) #EMI_Amount is 2353.6736..