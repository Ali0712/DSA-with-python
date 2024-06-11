# 73. Set Matrix Zeroes

# without using extra space
def set_matrix_zero(arr):
    col = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                arr[i][0] = 0
                if j != 0:
                    arr[0][j] = 0
                else:
                    col = 0
    
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if arr[i][0] == 0 or arr[0][j] == 0:
                arr[i][j] = 0
    
    if arr[0][0] == 0:
        for j in range(len(arr[0])):
            arr[0][j] = 0
    if col == 0:
        for i in range(len(arr)):
            arr[i][0] = 0
    return arr


# using extra space
def set_matrix_zero_extraspace(arr):
    r = [1] * len(arr)
    c = [1] * len(arr[0])

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                r[i] = 0
                c[j] = 0
        
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if r[i] == 0 or c[j] == 0:
                arr[i][j] = 0

    return arr

# test cases
print(set_matrix_zero([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(set_matrix_zero([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(set_matrix_zero([[1,1,1],[0,1,2]])) # [[0,1,1],[0,0,0]]