def sorted_squares(nums):
    if not nums:
        return []
    if nums[0] >= 0:
        return [x * x for x in nums]
    
    res = [0] * len(nums)
    pos = len(nums) -1
    left_pointer, right_pointer = 0, len(nums) -1

    while left_pointer<= right_pointer:
        if abs(nums[right_pointer]) > abs(nums[left_pointer]):
            res[pos] = nums[right_pointer] ** 2
            right_pointer -=1
        else:
            res[pos] = nums[left_pointer] **2
            left_pointer +=1
        pos-=1
    return res
