from arraysearch import constants

def ternary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle1 = left + (right - left) // 3
        middle2 = right - (right - left) // 3

        if list[middle1] == target:
            return middle1
        if list[middle2] == target:
            return middle2

        if target < list[middle1]:
            right = middle1 - 1
        elif target > list[middle2]:
            left = middle2 + 1
        else:
            left = middle1 + 1
            right = middle2 - 1

    return -1  

def linear_search(list, target):
    for i,elem in enumerate(list):
        if elem == target:
            return i
        
    return -1

def binary_search(list, target):
    left: int = 0
    right: int = len(list) - 1

    while left <= right:
        middle: int = (right + left) // 2
        
        if list[middle] == target:
            return middle
        
        if list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
