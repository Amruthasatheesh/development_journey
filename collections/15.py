#Write a program to check whether a list is a palindrome.

list=["m","o","m"]
is_palindrome=True
new_list=list[::-1]
if list==new_list:
    print(is_palindrome)
else:
    is_palindrome=False
    print(is_palindrome)

