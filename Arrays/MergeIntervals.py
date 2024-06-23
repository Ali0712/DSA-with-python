# 56. Merge Intervals

def merge_intervals(arr):
    if not arr:
        return []
    
    arr.sort(key=lambda interval: interval[0])
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], arr[i][1])
        else:
            result.append(arr[i])
    return result


# test cases
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]])) # [[1,5]]
print(merge_intervals([[1,4],[0,4]])) # [[0,4]]
print(merge_intervals([[1,4],[2,3]])) # [[1,4]]
