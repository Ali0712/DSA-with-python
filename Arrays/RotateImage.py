# 48. Rotate Image

# brute force
def rotate_image1(arr):
    n = len(arr)
    res = [[0] * n for _ in range(n)]   
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = arr[i][j]
    return res

# optimized
def rotate_image(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(n):
        arr[i].reverse()
    return arr

# test cases
print(rotate_image([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
print(rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

'''
Explanation:
use indexes to understand the pattern
'''