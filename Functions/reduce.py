from functools import reduce
arr=[10,12,14,11,15]
result_reduce=lambda n1,n2:n1*n2
res=reduce(result_reduce,arr)
print(res)