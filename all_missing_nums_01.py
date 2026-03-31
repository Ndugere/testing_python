def all_missing_nums(nums: list) -> list:
    res = []
    for num in nums:
        if abs(num) < len(nums):
            nums[abs(num)] = - (abs(nums[num]))
    
    for i, num in nums:
        if num > 0:
            res.append(i)
    
    return res
    
