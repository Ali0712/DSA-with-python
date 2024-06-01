
def check_palindrome(s):
    '''Check if a string is a palindrome by slicing.'''
    return s == s[::-1]

def check_palindrome2(s, i=0):
    '''Check if a string is a palindrome by recursion.'''
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return check_palindrome2(s, i+1)


def check_palindrome_leetcode(s):
    a = ''
    for i in s:
        if i.isalnum():
            a += i.lower()
    
    # for i in range(len(a)//2):
    #     if a[i] != a[len(a)-i-1]:
    #         return False
    # return True
    l = 0
    r = len(a)-1
    while l <= r:
        if a[l] != a[r]:
            return False
        l += 1
        r -= 1
    return True

print(check_palindrome_leetcode("A man, a plan, a canal: Panama"))