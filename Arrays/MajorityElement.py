# 169. Majority Element

# using Boyer-Moore Voting Algorithm
def majority_element(arr):
    element = None
    count = 0
    for i in arr:
        if count == 0:
            count += 1
            element = i
        elif i == element:
            count += 1
        else:
            count -= 1
    return element
        

def majority_element2(arr):
    # arr.sort()
    # return arr[len(arr)//2]
    counter = {}
    for i in arr:
        counter[i] = counter.get(i, 0) + 1
    for key, value in counter.items():
        if value > len(arr) // 2:
            return key
    
    return -1

# test cases
print(majority_element([3,2,3])) # 3
print(majority_element([2,2,1,1,1,2,2])) # 2
print(majority_element([1])) # 1
print(majority_element([1,1])) # 1

'''
In Moore's Voting Algorithm, we first find a candidate for majority element.
Then we check if the candidate is the majority element.
If it is, we return the candidate.
If it is not, we return -1.

Time complexity: O(n)
Space complexity: O(1)
'''