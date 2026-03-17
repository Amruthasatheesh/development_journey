
#6. Write a Python program to create a file and write 5 lines of text into it.
movies=["ABCD2","yaariyan","lootera","love aaj kal"]
fw=open("Task25\movies.txt","w")
for m in movies:
    fw.write(m+"\n")
print("movies list....")

