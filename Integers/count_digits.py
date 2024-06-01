
def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10

    return count

'''
Explanation:
let n = 124
124//10 -- 12
12//10  -- 1
1//10   -- 0
so loop is running 3 times which is also the no of digits
'''

# test cases
print(count_digits(10)) # 2
print(count_digits(12345)) # 5
print(count_digits(100)) # 3


