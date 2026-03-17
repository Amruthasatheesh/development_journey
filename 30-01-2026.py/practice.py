# string palindrome

text=input("enter string:")
text_copy=text
length=len(text) -1
rev=""
for ch in range(length,-1,-1):
    rev=rev+text[ch]
if text_copy==rev:
    print("palindrome")
else:
    print("not palindrome")
print(rev)  



          



    