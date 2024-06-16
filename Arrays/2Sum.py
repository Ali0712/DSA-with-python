# def two_sum(nums, target):

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] == target:
#                 return [i, j]
#     return None

def two_sum_2(nums, target):
    map = {}
    for i in range(len(nums)):
        value = nums[i]
        diff = target - value
        if diff in map:
            return [map[diff], i]
        
        map[value] = i
    return None


# test cases
print(two_sum_2([2, 7, 11, 15], 9))  # [0, 1] 
print(two_sum_2([3, 2, 4], 6))  # [1, 2]
print(two_sum_2([5, 2, 7, 32, 43, 12 ,54 ,33, 65, 35, 76, 4], 47))  # [5, 9]

'''
Explanation:
- We create a dictionary to store the value and its index.
- We iterate through the list of numbers.
- We calculate the difference between the target and the value.
- If the difference is in the dictionary, we return the index of the difference and the current index.
- Otherwise, we add the value and its index to the dictionary.
- If we don't find any pair, we return None.

Time complexity: O(n)
let [2, 7, 11, 15], target = 9
map = {}
i = 0, value = 2, diff = 9 - 2 = 7
map = {2: 0}
i = 1, value = 7, diff = 9 - 7 = 2
2 in map, return [0, 1]

'''
