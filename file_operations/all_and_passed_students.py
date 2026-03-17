fr_all_students=open("file_operations\\All_students.txt","r")
fr_passed_students=open("file_operations\\passed_students.txt","r")

all_students_list=[line.rstrip("\n")for line in fr_all_students]
passed_students_list=[line.rstrip("\n")for line in fr_passed_students]
print("all students",all_students_list)
print("passed students",passed_students_list)
failed_students=set(all_students_list).difference(passed_students_list)
print("failed students",failed_students)
