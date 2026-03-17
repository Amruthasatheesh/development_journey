"""
1  1  1  1
1  0  0  1
1  0  0  1
1  1  1  1
"""
# for r in range(1,5):
#     for c in range(1,5):
           
#         if r==1 or r==4 or  c==1 or c==4:
            
#             print(1,end="\t")
#         else:
            
#             print(0,end="\t")    
        
#     print()        

for r in range(1,5):
    for c in range(1,5):
        if r==1 or c==1 or r==4 or c==4:
            print("1",end="\t")
        else:
            print("0",end="\t")
    print()
    