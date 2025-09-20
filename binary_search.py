def binary_search(s, target):
    left , right = 0, len(s)-1

    while left <= right:
        mid = (left + right) // 2

        if s[mid] == target:
            return mid
        
        elif s[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
    
    return -1



