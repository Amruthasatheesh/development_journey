#check 9 is fibonacci number ,if its true returns True,else False
def is_fibonacci_number(number):
    is_fibo=False
    prev=0
    curr=1
    next=prev+curr
    while(next<=number):
        next=prev+curr
        prev=curr
        curr=next
        if next==number:
            is_fibo=True
            break
    return is_fibo
print(is_fibonacci_number(9))
print(is_fibonacci_number(2))
print(is_fibonacci_number(5))
         