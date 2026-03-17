# word=input("enter string:")#madam index=01234

# word_length=len(word) -1

# result=""

# for i in range(word_length,-1,-1):
#     result=result+word[i]

# if result==word:
#     print("palindrome")
# else:
#     print("not palindrome")      


# word=input("enter the word:")
# word_copy=word
# result=" "
# reversed=word[::-1]
# result=reversed
# if word_copy==result:
#     print("string palindrome")
# else:
#     print("not string palindrome")
# print(result)

class Palindrome:
    def palindrom(self,word):
        result=" "
        reversed=word[::-1]
        result=reversed
        if word==result:
            print("palindrome")
        else:
            print("not palindrome")
        return result
pal_instance=Palindrome()
word=input("Enter the word:")
print(pal_instance.palindrom(word))

          

        