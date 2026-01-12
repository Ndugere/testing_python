def solution(nums):
    is_there = set(nums)

    res = []
    
    for num in range(1, len(nums) + 1):
        if num not in is_there:
            res.append(num)
    

    return res

