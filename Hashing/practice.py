'''
Hashing or map or dict is used to store key-value pairs. It is used to store data in such a way that it can be retrieved very quickly using keys. For finding the frequency of elements in an array, we can use hashing. We can also use hashing to find the frequency of characters in a string.
Also we can use hashing to check if a string is a palindrome or not.
'''


def count_occurence(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

# print(count_occurence([1, 2, 3, 4, 4, 2, 1, 4]))

def count_occurence_str1(s):
    counter = [0] * 26
    for i in s:
        counter[ord(i) - ord('a')] += 1
    return counter

# print(count_occurence_str1("hello"))

def count_occurence_str2(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(count_occurence_str2("hello"))


