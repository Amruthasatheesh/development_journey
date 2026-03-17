num=int(input("enter the number:"))

sumeven=0
sumodd=0
i=1
while(i<=num):
    if i%2==0:
        sumeven=sumeven+i
    else:
        sumodd=sumodd+i
    i=i+1
print(sumeven)
print(sumodd)    