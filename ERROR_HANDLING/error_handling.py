"""
error handling
try:
     doubtful code
except:
     handling code

"""

lst=[12,13,14,15]

index=int(input("enter the index position"))

try:
    print(lst[index])
except Exception as e:
    print(e)# this shows what type of error is occured here
print("database commit")
print("file write")#enter the index position8
#output
# list index out of range
# database commit
# file write

