
def reverse_a_no(n):
    maxi, mini = 2**31 -1, -2**31
    if n < 0:
        sign = -1
    else:
        sign = 1
    n = abs(n)
    rev = 0
    while n != 0:
        lastdigit = n % 10
        rev = rev * 10 + lastdigit
        n = n//10
        if rev > maxi:
            return 0
    
    return rev * sign

# test cases
print(reverse_a_no(7789)) # 9877
print(reverse_a_no(-1234)) # -4321
print(reverse_a_no(1000)) # 1
print(reverse_a_no(12143)) # 1001



'''
Explanation:
let n = 7789 so if n // 10 gives 778 and lastdigit = n % 10 gives 9
r = r * 10 + lastdigit = 0 * 10 + 9 = 9
n = 778
n = n // 10 = 77
r = r * 10 + lastdigit = 9 * 10 + 7 = 97
'''