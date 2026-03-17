lst=[10,20,30,40,50,60]
index=int(input("enter the index"))
try:
    print(lst[index])

except Exception as e:
    index=int(input("enter the index"))
    print(lst[index])

finally:    # for clean process
    print("file operations...")
    print("database commit")