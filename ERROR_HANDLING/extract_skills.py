def extract_skills(sentance):
    result=""
    fr=open("ERROR_HANDLING\\skills.txt","r")
    skills_set=[line.rstrip("\n")for line in fr]
    skills_in_sentance=[w for w in sentance.split(" ")if w in skills_set]
    result=" ".join(skills_in_sentance)
    return result
sentance="Python is my favourite language"
sentance1="error handling functionas are almost similar in Java and Python"
print(extract_skills(sentance))
print(extract_skills(sentance1))
assert extract_skills(sentance)=="Python","test case 1 failed"
assert extract_skills(sentance1)=="Java Python","test case 2 failed"
print("code executed..")