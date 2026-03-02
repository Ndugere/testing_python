def missing_number(arr: list[int]) -> int:
    arr.sort()

    if arr[0] != 0:
        return 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1] + 1:
            return arr[i - 1] + 1

    return arr[-1] + 1