# 121. Best Time to Buy and Sell Stock

def maxProfit(arr):
    i = 0
    j = 1
    maxprofit = 0
    while j < len(arr):
        profit = arr[j] - arr[i]
        if arr[j] < arr[i]:
            i = j
        maxprofit = max(profit, maxprofit)
        j += 1
    return maxprofit

    # maxprofit = 0
    # buy = arr[0]
    # for i in range(1, len(arr)):
    #     profit = arr[i] - buy

    #     if profit > maxprofit:
    #         maxprofit = profit

    #     buy = min(buy, arr[i]) 
    # return maxprofit 


# test cases
print(maxProfit([7,1,5,3,6,4,0,9])) # 9 
print(maxProfit([7,6,4,3,1])) # 0
print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([1,4,2])) # 3