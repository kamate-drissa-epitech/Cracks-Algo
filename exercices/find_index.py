def find_index(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        guess_index = (low + high) // 2
        guess = arr[guess_index]

        if guess == target:
            return guess_index
        if guess < target:
            low  = guess_index + 1
        elif guess > target:
            high  = guess_index - 1
    return -1



def find_smallest(arr):
    smallest_index = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index
       

     

def find_missing(arr):
    newArr = []
    copiedArr = list(arr)

    for i in range(len(copiedArr)):
        small = find_smallest(copiedArr)
        newArr.append(copiedArr.pop(small))

    for i in range(len(newArr) - 1 ):
        interval = newArr[i + 1] - newArr[i]
        if interval != 1:
            return newArr[i] + 1
        
    return newArr[-1] + 1

   

def sum(arr : list):
    
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


def count(arr: list):
    if len(arr) == 0:
        return 0
    return 1 + count(arr[1:])


def find_maximum(arr : list):
    if len(arr) == 2:
        return arr[1] if arr[1] > arr[0] else arr[0]
    sub_max = find_maximum(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(find_maximum([1, 2, 3, 4]))