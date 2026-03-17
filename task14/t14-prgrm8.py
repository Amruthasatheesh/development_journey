#Using nested loops, print the sum of two numbers where the first loop runs from 1 to 2 and the second loop runs from 1 to 3.

for r in range(1,3):
    for c in range(1,4):
        sum=r+c
        print(sum,end="\t")
    print()    