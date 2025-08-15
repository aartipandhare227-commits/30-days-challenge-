def sortColors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: 
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sortColors(arr))
