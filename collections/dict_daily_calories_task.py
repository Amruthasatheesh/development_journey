#daily calories
daily_calories={
    "sun":1200,
    "mon":2000,
    "tue":3000,
    "wed":1500,
    "thu":2300,
    "fri":1300,
    "sat":1250
}

for key in daily_calories:
    print(key,daily_calories[key])
# to find the total calories
total_calories=0
for key in daily_calories:
    cal=daily_calories[key]
    total_calories+=cal
print(total_calories)
avg_calories=total_calories/len(daily_calories)
print(avg_calories)
