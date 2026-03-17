#.Create a nested loop that prints numbers 1 to 2 inside an outer loop that runs 2 times.

"""
1 2
1 2
"""

for r in range(1,3):
    for c in range(1,3):
        print(c,end="\t")
    print()    