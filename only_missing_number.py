def only_missing_number(nums: list) -> int:
    set_of_nums = set(nums)
    for i in range(len(nums) +1):
        if i not in set_of_nums:
            return i