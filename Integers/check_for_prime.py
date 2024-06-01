
def check_for_prime(n):
    if n == 1:
        return False
    
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n//i != i:
                count += 1
    
    return count == 2

# test cases
print(check_for_prime(10)) # False
print(check_for_prime(3)) # True
print(check_for_prime(5)) # True

'''
Explanation:
refer to print_all_divisors.py for the explanation of the loop
'''