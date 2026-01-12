def merge_sort(arr=[5, 4, 1, 2, 3, 7, 7, 8]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_side = merge_sort(arr[:mid])
    right_side = merge_sort(arr[mid:])

    i = 0
    j = 0
    res = []

    # Merge step
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            res.append(left_side[i])
            i += 1
        else:
            res.append(right_side[j])
            j += 1

    # Add leftovers
    res.extend(left_side[i:])
    res.extend(right_side[j:])

    return res

print(merge_sort())
