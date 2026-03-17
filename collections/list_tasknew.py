# display the duplicate values

numbers=[10,10,20,30,10,40,50,60,50,30,10]
st=set()                  # here set is used bcos duplicates values are not allowed in set
for num in numbers:
    num_count=numbers.count(num)
    if num_count>1:
        st.add(num)
print(st)        

#another way of :
numbers=[10,10,20,30,10,40,50,60,50,30,10]
st={num for num in numbers if numbers.count(num)>1}
print(st)
