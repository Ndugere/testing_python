def starting_and_ending_index_of_target_in_a_sorted_array(arr: list, target: int) -> list:
    # [1,2,2,2,3,4,5]
    res = [-1, -1]
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left +right)//2
        if arr[mid] > target:
            right = mid -1
        elif arr[mid] < target:
            left = mid + 1
        else:
            res[0] = mid
            right = mid -1
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left +right)//2
        if arr[mid] > target:
            right = mid -1
        elif arr[mid] < target:
            left = mid + 1
        else:
            res[1] = mid
            left = mid +1
    
    return res
    