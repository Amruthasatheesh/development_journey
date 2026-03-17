#food_logs,list creation
food_logs=["coffee","idli","rice","dosa",]
print(food_logs)
#update the food dosa with appam,bcos list is mutable
food_logs[3]="Appam"
print(food_logs)
#display the value of 2
print(food_logs[2])

#to print the food_logs in one by one ,using for loop
for i in range(0,4):
    print(food_logs[i])
#instead of i use f for indexing ,no need to mention the range or index:
for f in food_logs:
    print(f)    
