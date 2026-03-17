#w.a.p to display all leap yrs from 1800 to 2026

i=1800
while(i<=2026):

    if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):

        print(i,"leap year")


    i=i+1