
def second_largest_element(arr):
    '''this function returns the second largest element from the array, if not present return -1'''
    
    largest = arr[0]
    second_largest = -1

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i < largest and i > second_largest:
            second_largest = i
            
    return second_largest


# test cases
print(second_largest_element([12, 35, 1, 10, 34, 1])) # 34
print(second_largest_element([10, 5, 10])) # 5
print(second_largest_element([10, 10, 10])) # -1
print(second_largest_element([10, 105, 105,10, 5])) # 10
print(second_largest_element([10])) # -1