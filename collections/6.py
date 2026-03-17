# Write a program to count how many even numbers are present in a list.
list=[2,3,4,6,7,8,9,10]
count=0
for lst in list:
    if lst%2==0:
        count+=1
print(count)