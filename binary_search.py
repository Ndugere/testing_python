def binary_search(s, target):
    l, r = 0, len(s)-1


    while l <= r:
        mid = (l+ r) // 2
        if s[mid] == target:
            return mid
        
        elif s[mid] > target:
            r = mid - 1
        
        else:
            l = mid + 1
    
    return -1