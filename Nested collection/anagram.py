#lst1=["listen","earth","moon","dad","madam","race"]
#lst2=["silent","angel","heart","test","dam","care"]
#anagram_words={"listen"}
words="racecarfast"
non_rec=[char for char in words if words.count(char)==1]
print(non_rec)
rec_char={char:words.count(char) for char in words if words.count(char)>=2}
print(rec_char)