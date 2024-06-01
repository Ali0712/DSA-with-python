
def fabonacci(n):
    '''this function prints the fabonacci series using for loop'''
    a, b = 0, 1
    print(a, b, end=' ')
    for i in range(2, n):
        print(a+b, end=' ')
        a , b = b, a+b

def fabonacci_rec(n):
    '''this function prints the fabonacci series using recursion'''
    if n <= 1:
        return n
    return fabonacci_rec(n-1) + fabonacci_rec(n-2)
        
print(fabonacci_rec(10)) # 55

