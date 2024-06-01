
def check_palindrome(x):
    # return str(x) == str(x)[::-1]

    # without using string
    if x < 0:
        return False
    rev = 0
    temp = x
    while temp != 0:
        lastdigit = temp % 10
        rev = rev * 10 + lastdigit
        # rev = rev * 10 + x % 10
        temp = temp // 10
    
    return rev == x


# test cases
print(check_palindrome(121)) # True
print(check_palindrome(-121)) # False
print(check_palindrome(10)) # False
print(check_palindrome(-101)) # False

'''
Explanation:
let x = 121 so if x // 10 gives 12 and lastdigit = x % 10 gives 1
r = r * 10 + lastdigit = 0 * 10 + 1 = 1
x = 12
x = x // 10 = 1
r = r * 10 + lastdigit = 1 * 10 + 2 = 12
'''