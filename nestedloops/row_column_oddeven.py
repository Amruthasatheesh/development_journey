# for r in range(1,5):
#     for c in range(1,5):
#         if (r+c)%2==0:
#             print("O",end="\t")
#         else:
#             print("E",end="\t")
#     print()            





# for r in range(1,5):
#     for c in range(1,5):
#         print("*",end="\t")
#     print()



# for r in range(1,7):
#     for s in range(1-r):
#         print(" ",end="")
#     for c in range(1,6-r+2):
#         print("* ",end="")
#     print()

for r in range(7,0,-1):
    for s in range(1,r):
        print("",end="")
    for c in range(1,6-r+2):
        print(c,end=" ")
    print()