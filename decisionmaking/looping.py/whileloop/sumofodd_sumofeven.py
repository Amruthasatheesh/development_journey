#w.a.p to display sum of even and sum of odd numbers up to limit 6


num=int(input("enter the number:"))

i=1
odd_sum=0# even numbers sum up to limit so here the new var even_sum 
even_sum=0
while(i<=num):
    if i%2==0:   
       even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i

    i=i+1

print(even_sum,"even number")
print(odd_sum," odd number")    

