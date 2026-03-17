from csv import DictReader 
fr=open("Nested collection\\TASK27\\movie.csv","r")
data=list(DictReader(fr))
print(data)

