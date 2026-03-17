#Reverse a string using a for loop.
char=input("enter a character:")
rev=" "

for ch in char:
    rev=ch+rev
print(rev)