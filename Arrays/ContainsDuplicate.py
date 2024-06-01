def contains_duplicate(array):
    seen = set()
    for i in array:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


# test cases
print(contains_duplicate([1, 2, 3, 4, 5]))  # False
print(contains_duplicate([1, 2, 3, 4, 5, 1]))  # True
