# 485. Max Consecutive Ones

def count_max_consecutive_ones(arr):
    max_count = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
            # max_count = max(max_count, count)
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count


# test cases
print(count_max_consecutive_ones([1,1,0,1,1,1])) # 3
print(count_max_consecutive_ones([1,0,1,1,0,1])) # 2
print(count_max_consecutive_ones([0,0,0,0,0,0])) # 0
print(count_max_consecutive_ones([1,1,1,1,1,1])) # 6