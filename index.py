def search(arr, low, high, elem):
    if high >= low:
        middle = (high + low) // 2

        if arr[middle] == elem:
            return middle
        elif arr[middle] > elem:
            return search(arr, low, middle - 1, elem)
        else:
            return search(arr, middle + 1, high, elem)
    
    else:
        return -1

array = [1, 20, 45, 70, 80, 98, 120, 145, 170, 230, 286, 345, 500]

print(search(array, 0, len(array)-1, 286))