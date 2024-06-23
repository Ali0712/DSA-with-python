# 15. 3Sum

def three_sum(arr):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = n-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1              
    return ans

def three_sum1(arr):
    ans = set()
    hashset = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            x = (arr[j]+arr[i]) * -1
            if x in hashset:
                temp = sorted([arr[i], arr[j], x])
                ans.add(tuple(temp))
            hashset.add(arr[j])
        hashset.clear()
    ans = list(list(i) for i in ans)
    return ans

# test cases
print(three_sum([-1,0,1,2,-1,-4,4,3,2,0,-3])) # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([])) # []
print(three_sum([0])) # []
print(three_sum([0,0,0])) # [[0, 0, 0]] 