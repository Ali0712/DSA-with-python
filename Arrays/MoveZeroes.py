# 283. Move Zeroes

def move_zeroes(arr):
    # n = len(arr)
    
    # i = 0
    # for j in range(1, n):
    #     if arr[i] == 0 and arr[j] != 0:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         i += 1
    #     if arr[i] != 0:
    #         i += 1

    # return arr
    
    # 2nd approach
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


# test cases
print(move_zeroes([0,1,0,3,12]))
print(move_zeroes([0]))
print(move_zeroes([1,0,1]))
