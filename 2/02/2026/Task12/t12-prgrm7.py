#Count the number of vowels in a given string using a for loop.
word="rose"
count=0
vowels="a,e,i,o,u"
for ch in word:
    if ch in vowels:
        count=count+1
print(count)
