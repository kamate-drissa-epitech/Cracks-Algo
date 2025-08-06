def binary_search(arr : list, target : int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return guess
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binary_search([1,5,8,9,7], 5))
    


