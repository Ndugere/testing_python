def longest_mountain(arr: list) -> int:
    # arr = [2,1,4,7,3,2,5]

    res = 0

    for i in range(1, len(arr) -1):
        if arr[i -1] < arr[i] > arr[i +1]:
            left_pointer, right_pointer = i-1, i+1
            while left_pointer> 0 and arr[left_pointer -1] < arr[left_pointer]:
                left_pointer -=1
            while right_pointer < len(arr) -1 and arr[right_pointer +1] <arr[right_pointer]:
                right_pointer+=1
            res = max(res, (right_pointer -left_pointer)+1)
    return res