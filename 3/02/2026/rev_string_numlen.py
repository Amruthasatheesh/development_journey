word=input("enter string:")#java

word_length=len(word) -1# 4-1=3(bcos indexing strts from 0)    actually the length strts from 1 to..n that is java length is 1234=4
result=""

for i  in range(word_length,-1,-1):#(3,-1,-1)
    result=result+word[i]#word+ ith index

print(result)    #avaj