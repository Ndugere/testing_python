def all_missing_nums(nums: list) -> list:

    set_of_nums = set(nums)
    res = []

    for i in range(len(nums) +1):
        if i not in set_of_nums:
            res.append(i)
    return res

