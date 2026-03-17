
rollnumber=501,502,503,504

student_Rollno=int(input("enter the rollnumber:"))
if student_Rollno in rollnumber:
    marks=int(input("enter the marks:"))
    if marks>=40:
        print("pass")
    else:
        print("fail")

else:
    print("invalid rollnumber")            
    


