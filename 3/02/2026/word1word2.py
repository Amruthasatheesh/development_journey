#word1=ABCDE

#word2=PQR

word1=input("enter string:")

word2=input("enter string:")

if len(word1) > len(word2):
    print(word1[len(word2):])
elif  len(word2) > len(word1):
    print(word2[len(word1):])    