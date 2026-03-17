#Write a nested loop program that prints numbers 1 to 4 in 2 rows.

"""
1 2 3 4
1 2 3 4
"""

for r in range(1,3):

    for c in range(1,5):
        print(c,end="\t")
    print()