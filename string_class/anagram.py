word1="silent"
word2="listen"
is_anagram=True
for ch in word1:
    if word2.find(ch)==-1:
        is_anagram=False
        break
if is_anagram==True:
    print(is_anagram)        

# another way of anagram programming
word1="silent"
word2="listen"
is_anagram=True
for ch in word1:
    if ch not in word2:
        is_anagram=False
if is_anagram==True:
    print(is_anagram)
