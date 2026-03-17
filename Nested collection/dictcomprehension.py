#cretae a dictionary of output as{10:2,11:2,12:1,13:2}
lst=(10,11,12,11,10,13,13)
num_count={n:lst.count(n) for n in lst}
print(num_count)

word="racecar"
#dispaly character count
char_count={w:word.count(w) for w in word}
print(char_count)