# print/display numbers from 1 to 100
# range(start,stop,step) # 
#display the numbers from 1 to 10 which is divisible by 9

number=int(input("enter the number:"))


for i in range(1,number+1):
    if number%i==0:
        print(i)


      
