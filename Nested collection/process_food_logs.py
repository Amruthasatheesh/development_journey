fr=open("Nested collection\\food_logs.txt","r")
food_log=[]
for line in fr:
  
    #line="1,break_fast,idly,175,11-1-2025,hari"
    data=line.rstrip("\n").split(",")
    log={"id":data[0],"meal_type":data[1],"name":data[2],"calorie":data[3],"date":data[4],"owner":data[5]}
    food_log.append(log)
print(food_log)