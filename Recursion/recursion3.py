
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# print(factorial(5)) # 120

def factorial2(i, n):
    if n == 0:
        print(i)
        return
    i *= n
    factorial2(i, n-1)

factorial2(1, 5) # 120


