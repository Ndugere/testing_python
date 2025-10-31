def solution(nums):

    sorted_nums = sorted(nums)

    is_there = set(sorted_nums)

    res = []

    for num in range(1, sorted_nums[len(sorted_nums) - 1]):
        if num not in is_there:
            res.append(num)

    return res
