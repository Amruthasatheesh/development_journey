prev=0 #previous print 0
curr=1# current prints 1 here
print(prev,curr)
for i in range(1,16):
    next=prev+curr
    print(next)
    prev=curr
    curr=next # prints up to 17 numbers including the ist 0 and 1 