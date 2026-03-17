#9. Write a program to append new content to an existing file without deleting old data.
karate_lst=["varun","mini","beena"]
fa=open("Task25\\9_karate_students.txt","a")
for k in karate_lst:
    fa.write(k + "\n")
print("karate students list..")