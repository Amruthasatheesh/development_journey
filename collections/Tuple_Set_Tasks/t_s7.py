#Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, write a program to find:
# * Common elements
# * All unique elements from both sets

seta={1,2,3,4}
setb={3,4,5,6}
intersect=seta.intersection(setb)
print(intersect)
diff_a=seta.difference(setb)
print(diff_a)
diff_b=setb.difference(seta)
print(diff_b)