
# def leaders_of_array(arr):
#     n = len(arr)
#     max_right = arr[n - 1]
#     print(max_right, end=' ')
#     for i in range(n - 2, -1, -1):
#         if arr[i] >= max_right:
#             max_right = arr[i]
#             print(max_right, end=' ')
#     print()

# if we want to print the leaders from left to right
def leaders_of_array(arr):
    n = len(arr)
    maxi = [arr[n - 1]]
    for i in range(n - 2, -1, -1):
        if arr[i] >= maxi[-1]:
            maxi.append(arr[i])
    return maxi[::-1]

# test cases
print(leaders_of_array([16, 17, 4, 3, 5, 2]))  # 2 5 17
print(leaders_of_array([1, 2, 3, 4, 0]))  # 0 4
print(leaders_of_array([7, 4, 5, 7, 3]))  # 3 7 7
print(leaders_of_array([1, 2, 3, 4]))  # 4