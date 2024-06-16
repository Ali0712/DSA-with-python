# 229. Majority Element II

def majority_element(arr):
    count1, count2 = 0, 0
    element1, element2 = None, None

    for i in arr:
        if count1 == 0 and i != element2:
            count1 += 1
            element1 = i
        
        elif count2 == 0 and i != element1:
            count2 += 1
            element2 = i
        
        elif i == element1:
            count1 += 1
        
        elif i == element2:
            count2 += 1
        else:
            count1, count2 = count1-1, count2-1
    
    res = []
    c1, c2 = 0, 0
    threshold = len(arr) // 3
    for i in arr:
        if i == element1:
            c1 += 1
        elif i == element2:
            c2 += 1
        
    if c1>threshold:
        res.append(element1)
    if c2>threshold:
        res.append(element2)
    return res


def majority_element2(arr):
    store = {}
    res = []
    threshold = len(arr) // 3

    for i in arr:
        store[i] = store.get(i, 0) + 1
        if store[i] > threshold and i not in res:
            res.append(i)
    return res

# test cases
print(majority_element([3,2,3])) # [3]
print(majority_element([1,1,1,3,3,2,2,2])) # [1,2]
print(majority_element([1])) # [1]