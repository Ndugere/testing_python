def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    sorted_list = []

    left_ind = 0
    right_ind = 0

    while left_ind < len(left_arr) and right_ind < len(right_arr):
        if left_arr[left_ind] <= right_arr[right_ind]:
            sorted_list.append(left_arr[left_ind])
            left_ind += 1
        
        else:
            sorted_list.append(right_arr[right_ind])
            right_ind += 1

    sorted_list.extend(left_arr[left_ind:])
    sorted_list.extend(right_arr[right_ind:])

    return sorted_list
