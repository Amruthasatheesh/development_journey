#isalpha() only when str contains alphabets
# word="hello"

# print(word.isalpha())
# #isdigit()
# text="123"
# print(text.isdigit())

#isalnum
text="hello123"
print(text.isalnum())
text="hello123$"
print(text.isalnum())

# ##startswith()
text="luminar technolab"
print(text.startswith("lu"))
print(text.startswith("Lu"))

# #endswith()
# text="luminar technolab"
# print(text.endswith("lab"))
# print(text.endswith("labs"))
# #strip()
# """
# def strip(self)=> remove the bothsides space
# """
# text="luminar technolab"
# print(f"left{text.strip()}right")# without any space "left" and "right" is added at the both sides of the text "luminar technolab.

# text="\nluminar technolab"
# print(text.strip())
# #lstrip()=> remove the space from left side
# #rstrip()=>remove the right side space
# text="\nluminar technolab\t"
# print(text.lstrip("\n"))
# print(text.rstrip("\t"))

# text="hello world Python"
# result="" 
# for ch in text:
#     if ch !="":
#         result+=ch
# print(result)        

# text="python"
# vowels="a","e","i","o","u"
# count=0
# for ch in text:
#     if ch in vowels:
#         count+=1
# print(count)
#check the string is palindrome
word=input("enter the word:")
reverse=0
word_copy=word
reverse=word[::-1]
is_palindrome=True
if word_copy==reverse:
    print("palindrome")
else:
    is_palindrome=False
    print("not palindrome")    