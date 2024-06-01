
def is_armstrong(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    
    return sum == n

# test cases
print(is_armstrong(153)) # True
print(is_armstrong(9474)) # True
print(is_armstrong(9478)) # False
print(is_armstrong(1634)) # True
print(is_armstrong(1635)) # False

'''
Explanation:
Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
'''