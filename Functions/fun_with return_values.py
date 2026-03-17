# create function is_odd with para num return true if num is odd else return false
def is_odd(num):
    if num%2!=0:
        return True
    else:
        return False
print(is_odd(3)) 
print(is_odd(10))

#create fun is_even with para num return true if num is even else false
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(10))    
#create fun is_positive with para num return true if num is positive else false
def is_positive(num):
    if num>0:
        return True
    else:
        return False
print(is_positive(120))

# create function is_zero with para num return true if num is zero else false
def is_zero(num):
    if num==0:
        return True
    else:
        return False
print(is_zero(5))
print(is_zero(0))    
  