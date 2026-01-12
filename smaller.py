def solution(nums):
    sorted_nums = sorted(nums)
    num_to_index = {}
    res = []

    for i, num in enumerate(sorted_nums):
        if num not in num_to_index:
            num_to_index[num] = i

    for each_num in nums:
        res.append(num_to_index[each_num])
    return res



