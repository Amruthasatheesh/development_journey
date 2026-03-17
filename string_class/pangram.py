#important pangram and anagram
#chk if all alphabets is present if true print pangram

word="the quick brown fox jumps over lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
for ch in alphabet:
    if ch not in word:
        is_pangram=False
        break
if is_pangram==True :
        print(is_pangram)   