def bubble_sort(arr):
    for i in range(len(arr) - 1):
        is_sorted = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if is_sorted:
            break
    return arr
