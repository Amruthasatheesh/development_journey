def count_evens(*args):
    ecount=0
    for i in args:
        if i%2==0:
            ecount+=1
    return ecount
    
print(count_evens(10,11,12,13,14))
    
def count_odd(*args):
    odd=len([num for num in args if num%2!=0])
    return odd
print(count_odd(11,12,13,14,15,16,17))


def product_of_nums(*args):
    product=1
    for num in args:
        product=product*num
    return product
print(product_of_nums(1,2,3))
print(product_of_nums(1,2,3,4))
print(product_of_nums(1,2,3,4,5))