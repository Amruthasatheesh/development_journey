#remove stopwords  
# def stop_words(sentance):
#     result=""

#     fr=open("ERROR_HANDLING\\stop_words.txt","r")
#     stop_words=[line.rstrip("\n")for line in fr]
#     cleaned_line=[w for w in sentance.split(" ")if w not in stop_words]
#     result=" ".join(cleaned_line)
#     return result
# sentance="Django is one of the python framework"
# sentance1="life is beautiful"
# print(stop_words)
# assert stop_words(sentance)=="Django one python framework","testcase 1 failed"
# assert stop_words(sentance1)=="life beautiful","test case 2 failed"
# print("code accepted")
#spam_words count in a message
def spam_words(message):
    count=0
    fr=open("ERROR_HANDLING\\spam_words.txt")
    spam_words=[line.rstrip("\n")for line in fr]
    spamwords_in_message=[w for w in message.split(" ")if w in message]
    count=len(spamwords_in_message)
    print(len(spamwords_in_message)/len(message))*100
    return count
print(spam_words(" win free cash"))



