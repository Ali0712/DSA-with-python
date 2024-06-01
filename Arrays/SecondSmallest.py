
def second_smallest(arr):
    small = arr[0]
    second_small = -1

    for i in arr:
        if i < small:
            second_small = small
            small = i
        elif i > small and i < second_small:
            second_small = i

    return second_small 


# test cases
print(second_smallest([12, 35, 1, 10, 34, 9, 0, 1])) # 1
print(second_smallest([10, 5, 10])) # 10
print(second_smallest([10, 10, 10])) # -1
print(second_smallest([10, 105, 105,10, 5])) # 10