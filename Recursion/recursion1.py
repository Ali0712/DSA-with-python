
def print_no1(i, n): # print numbers from i to n e.g 1 to 4 , 1 2 3 4
    if i > n:
         return
    print(i, end = ' ')
    print_no1(i+1, n)

print_no1(1, 4)
print()

def print_no2(i, n): # print numbers from n to i e.g 4 to 1 , 4 3 2 1
    if n < i:
        return
    
    print(n, end = ' ')
    print_no2(i, n-1)
    
print_no2(1, 4)
print()


def print_no3(n):
    if n < 1:
        return
    print_no3(n-1)
    print(n, end = ' ')

print_no3(4)
print()


def print_no4(i, n):
    if i > n:
        return
    print_no4(i+1, n)
    print(i, end = ' ')

print_no4(1, 4)



     