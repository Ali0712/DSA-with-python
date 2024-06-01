
def print_all_divisors(n):
    factors = []
    # int(n**0.5) is the square root of n
    # like if n=100 then int(n**0.5) = 10, so the range will be 1 to 10 and adding 1 so that 10 is also included
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    
    factors.sort()
    return factors

''' 
Explanation:
    let n = 36
    factors are 1, 2, 3, 4, 6, 9, 12, 18, 36
    1 X 36 = 36
    2 X 18 = 36
    3 X 12 = 36
    4 X 9 = 36
    6 X 6 = 36
    ------------
    9 X 4 = 36
    12 X 3 = 36
    18 X 2 = 36
    36 X 1 = 36

here we can see after 6 which is sqrt of n factors are repeating so we can stop at sqrt(n),
but too include all factors we need to add n//i also in the list which gives the multiplier to get n

first check for i = 1, 36 % 1 == 0, so add 1 and 36//1 = 36, so add 36
then check for i = 2, 36 % 2 == 0, so add 2 and 36//2 = 18, so add 18

'''


# test cases
print(print_all_divisors(10)) # [1, 2, 5, 10]
print(print_all_divisors(15)) # [1, 3, 5, 15]
print(print_all_divisors(100)) # [1, 2, 4, 5, 10, 20, 25, 50, 100]


