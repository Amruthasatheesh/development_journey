manali={
    "dijo":300,
    "akshay":1000,
    "Edwin":800,
    "alan":15000,
    "manoj":0,
    "subin":0,
    "sreeyesh":500

}
total_expense=0
for v in manali.values():
    print(v)
    total_expense+=v
print(total_expense)
individual_expense=total_expense/len(manali)
print(individual_expense)
spend_wise={}
for k,v in manali.items():

    payment=individual_expense-v
    spend_wise[k]=payment
print(spend_wise)

 