# Two Pointer Technique to find pair with given target sum,target=10

# def pair_sum(arr, target):
#     # Step 1: Sort the array
#     arr.sort()
    
#     # Step 2: Initialize two pointers
#     left = 0
#     right = len(arr) - 1
    
#     # Step 3: Loop until left < right
#     while left < right:
#         current_sum = arr[left] + arr[right]
        
#         # Case 1: If sum equals target
#         if current_sum == target:
#             print("Pair found:", arr[left], arr[right])
#             return
        
#         # Case 2: If sum is less than target → move left pointer
#         elif current_sum < target:
#             left += 1
        
#         # Case 3: If sum is greater than target → move right pointer
#         else:
#             right -= 1
    
#     print("No pair found")


# Example usage
# numbers = [2, 7, 4, 1, 9, 5]
# target = 10

# pair_sum(numbers, target)



def two_pair_sum(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            print(arr[left],arr[right])
            return
        elif current_sum<target:
            left+=1

        else:
            right=-1
        print("no pair found")
two_pair_sum([1,2,3,4,5],6)