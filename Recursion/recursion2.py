
def sum_to_n(n, sum):
    
    # if n < 1:
    #     return sum
    # sum += n
    # return sum_to_n(n-1, sum)

    if n < 1:
        print(sum)
        return
    sum += n
    sum_to_n(n-1, sum)

# functional approach
def sum_to_n2(n):
    if n == 0:
        return 0
    return n + sum_to_n2(n-1)

'''
visualize the recursion tree of sum_to_n2 function
sum_to_n2(5)
    5 + sum_to_n2(4)
        4 + sum_to_n2(3)
            3 + sum_to_n2(2)
                2 + sum_to_n2(1)
                    1 + sum_to_n2(0)
                        return 0
                    return 1
                return 3
            return 6
        return 10
    return 15
'''

# sum_to_n(5, 0)
print(sum_to_n2(5))

'''
Explanation:
The above function calculates the sum of numbers from 1 to n.
The function takes two arguments n and sum. The function returns the sum of numbers from 1 to n.
The base case is when n < 1, the function returns the sum.

let n = 5
sum = 0, n = 5
sum = 5, n = 4 
sum = 9, n = 3
sum = 12, n = 2
sum = 14, n = 1
sum = 15, n = 0
return 15, sum = 15
'''
