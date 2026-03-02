def all_missing_numbers(arr: list) -> list:
    n = len(arr)
    present_ints = set(arr)
    missing_ints = []

    for i in range(1, n + 1):
        if i not in present_ints:
            missing_ints.append(i)
    
    return missing_ints