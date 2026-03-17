# largest and smallest in a list
numbers=[20,30,10,9,8]

numbers.sort()
print(f"smallest number in the list is {numbers[0]}")
print(f"largest number in the list is {numbers[4]}")

# count how many even numbers in a list
numbers=[2,4,6,7,9,3]
for num in numbers:
    if num%2==0:
        numbers.count(num)
print(num)
# reverse a list without using reverse method()
numbers=[2,4,8,1]
reverse=numbers[::-1]
print(reverse)
