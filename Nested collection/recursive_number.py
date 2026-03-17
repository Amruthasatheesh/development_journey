#create a new collection that contains recursive numbers
nums=[10,11,10,11,12,13,14,15,16,15]
recursive_num={num for num in nums if nums.count(num)>1}
print(recursive_num)