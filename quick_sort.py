def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left_side = []
    right_side = []

    for each_value in arr[1:]:
        if each_value <= pivot:
            left_side.append(each_value)
        else:
            right_side.append(each_value)
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
