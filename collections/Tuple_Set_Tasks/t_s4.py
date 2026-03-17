#Given a tuple (1, 2, 3, 4, 5), convert it into a list, add a new element, and convert it back to a tuple.
tup=(1,2,3,4,5)
res=list(tup)
res.insert(1,10)
tu=tuple(res)
print(tu)
