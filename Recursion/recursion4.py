
def reverse_an_array(arr):
    '''This function reverses an array using pop and insert methods.'''
    for i in range(len(arr)):
        # last = arr.pop()
        arr.insert(i, arr.pop())
    return arr

def reverse_an_array2(arr):
    '''This function reverses an array using two pointers.'''
    start = 0
    end = len(arr) -1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def reverse_an_array3(arr):
    '''This function reverses an array using slicing.'''
    return arr[::-1]

def reverse_an_array4(arr, start, end):
    '''This function reverses an array using recursion with two pointers.'''
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_an_array4(arr, start+1, end-1)
    return arr
    



print(reverse_an_array([1, 2, 3, 4, 5, 6])) # [5, 4, 3, 2, 1]
print(reverse_an_array2([1, 2, 3, 4, 5, 6])) # [5, 4, 3, 2, 1]
print(reverse_an_array3([1, 2, 3, 4, 5, 6])) # [5, 4, 3, 2, 1]
print(reverse_an_array4([1, 2, 3, 4, 5, 6], 0, 5)) # [5, 4, 3, 2, 1, 6]


