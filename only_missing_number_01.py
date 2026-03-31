def only_missing_number(nums: list) -> int:
    expected_sum = ((len(nums) + 1) * len(nums)) // 2
    real_sum = sum(nums)
    return expected_sum - real_sum