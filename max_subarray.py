def max_subarray(nums: list) -> int:
    if not nums:
        return 0

    current_sum = nums[0]
    max_total = nums[0]

    for i in range(1, len(nums)):
        # decision: continue vs restart
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]   # restart here
        else:
            current_sum += nums[i]  # continue

        max_total = max(max_total, current_sum)

    return max_total