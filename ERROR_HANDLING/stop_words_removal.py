def remove_stop_words(sentence):
    result=""
   
    fr=open("ERROR_HANDLING\\stop_words.txt","r")
    stop_words=[line.rstrip("\n")for line in fr]
    cleaned_word=[w for w in sentence.split(" ")if w not in stop_words]
    result=" ".join(cleaned_word)
    return result

sentence2="machine learning is subset of AI"
sentence3="django is one of python framework"
print(remove_stop_words)
assert remove_stop_words(sentence2)=="machine learning subset AI","testcase 1 failed"
assert remove_stop_words(sentence3)=="django one python framework","testcase 1 failed"
print("code Accepted")