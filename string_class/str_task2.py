#w.a.p to display digits in text
text="ihave2pen1pencilonecar"
for ch in text:
    if ch.isdigit():
        print(ch)

# w.a.p to display alphabet_count,digit_count,special_character_count

word="aman##aplan**panamawith2car1bike"
alpha_count=0
digit_count=0
spcl_chr_count=0
for ch in word:
    if ch.isalpha():
        alpha_count+=1
    if ch.isdigit():
        digit_count+=1
    if not ch.isalnum():
        spcl_chr_count+=1
print(f"alphabet_count is {alpha_count}")
print(f"digit_count is {digit_count}")
print(f"spcial_character_count is {spcl_chr_count}")
