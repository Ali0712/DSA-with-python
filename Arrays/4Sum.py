# 18. 4Sum

def four_sum(arr, target):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            left = j+1
            right = n-1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
    return ans


def four_sum1(arr, target):
    if len(arr) < 4:
        return []
    ans = set()
    hashset = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                fourth = target - (arr[i]+arr[j]+arr[k])
                if fourth in hashset:
                    ans.add(tuple(sorted([arr[i], arr[j], arr[k], fourth])))
                hashset.add(arr[k])
            hashset.clear()
    return ans

# test cases
print(four_sum([1, 0, -1, 0, -2, 2], 0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(four_sum([], 0)) # []
print(four_sum([0], 0)) # []


def k_sum(arr, target, k):
    def k_sum_helper(arr, target, k, start, end):
        if k == 2:
            return two_sum(arr, target, start, end)
        ans = []
        for i in range(start, end):
            if i > start and arr[i] == arr[i-1]:
                continue
            temp = k_sum_helper(arr, target-arr[i], k-1, i+1, end)
            for t in temp:
                ans.append([arr[i]] + t)
        return ans

    def two_sum(arr, target, start, end):
        ans = []
        left = start
        right = end
        while left < right:
            total = arr[left] + arr[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                ans.append([arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
        return ans

    arr.sort()
    return k_sum_helper(arr, target, k, 0, len(arr)-1)

# test cases
print(k_sum([1, 0, -1, 0, -2, 2], 0, 4)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(k_sum([], 0, 4)) # []
print(k_sum([0], 0, 4)) # []
print(k_sum([1, 0, -1, 0, -2, 2], 0, 2)) # [[-2, 2], [-1, 1], [0, 0]]