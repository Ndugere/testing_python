import collections
def sortedSquares(nums: list) -> list:
    if not nums:
        return []
    if nums[0] >= 0:
        return [x * x for x in nums]
    
    res = collections.deque()
    left_pointer, right_pointer = 0, len(nums) -1
    while left_pointer<=right_pointer:
        if abs(nums[right_pointer]) > abs(nums[left_pointer]):
            res.appendleft(nums[right_pointer] * nums[right_pointer])
            right_pointer -=1
        else:
            res.appendleft(nums[left_pointer] * nums[left_pointer])
            left_pointer+=1
    return list(res)

       