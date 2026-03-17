#Create a dictionary to store a student's details:
# id
# name
# course
# marks
# Tasks:
# Print the student name
# Update marks by adding 5 bonus marks
# Add a new key grade
# Check if attendance key exists

student_details={"id":10,"name":"anu","course":"computer science","marks":85}
student_details["name"]
student_details["marks"]+=5
student_details["grade"]="A"

print(student_details)
if "attendance" in student_details:
    print("yes")
else:
    print("no")    