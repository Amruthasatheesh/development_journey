#to store the expense from jan to december
expense=[1000,1000,1200,2000,7500,4500,2000,1500,4000,3000,1200,11000]
total=0
for ex in expense:
    total=total+ex
print("totalexpense",total)
#find the avg=avg/total is calculated by avg/len(expense)
avg=total/len(expense)
print("average",avg)
