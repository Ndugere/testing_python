def find_boundary(arr):
    left, right = 0, len(arr) -1
    res = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == True:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return res