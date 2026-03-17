employees=["hari","dixon","Amal","raju","veera"]
fw=open("file_operations\\write_employees.txt","w")
for e in employees:
    fw.write(e+"\n")
print("completed......")