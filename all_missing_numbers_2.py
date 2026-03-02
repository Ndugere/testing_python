def all_missing_numbers(arr: list) -> list:
    n = len(arr)
    missing = []

    for i in range(n):
        val = abs(arr[i])

        if 0 < val <= n:
            arr[val - 1] = -abs(arr[val - 1])
    
    for i, each_item in enumerate(arr):
        if each_item > 0:
            missing.append(i + 1)
    
    return missing