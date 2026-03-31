def overlap_check(nums: list) -> bool:

    if len(nums) <= 1:
        return True
    nums.sort()

    for i in range(len(nums) -1):
        if nums[i][1] > nums[i +1][0]:
            return False
    return True
