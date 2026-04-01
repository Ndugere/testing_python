def contains_duplicate(arr: list, k: int) -> bool:
    # [1,2,3,1]
    # k = 3
    seen = set()
    for i in range(k):
        if arr[i] in seen:
            return True
        else:
            seen.add(arr[i])
    left_pointer, right_pointer = 0, k
    while right_pointer < len(arr):
        if arr[left_pointer] == arr[right_pointer]:
            return True
        left_pointer +=1
        right_pointer+=1
    return False
    