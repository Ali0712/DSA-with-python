
def hcf(a, b):
    while b!=0:
        a, b = b, a % b
    
    return a

def lcm(a, b):
    lcm = (a * b) // hcf(a, b)
    return lcm

# test cases
print(hcf(10, 15)) # 5
print(hcf(10, 20)) # 10
print(hcf(10, 25)) # 5
print(hcf(12, 32)) # 4


'''
Explanation:
    let a = 10, b = 15
    a, b = b, a % b = 15, 10 % 15 = 15, 10
    a, b = b, a % b = 10, 15 % 10 = 10, 5
    a, b = b, a % b = 5, 10 % 5 = 5, 0
    a = 5
    so the hcf of 10 and 15 is 5

    this is the euclidean algorithm for finding hcf
    hcf(a, b) = hcf(b, a % b)
    if b == 0 then return a
    else repeat the process

    
'''