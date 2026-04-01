def minimum_size_subarray_sum(arr: list, target: int) -> int:
    #[2,3,1,2,4,3]
    #target =7
    #output = 2
    
    if not arr:
        return 0
    
    if len(arr) == 1:
        if arr[0] >= target:
            return 1
        else:
            return 0
    
    res = float("inf")
    total = 0
    left_pointer = 0

    for right_pointer in range(len(arr)):
        total = total + arr[right_pointer]
        while total >= target and left_pointer <= right_pointer:
            res = min(res, right_pointer - left_pointer +1)
            total -= arr[left_pointer]
            left_pointer +=1
    if res == float("inf"):
        return 0
    else:
        return res



        

