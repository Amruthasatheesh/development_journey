
# count vowels in a string
# text=input("enter the string:")
# count=0
# vowels="a,e,i,o,u"
# for ch in text:
#     if ch.lower() in vowels:
#         count+=1
# print(count)
#print consonants in a string
text=input("enter string:")
vowels="a,e,i,o,u"
count=0
for ch in text:
    if ch not in vowels:
     count+=1
print(count)    

