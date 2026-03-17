# Write a function that takes three numbers as parameters and returns the largest number.
def largest(n1,n2,n3):
    if n1>n2 and n1>n3:
        n1_lrg="n1 is largest"
        print(n1_lrg)
        return n1
    elif n2>n1 and n2>n3:
        n2_lrg="n2 is largest"
        print(n2_lrg)   
        return n2 
        
        
    else:
        n3_lrg="n3 is largest"
        print(n3_lrg)
        return n3
print(largest(12,13,14))
print(largest(22,44,45))
print(largest(13,100,67))