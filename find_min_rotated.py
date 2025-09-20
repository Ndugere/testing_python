def find_min_rotated(arr):
    left, right = 0, len(arr) -1

    res = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


 