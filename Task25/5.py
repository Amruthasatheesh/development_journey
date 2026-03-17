#5. Use a lambda function with filter() to get all even numbers from a list.
lst=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(lambda n:n%2==0,lst))  #"syntax of filter"==>filter(function,iterable)
print(even_numbers)


