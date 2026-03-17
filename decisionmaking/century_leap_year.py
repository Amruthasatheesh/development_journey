# to check the year is leap year or not

# NB: some century year is not leap year so that condition is also checked here like"the century yr is leap yr checked and also non century yr is leap yr"

# that 2 conditions are checked here using if condition and or,and operations.

year=int(input("enter a year"))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
   print("leap year")

else:
   print("not a leap year")   