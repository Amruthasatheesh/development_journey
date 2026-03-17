from csv import DictReader
fr=open("Nested collection\\tips.csv")
Data=list(DictReader(fr))
print(Data)

#day_wise_summary={sun:345,mon:345}
day_wise_summary={}
for d in Data:
    tip=float(d.get("tip"))
    day=d.get("day")
    if day in day_wise_summary:
        day_wise_summary[day]+=tip
    else:
        day_wise_summary[day]=tip
print(day_wise_summary)
#day_with_highest_revenue



day_highest_revenue={}
for d in Data:
    total_bill=float(d.get("total_bill"))
    day=d.get("day")
    if day in day_highest_revenue:
        day_highest_revenue[day]+=total_bill
    else:
        day_highest_revenue[day]=total_bill
print(day_highest_revenue)

#which male or female customers is giving more tip
#{male:123,female:456}

more_tip={}
for d in Data:
    sex=d.get("sex")
    tip=float(d.get("tip"))
    if sex in more_tip:
       more_tip[sex]+=tip
    else:
       more_tip[sex]=tip
print("more_tip_in male_or_female",more_tip)#more_tip_in male_or_female {'Female': 246.51, 'Male': 485.0700000000001}





