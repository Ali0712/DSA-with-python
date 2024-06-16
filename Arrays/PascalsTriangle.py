# 118. Pascal's Triangle

def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
        
    # we can also use generate row function to generate the pascal's triangle
    # triangle = []
    # for i in range(n):
    #     row = pascal_triangle_row(i+1)
    #     triangle.append(row)
    # return triangle


# test cases
print(generate_pascal_triangle(1))
print(generate_pascal_triangle(5))
print(generate_pascal_triangle(10))


# if we have given row and column number, then we can find the value at that position by using the formula  nCr
def pascal_triangle_no(row, column):
    # if column == 0 or column == row:
    #     return 1
    # return pascal_triangle_no(row-1, column-1) + pascal_triangle_no(row-1, column)

    # we can also use the formula nCr = n! / r! * (n-r)!
    # nCr = n! / r! * (n-r)!
    # nCr = n * (n-1) * (n-2) * ... * (n-r+1) / r!

    result = 1
    for i in range(column):
        result *= (row - i)
        result //= (i + 1)

    return result

# test cases
# n-1C r-1 so always pass n-1 and r-1
# print(pascal_triangle_no(2-1,1-1))
# print(pascal_triangle_no(5-1,3-1)) 

# if we have to return the entire row of pascal's triangle
def pascal_triangle_row(n):
    # result = []
    # for i in range(n):
    #     result.append(pascal_triangle_no(n-1, i))
    # return result

    result = [1]
    ans = 1
    for i in range(1, n):
        ans = ans * (n-i) // i
        result.append(ans)
    return result

# test cases
# print(pascal_triangle_row(1))
# print(pascal_triangle_row(5))