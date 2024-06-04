# 121. Best Time to Buy and Sell Stock

def maxProfit(arr):
    i = 0
    j = len(arr) -1
    # max_profit = arr[j] - arr[i]
    max_profit = 0
    while i < j:
        profit = arr[j] - arr[i]
        if profit < 0:
            j -= 1          
        i += 1

        max_profit = max(profit, max_profit)

    return max(max_profit, 0)

# test cases
print(maxProfit([7,1,5,3,6,4,0,9])) # 9 
print(maxProfit([7,6,4,3,1])) # 0
print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([1,4,2])) # 3