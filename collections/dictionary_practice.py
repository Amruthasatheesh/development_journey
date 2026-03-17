#Create a dictionary:
# account_number
# holder_name
# balance
# Tasks:
# Deposit 5000
# Withdraw 2000
# Check if balance is less than 1000 → print "Low Balance"
# account={"acc_number":101,"holder_name":"anu","balance":1000}
# account["balance"]+=5000
# if account["balance"]>2000:
#     account["balance"]-=2000
# else:
#     print("insufficient balance")
# if account["balance"]<1000:
#     print("low balance")
# print(account)
#task: daily_calories
# daily_calories={
#     "sun":1200,
#     "mon":2000,
#     "tue":3000,
#     "wed":1500,
#     "thu":2300,
#     "fri":1300,
#     "sat":1250
# }
# #one by one printing
# for k in daily_calories:
#     print(k,daily_calories[k])
#     #total_calories find
# total_calories=0
# for k in daily_calories:
#     cal=daily_calories[k]
#     total_calories+=cal
# print("total calories",total_calories)
# # to get the avg 
# avg=0
# avg=total_calories/len(daily_calories)
# print(avg)
sales_report={
    "sun":23000,
    "mon":16000,
    "tue":18000,
    "wed":15000,
    "thu":19000,
    "fri":19000,
    "sat":20000
}
#display day_wise values
# total_sale
# display avg_value
# display day where sales<avg_sales
# for k in sales_report:
#     print(k,sales_report[k])
# total=0
# for k in sales_report:
#     sales=sales_report[k]
#     total+=sales
# print(total)
# avg=0
# avg=total/len(sales_report)
# print(avg)
# for k in sales_report:
#     values=sales_report[k]
#     if values<avg:
#         print(k)

manali={
    "dijo":300,
    "akshay":1000,
    "Edwin":800,
    "alan":15000,
    "manoj":0,
    "subin":0,
    "sreeyesh":500

}

# find the total expense,individual_expense/split,spend wise
total_expense=0
for  v in manali.values():
    print(v)
    total_expense+=v
print("total",total_expense)
individual_expense=0
individual_expense=total_expense/len(manali)
print("indi expense is",individual_expense)
spend_wise={}
for k,v in manali.items():
    payment=individual_expense-v
    spend_wise[k]=payment
print(spend_wise)
#w.a.p to display missing least positive number in a llist
lst=[1,2,3,4,5]
length=len(lst)
for i in range(1,length+1):
    if i not in lst:
        print(i)
        break
else:
    print(length+1,"is missing")
