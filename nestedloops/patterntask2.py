"""
1 1 1 1
0 0 0 0
1 1 1 1
0 0 0 0 
"""
for r in range(1,5):
    for c in range(1,5):
        if r==1 or r==3 :
            print(1,end="\t")
        else:
            print(0,end="\t")
    print()            
        


"""
1 1 1 1
0 0 0 0
1 1 1 1
0 0 0 0 
"""        


for r in range(1,5):
    for c in range(1,5):
        if r==1 and r==3:
            print("1",end="\t")
    print()