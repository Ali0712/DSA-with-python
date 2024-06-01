
def largest_element(arr):
    '''this function returns the largest element from the array'''
    
    largest = arr[0]
    
    for i in arr:
        if i > largest:
            largest = i
            
    return largest

# test cases
print(largest_element([4, 6, 2, 5 ,7, 9, 1 , 9,3, 10]))
print(largest_element([5, 2, 3, 1]))
print(largest_element([1, 25, 43, 45,13, -32, 232, 42 ,21]))