#attendance storage from sunday to monday as H,p,o,
attendance=["H","p","p","p","p","p","H","H","P"]
#print(attendance)
# to update the value of 5th index p in to h
#attendance[5]="H"
#print(attendance)
#print one by one
for at in attendance:
    print(at)
#to count the holiday_count,present_count
attendance=["H","p","p","p","p","p","H","H","P"]
holiday_count=0
present_count=0
for att in attendance:
    if att=="H":
        holiday_count+=1
    elif att=="p":
        present_count+=1
print("holidayaccount",holiday_count)
print("presentcount",present_count)            